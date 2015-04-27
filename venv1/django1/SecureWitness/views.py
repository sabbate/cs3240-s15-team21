# import sys
# import os.path

# sys.path.append(os.path.join(os.path.dirname('views.py'), '..'))
# import gen_py.lib
# from SecureWitness.forms import *
# from django import forms
# from django import forms
import hashlib
import random
import os

from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from SecureWitness.models import Report
from SecureWitness.models import File
from SecureWitness.models import ActivationProfile, GroupProfile
from django import forms

from django.shortcuts import render
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from django.core.mail import send_mail

from SecureWitness.models import *
from .forms import *
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core import serializers
import json
from django.contrib.contenttypes.models import ContentType


class GroupIndexView(generic.ListView):
    template_name = 'SecureWitness/group_index.html'
    context_object_name = 'group_list'

    def get_queryset(self):
        """Return the last five published groups."""
        return Group.objects.order_by('-id')[:5]


class GroupDetailView(generic.DetailView):
    model = Group
    template_name = 'SecureWitness/group_detail.html'


class ReportIndexView(generic.ListView):
    template_name = 'SecureWitness/report_index.html'
    context_object_name = 'report_list'

    def get_queryset(self):
        """Return the last five uploaded reports."""
        return Report.objects.order_by('-RID')[:5]


def index(request):
    reports = Report.objects.raw('SELECT * FROM SecureWitness_report')
    return render(request, 'all-reports.html', {'reports': reports})
    # return HttpResponse("Welcome to SecureWitness!")


def newreport(request):
    return render(request, 'newreport.html')


def submitreport(request):
    if request.POST.get('short', False) and request.POST.get('long', False):
        short = request.POST.get('short', False)
        long = request.POST.get('long', False)
        loc = request.POST.get('location', False)
        date = request.POST.get('date', False)
        keys = request.POST.get('keys', False)
        priv = request.POST.get('private', False)
        password = request.POST.get('pw', False)
        # files = HttpRequest.FILES;

        cur_time = datetime.datetime.now()
        usr = User.objects.get(username=request.user.username)
        r = Report(author_id=usr.id, create_date=cur_time, last_update_date=cur_time, short_desc=short, long_desc=long,
                   location=loc, incident_date=date, keywords=keys, private=priv)
        r.save();
        r = Report.objects.filter(author_id=usr.id, short_desc=short, incident_date=date)[0]
        for key, file in request.FILES.items():
            path = os.getcwd() + '\\SecureWitness\\files\\'
            dest = open(path + file.name, 'wb+')
            dest.write(file.read())
            dest.close()
            encrypt(path, file.name, password)
            f = File(author_id=usr.id, report_id=r.report_id, docfile=path)
            f.save();
        # r.save();
        return HttpResponse('Thank you for submitting a report!')
    else:
        return HttpResponse('Your submission was unsuccessful.')


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if "AND" in q:
            terms = q.split(" AND ");
            r = Report.objects.filter(keywords__icontains=terms[0])
            for word in terms:
                r = r.filter(keywords__icontains=word)
            reports = r
        if "OR" in q:
            terms = q.split(" OR ");
            reports = Report.objects.filter(keywords__icontains=terms[0])
            for word in terms[1:]:
                reports = reports | Report.objects.filter(keywords__icontains=word)
            return render(request, 'search_results.html', {'reports': reports, 'query': q})
        else:
            return HttpResponse('No results found. Please try another search term.')


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        if not user.is_active:
            return HttpResponseRedirect('../user_not_active')
        else:
            if user.is_superuser:
                return HttpResponseRedirect('../../admin')
            else:
                return HttpResponseRedirect('../loggedin')
    else:
        return HttpResponseRedirect('../invalid')


@login_required(login_url="/SecureWitness/account/login")
def loggedin(request):
    c = {}
    c.update(csrf(request))

    try:
        groups = []
        user_to_groups = UserToGroup.objects.filter(user_id=request.user.id)
        for group in user_to_groups:
            groups.append(Group.objects.get(id=group.group_id.id))
    except:
        groups = None

    try:
        reports = []

        # TODO Reports which the user is the author
        reports_author = Report.objects.filter(author_id=request.user)
        for report in reports_author:
            reports.append(report)

        # Need to check ReportUserSharing for every instance of this user
        shared_with_user = ReportUserSharing.objects.filter(user=request.user)
        for item in shared_with_user:
            reports.append(Report.objects.get(report_id=item.report.report_id))
        # Need to check ReportGroupSharing for every instance of a group that the user is in
        if groups:
            for group in groups:
                reports_for_group = Report.objects.filter(group_id=group)
                for item in reports_for_group:
                    reports.append(item)
                reports_shared_with_group = ReportGroupSharing.objects.filter(group=group)
                for item in reports_shared_with_group:
                    reports.append(item)
    except:
        reports = None
    c['full_name'] = request.user.username
    c['groups'] = groups
    c['reports'] = reports
    return render_to_response('loggedin.html', c)


@login_required(login_url="/SecureWitness/account/login")
def admin(request):
    c = {}
    c.update(csrf(request))
    # c['username'] =  request.newAdmin.username
    return render_to_response('admin.html', c)


@login_required(login_url="/SecureWitness/account/login")
def activate_user_view(request):
    username = request.POST.get('username_activate', '')
    try:
        activate = User.objects.get(username=username)
    except:
        return HttpResponseRedirect('../user_activate_failed')

    if not activate.is_active:
        activate.is_active = True
        activate.save()
        if activate.is_active:
            return HttpResponseRedirect('../user_activated')
    else:
        return HttpResponseRedirect('../user_already_activated')


@login_required(login_url="/SecureWitness/account/login")
def suspend_user_view(request):
    username = request.POST.get('username_suspend', '')
    try:
        suspend = User.objects.get(username=username)
    except:
        return HttpResponseRedirect('../user_suspend_failed')

    if suspend.is_active:
        suspend.is_active = False
        suspend.save()
        if not suspend.is_active:
            return HttpResponseRedirect('../user_suspended')
    else:
        return HttpResponseRedirect('../user_already_suspended')


def assigning_admin_view(request):
    username = request.POST.get('username_admin', '')

    try:
        newAdmin = User.objects.get(username=username)
    except:
        return HttpResponseRedirect('../admin_assign_failed')

    if not newAdmin.is_superuser:
        newAdmin.is_superuser = True
        newAdmin.save()
        if newAdmin.is_superuser:
            return HttpResponseRedirect('../admin_assigned')
    else:
        return HttpResponseRedirect('../admin_already_assigned')


@login_required(login_url="/SecureWitness/account/login")
def removing_admin_view(request):
    username = request.POST.get('username_removeadmin', '')

    try:
        admin = User.objects.get(username=username)
    except:
        return HttpResponseRedirect('../admin_remove_failed')

    if admin.is_superuser:
        admin.is_superuser = False
        admin.save()
        if not admin.is_superuser:
            return HttpResponseRedirect('../admin_removed')
    else:
        return HttpResponseRedirect('../not_admin')


def invalid(request):
    return render_to_response('invalid.html')


@login_required(login_url="/SecureWitness/account/login")
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def encrypt(path, filename, root):
    # Open up unencrypted file and read the plaintext into a buffer.
    with open(path + filename, 'r') as f:
        buffer = f.read()
    plaintext = buffer

    # Create a 16 byte SHA hash of the key root
    hash = SHA256.new()
    hash.update(root.encode('utf-8'))
    key = hash.digest()[0:16]

    # Using this newly generated key, create a cipher. Then, use this cipher to encrypt
    # the plaintext
    cipher = AES.new(key, AES.MODE_CFB, 'this is an IV456')
    ciphertext = cipher.encrypt(plaintext)

    # Write the encrypted plaintext (ciphertext) into the same file.
    # NOTE: this ciphertext is written in bytes, not unicode. Notice the "wb" flag
    # in write() instead of just "w".
    with open(path + filename, 'wb') as f:
        # print(ciphertext)
        f.write(ciphertext)
    with open(path + "key_" + filename, 'wb') as f:
        f.write(key)


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = request.POST.get('email', '')
            temp = False  # to see if the user has been saved into the database
            try:
                u = User.objects.get(email=email)
            except:
                form.save()
                user = User.objects.get(username=username)
                user.email = email
                user.is_active = False
                user.save()
                temp = True
            if not temp:
                return render_to_response('duplicate_email.html', {'username': username, 'password': password})

            # form.save()
            # username = form.cleaned_data['username']
            # email = request.POST.get('email', '')
            # user = User.objects.get(username=username)
            # user.is_active = False
            # user.email = email
            # user.is_active = False
            # user.save()
            # try:
            # u = User.objects.get(email = email)
            # except:
            # user.email = email
            # user.is_active = False
            # user.save()
            # if u:
            # return render_to_response('duplicate_email.html', {'user':user})

            # Send email with activation key
            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            user = User.objects.get(username=username)
            new_profile = ActivationProfile(user=user, activation_key=activation_key, key_expires=key_expires)
            new_profile.save()

            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link " \
                         " http://127.0.0.1:8000/SecureWitness/account/confirm/%s" % (username, activation_key)

            send_mail(email_subject, email_body, 'nyxeliza1107@gmail.com',
                      [email], fail_silently=False)
            '''
            s=smtplib.SMTP()
            s.connect("smtp.gmail.com",587)
            s.starttls()
            s.ehlo()
            s.login("nyxeliza1107@gmail.com", "password")
            s.sendmail("nyxeliza1107@gmail.com", email, email_body)
            '''

            return HttpResponseRedirect('../register_success')
    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()
    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')


@login_required(login_url="/SecureWitness/account/login")
def admin_assigned(request):
    return render_to_response('admin_assigned.html')


@login_required(login_url="/SecureWitness/account/login")
def admin_already_assigned(request):
    return render_to_response('admin_already_assigned.html')


@login_required(login_url="/SecureWitness/account/login")
def admin_assign_failed(request):
    return render_to_response('admin_assign_failed.html')


@login_required(login_url="/SecureWitness/account/login")
def user_suspended(request):
    return render_to_response('user_suspended.html')


@login_required(login_url="/SecureWitness/account/login")
def user_not_active(request):
    return render_to_response('user_not_active.html')


@login_required(login_url="/SecureWitness/account/login")
def user_already_suspended(request):
    return render_to_response('user_already_suspended.html')


@login_required(login_url="/SecureWitness/account/login")
def user_suspend_failed(request):
    return render_to_response('user_suspend_failed.html')


@login_required(login_url="/SecureWitness/account/login")
def group_management(request):
    c = {}
    c.update(csrf(request))
    grouplist = Group.objects.all()
    c['groups'] = grouplist
    return render_to_response('group_management.html', c)


@login_required(login_url="/SecureWitness/account/login")
def create_group_failed(request):
    return render_to_response('create_group_failed.html')


def add_user(request, group_id):
    username = request.POST.get('username', '')
    user = User()
    try:
        user = User.objects.get(username=username)
    except:
        return HttpResponseRedirect('../add_user_failed')
    related_groups = user.groups.all()
    group = Group.objects.get(id=group_id)
    if group in related_groups:
        return HttpResponseRedirect('../add_user_failed')
    user.groups.add(group)
    return HttpResponseRedirect('../add_user_succeeded')


# TODO: Pass private files into request
def grant_access_to_files(request):
    # give access to the group
    content_type = ContentType.objects.get_for_model(Group)
    code_name = 'can_access_report_' + request.report_id
    name = 'Can Access Report ' + request.report_id
    permission = Permission.objects.create(condename=code_name, name=name, content_type=content_type)
    group = Group.objects.get(id=request.group_id)
    if group.has_perm('SecureWitness.' + code_name):
        render_to_response('grant_access_to_files_failed.html')
    group.permissions.add(permission)

    # give access to every group member
    users_in_group = group.user_set.all()
    content_type = ContentType.objects.get_for_model(User)
    permission = Permission.objects.create(codename=code_name, name=name, content_type=content_type)
    for user in users_in_group:
        if not user == request.user:
            user.user_permissions.add(permission)
    return render_to_response('grant_access_to_files.html')


# return render_to_response('grant_access_to_files.html', {'files':})


def grant_access_to_files_failed(request):
    return render_to_response('grant_access_to_files.html')


def member_add_user_succeeded(request, group_id):
    return render_to_response('member_add_user_succeeded.html')


def member_add_user_failed(request, group_id):
    return render_to_response('member_add_user_failed.html')


def add_user_succeeded(request, group_id):
    return render_to_response('add_user_succeeded.html')


def add_user_failed(request, group_id):
    return render_to_response('add_user_failed.html')


def admin_remove_failed(request):
    return render_to_response('admin_remove_failed.html')


def admin_removed(request):
    return render_to_response('admin_removed.html')


def not_admin(request):
    return render_to_response('not_admin.html')


def user_activated(request):
    return render_to_response('user_activated.html')


def user_already_activated(request):
    return render_to_response('user_already_activated.html')


def user_activate_failed(request):
    return render_to_response('user_activate_failed.html')


@login_required(login_url="/SecureWitness/account/login")
def edit_group(request, id):
    c = {}
    c.update(csrf(request))
    group = Group.objects.get(id=id)
    users = group.user_set.all()
    folder_list = Folder.objects.filter(GID=id).filter(parent=None)
    report_list = Report.objects.filter(group_id=id).filter(folder_id=None)
    groupname = group.name
    usernames = []
    for u in users:
        usernames.append(u.username)
    allusers = User.objects.all()
    c['group_id'] = id
    c['group_name'] = groupname
    c['users'] = usernames
    c['allusers'] = allusers
    c['folders'] = folder_list
    c['reports'] = report_list

    return render_to_response('edit_group.html', c)


@login_required(login_url="/SecureWitness/account/login")
def edit_folder(request, id):
    c = {}
    c.update(csrf(request))
    folder = Folder.objects.get(folder_id=id)
    children = Folder.objects.filter(parent=id)
    group = Group.objects.get(id=folder.GID.id)
    reports = Report.objects.filter(group_id=folder.GID.id).filter(folder_id=id)

    c['folder_name'] = folder.folder_name
    c['children'] = children
    c['group_name'] = group.name
    c['group_id'] = group.id
    c['reports'] = reports
    if None != folder.parent:
        c['parent_name'] = folder.parent.folder_name
        c['parent_id'] = folder.parent.folder_id

    return render_to_response('edit_folder.html', c)


@login_required(login_url="/SecureWitness/account/login")
def quit_group(request):
    group_id = request.POST.get('group_id', '')
    try:
        group = Group.objects.get(id=group_id)
    except:
        return HttpResponseRedirect('..')
    group = Group.objects.get(id=group_id)
    if not request.user.groups.filter(name=group.name):
        return HttpResponseRedirect('..')
    group.user_set.remove(request.user)
    return render_to_response('quit_group.html', {'group_name': group.name})


@login_required(login_url="/SecureWitness/account/login")
def member_edit_group(request, id):
    c = {}
    c.update(csrf(request))
    group = Group.objects.get(id=id)
    users = group.user_set.all()
    groupname = group.name
    usernames = []
    folder_list = Folder.objects.filter(GID=id).filter(parent=None)
    report_list = Report.objects.filter(group_id=id).filter(folder_id=None)
    for u in users:
        usernames.append(u.username)
    allusers = User.objects.all()
    c['group_id'] = id
    c['group_name'] = groupname
    c['users'] = usernames
    c['allusers'] = allusers
    c['folders'] = folder_list
    c['reports'] = report_list

    return render_to_response('member_edit_group.html', c)


@login_required(login_url="/SecureWitness/account/login")
def create_group(request):
    groupname = request.POST.get('groupname', '')
    # print(groupname)
    try:
        group = Group.objects.get(name=groupname)
    except:
        # f = '%Y%m%d%H%M%S'
        # now = time.localtime()
        # timeString = time.strftime(f, now)
        # timeInt = int(timeString)
        # cur_time = datetime.datetime.now()
        g = Group(name=groupname)  # use datetime of created as id
        g.save()
        return HttpResponseRedirect('../../group_management')

    return HttpResponseRedirect('../create_group_failed')


def register_confirm(request, activation_key):
    # check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/home')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(ActivationProfile, activation_key=activation_key)

    # check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('../confirm_expired.html')
    # if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.user
    user.is_active = True
    user.save()
    return HttpResponseRedirect('../../confirmed')


def confirmed(request):
    return render_to_response('confirmed.html')


def confirm_expired(request):
    return render_to_response('confirm_expired.html')


def duplicate_email(request):
    return render_to_response('duplicate_email.html')


@login_required(login_url="/SecureWitness/account/login")
def change_parent(request, id):
    if request.method == 'POST':
        # TODO Check if parent inputted is correct
        if request.POST.get('parent'):
            folder = Folder.objects.get(folder_id=id)
            group = folder.GID.id
            parent_name = request.POST.get('parent')
            # Make sure it is the correct parent in that group as well
            folder.parent = Folder.objects.filter(folder_name=parent_name).get(GID=group)
            folder.save()

        else:
            # Folder no longer has a parent
            folder = Folder.objects.get(folder_id=id)
            folder.parent = None
            folder.save()

        # finish posting new data and reloading the page
        c = {}
        c.update(csrf(request))
        folder = Folder.objects.get(folder_id=id)
        children = Folder.objects.filter(parent=id)
        group = Group.objects.get(id=folder.GID.id)

        c['folder_name'] = folder.folder_name
        c['children'] = children
        c['group_name'] = group.name
        c['group_id'] = group.id
        if None != folder.parent:
            c['parent_name'] = folder.parent.folder_name
            c['parent_id'] = folder.parent.folder_id

        return render_to_response('edit_folder.html', c)


@login_required(login_url="/SecureWitness/account/login")
def rename_folder(request, id):
    if request.method == 'POST':
        if request.POST.get('new_name'):
            folder = Folder.objects.get(folder_id=id)
            folder.folder_name = request.POST.get('new_name')
            folder.save()

        # Redirect back
        c = {}
        c.update(csrf(request))
        folder = Folder.objects.get(folder_id=id)
        children = Folder.objects.filter(parent=id)
        group = Group.objects.get(id=folder.GID.id)

        c['folder_name'] = folder.folder_name
        c['children'] = children
        c['group_name'] = group.name
        c['group_id'] = group.id
        if None != folder.parent:
            c['parent_name'] = folder.parent.folder_name
            c['parent_id'] = folder.parent.folder_id

        return render_to_response('edit_folder.html', c)


def add_subfolder(request, id):
    if request.method == 'POST':
        cur_folder = Folder.objects.get(folder_id=id)
        try:
            sub_folder = Folder.objects.filter(GID=cur_folder.GID).get(folder_name=request.POST.get('child_name'))
            sub_folder.parent = cur_folder
            sub_folder.save()
        except:
            # Make the new folder
            sub_folder = Folder(folder_name=request.POST.get('child_name'), author_id=request.user, parent=cur_folder,
                                GID=cur_folder.GID)
            sub_folder.save()

        # Redirect back
        c = {}
        c.update(csrf(request))
        folder = Folder.objects.get(folder_id=id)
        children = Folder.objects.filter(parent=id)
        group = Group.objects.get(id=folder.GID.id)

        c['folder_name'] = folder.folder_name
        c['children'] = children
        c['group_name'] = group.name
        c['group_id'] = group.id
        if None != folder.parent:
            c['parent_name'] = folder.parent.folder_name
            c['parent_id'] = folder.parent.folder_id

        return render_to_response('edit_folder.html', c)


def copy_folder(request, id, recursive=False):
    if request.method == 'POST':
        cur_folder = Folder.objects.get(folder_id=id)
        copy = Folder(folder_name=("{0} (copy)".format(cur_folder.folder_name)),
                      author_id=request.user, GID=cur_folder.GID)

        if recursive:
            copy.parent = Folder.objects.filter(GID=cur_folder.GID.id).get(folder_name=(
                cur_folder.parent.folder_name + "( copy)"))
        else:
            copy.parent = cur_folder.parent

        copy.save()

        try:
            copy_children = Folder.objects.filter(parent=id)
            for child in copy_children:
                copy_folder(request, child.folder_id, True)

            # Redirect to new copied folder
            c = {}
            c.update(csrf(request))
            folder = Folder.objects.get(folder_id=copy.folder_id)
            children = Folder.objects.filter(parent=copy.folder_id)
            group = Group.objects.get(id=folder.GID.id)

            c['folder_name'] = folder.folder_name
            c['children'] = children
            c['group_name'] = group.name
            c['group_id'] = group.id
            if None != folder.parent:
                c['parent_name'] = folder.parent.folder_name
                c['parent_id'] = folder.parent.folder_id

            return render_to_response('edit_folder.html', c)
        except:
            # Redirect to new copied folder
            c = {}
            c.update(csrf(request))
            folder = Folder.objects.get(folder_id=copy.folder_id)
            children = Folder.objects.filter(parent=copy.folder_id)
            group = Group.objects.get(id=folder.GID.id)

            c['folder_name'] = folder.folder_name
            c['children'] = children
            c['group_name'] = group.name
            c['group_id'] = group.id
            if None != folder.parent:
                c['parent_name'] = folder.parent.folder_name
                c['parent_id'] = folder.parent.folder_id

            return render_to_response('edit_group.html', c)


@login_required(login_url="/SecureWitness/account/login")
def remove_folder(request, id):
    group = Folder.objects.get(folder_id=id).GID
    if request.method == 'POST':
        cur_folder = Folder.objects.get(folder_id=id)
        # Move children up one level
        try:
            children = Folder.objects.filter(parent=id)
            for child in children:
                child.parent = cur_folder.parent
                child.save()
        except:
            # No children, so skip this step
            pass

        # Delete this folder
        cur_folder.delete()
        # TODO Remove reports and put them at the top level of the group
        pass

    # TODO Redirect to the group management page
    c = {}
    c.update(csrf(request))

    c['group_id'] = group.id
    c['group_name'] = group.name
    c['users'] = UserToGroup.objects.filter(group_id=group.id)
    c['allusers'] = UserToGroup.objects.all()
    c['folders'] = Folder.objects.filter(GID=group.id)
    return render_to_response('edit_folder.html', c)


@login_required(login_url="/SecureWitness/account/login")
def edit_report(request, id):
    c = {}
    c.update(csrf(request))

    report = Report.objects.get(report_id=id)
    if report.folder_id:
        c['folder_name'] = report.folder_id.folder_name
        c['folder_id'] = report.folder_id.folder_id
    if report.group_id:
        c['group_name'] = report.group_id.name
        c['group_id'] = report.group_id.id
    c['report_name'] = report.report_name
    c['author_name'] = report.author_id.username
    c['author_id'] = report.author_id.id
    c['report'] = report

    return render_to_response('edit_report.html', c)


@login_required(login_url="/SecureWitness/account/login")
def report_change_group(request, id):
    if request.method == 'POST':
        # TODO Check if valid group name
        cur_report = Report.objects.get(report_id=id)
        groups = Group.objects.filter(name=request.POST.get('new_group_name'))
        # Change the group and save
        cur_report.group_id = groups[0]
        cur_report.save()

    c = {}
    c.update(csrf(request))

    report = Report.objects.get(report_id=id)
    if report.folder_id:
        c['folder_name'] = report.folder_id.folder_name
        c['folder_id'] = report.folder_id.folder_id
    if report.group_id:
        c['group_name'] = report.group_id.name
        c['group_id'] = report.group_id.id
    c['report_name'] = report.report_name
    c['author_name'] = report.author_id.username
    c['author_id'] = report.author_id.id
    c['report'] = report

    return render_to_response('edit_report.html', c)


def report_change_folder(request, id):
    if request.method == 'POST':
        cur_report = Report.objects.get(report_id=id)
        new_folder = Folder.objects.get(folder_name=request.POST.get('new_folder_name'))
        cur_report.folder_id = new_folder
        cur_report.save()

    c = {}
    c.update(csrf(request))

    report = Report.objects.get(report_id=id)
    if report.folder_id:
        c['folder_name'] = report.folder_id.folder_name
        c['folder_id'] = report.folder_id.folder_id
    if report.group_id:
        c['group_name'] = report.group_id.name
        c['group_id'] = report.group_id.id
    c['report_name'] = report.report_name
    c['author_name'] = report.author_id.username
    c['author_id'] = report.author_id.id
    c['report'] = report

    return render_to_response('edit_report.html', c)


def remove_report(request, id):
    if request.method == 'POST':
        cur_report = Report.objects.get(report_id=id)
        group_id = cur_report.group_id.id
        cur_report.delete()

        c = {}
        c.update(csrf(request))
        group_list = Group.objects.all()
        c['groups'] = group_list
        return HttpResponseRedirect('/SecureWitness/admin/group_management/' + str(group_id), c)


def rename_report(request, id):
    if request.method == 'POST':
        cur_report = Report.objects.get(report_id=id)
        new_name = request.POST.get('new_name')
        cur_report.report_name = new_name
        cur_report.save()

    c = {}
    c.update(csrf(request))

    report = Report.objects.get(report_id=id)
    if report.folder_id:
        c['folder_name'] = report.folder_id.folder_name
        c['folder_id'] = report.folder_id.folder_id
    if report.group_id:
        c['group_name'] = report.group_id.name
        c['group_id'] = report.group_id.id
    c['report_name'] = report.report_name
    c['author_name'] = report.author_id.username
    c['author_id'] = report.author_id.id
    c['report'] = report

    return render_to_response('edit_report.html', c)


def copy_report(request, id):
    if request.method == 'POST':
        cur_report = Report.objects.get(report_id=id)
        new_report = Report(folder_id=cur_report.folder_id,
                            group_id=cur_report.group_id,
                            author_id=request.user,
                            create_date=datetime.now(),
                            last_update_date=datetime.now(),
                            report_name="{0} (copy)".format(cur_report.report_name),
                            short_desc=cur_report.short_desc,
                            long_desc=cur_report.long_desc,
                            location=cur_report.location,
                            incident_date=cur_report.incident_date,
                            keywords=cur_report.keywords,
                            private=cur_report.private)
        new_report.save()

        c = {}
        c.update(csrf(request))

        report = new_report
        if report.folder_id:
            c['folder_name'] = report.folder_id.folder_name
            c['folder_id'] = report.folder_id.folder_id
        if report.group_id:
            c['group_name'] = report.group_id.name
            c['group_id'] = report.group_id.id
        c['report_name'] = report.report_name
        c['author_name'] = report.author_id.username
        c['author_id'] = report.author_id.id
        c['report'] = report

        return HttpResponseRedirect('/SecureWitness/admin/reports/' + str(report.report_id), c)


def map(request):
    reports = Report.objects.raw('SELECT * FROM SecureWitness_report')
    # json_list = serializers.serialize('json', reports)
    return render(request, 'map.html', {'reports': reports})


'''
def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='app/reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('app:login'))


def reset(request):
    return password_reset(request, template_name='reset.html',
        email_template_name='reset_email.html',
        subject_template_name='reset_subject.txt',
        post_reset_redirect=reverse(success))


def success(request):
     return render(request, "success.html")
'''
