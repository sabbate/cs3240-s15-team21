# import sys
# import os.path

# sys.path.append(os.path.join(os.path.dirname('views.py'), '..'))
# import gen_py.lib
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from SecureWitness.models import Report
from SecureWitness.models import File
from SecureWitness.models import Group
# from django import forms
# from django import forms
from django.shortcuts import render
import datetime
import time
from SecureWitness.models import *
import Crypto
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os
from .forms import *


class GroupIndexView(generic.ListView):
    template_name = 'SecureWitness/group_index.html'
    context_object_name = 'group_list'

    def get_queryset(self):
        """Return the last five published groups."""
        return Group.objects.order_by('-group_id')[:5]


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
    reports = Report.objects.raw('SELECT * FROM SecureWitness_reports')
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
		cur_time = datetime.now()
		usr = User.objects.filter(=request.user.username)
		r = Report(author_id=request.user, create_date=cur_time, last_update_date=cur_time, short_desc=short, long_desc=long,location=loc, incident_date=date, keywords=keys, private=priv)
		for key, file in request.FILES.items():
			path = os.getcwd() + '\\SecureWitness\\files\\'
			dest = open(path + file.name, 'wb+')
			dest.write(file.read())
			encrypt(path, file.name, password)
			dest.close()
			f = File(author=request.user, report=r, docfile=path)
			f.save();
		r.save();
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
            if (user.is_superuser):
                return HttpResponseRedirect('../../admin')
            else:
                return HttpResponseRedirect('../loggedin')
    else:
        return HttpResponseRedirect('../invalid')


@login_required
def loggedin(request):
    try:
        groups = UserToGroup.objects.filter(UID=request.user.username)
    except:
        groups = None

    try:
        reports = UserToReports.objects.filter(authorID=request.user.username)
    except:
        reports = None
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username, 'groups': groups, 'reports': reports})


@login_required
def admin(request):
    c = {}
    c.update(csrf(request))
    # c['username'] =  request.newAdmin.username
    return render_to_response('admin.html', c)


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


def invalid(request):
    return render_to_response('invalid.html')


@login_required
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
        f.write(ciphertext);
    with open(path + "key_" + filename, 'wb') as f:
        f.write(key);


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../register_success')
    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()
    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')


def admin_assigned(request):
    return render_to_response('admin_assigned.html')


def admin_already_assigned(request):
    return render_to_response('admin_already_assigned.html')


def admin_assign_failed(request):
    return render_to_response('admin_assign_failed.html')


def user_suspended(request):
    return render_to_response('user_suspended.html')


def user_not_active(request):
    return render_to_response('user_not_active.html')


def user_already_suspended(request):
    return render_to_response('user_already_suspended.html')


def user_suspend_failed(request):
    return render_to_response('user_suspend_failed.html')


def group_management(request):
    c = {}
    c.update(csrf(request))
    c['groups'] = Group.objects.values_list('group_name')
    return render_to_response('group_management.html', c)


def create_group_failed(request):
    return render_to_response('create_group_failed.html')


def create_group(request):
    groupname = request.POST.get('groupname', '')

    try:
        group = Group.objects.get(group_name=groupname)
    except:
        f = '%Y%m%d%H%M%S'
        now = time.localtime()
        timeString = time.strftime(f, now)
        timeInt = int(timeString)
        g = Group(group_name=groupname, group_id=timeInt)  # use datetime of created as id
        g.save()
        return HttpResponseRedirect('../../group_management')

    return HttpResponseRedirect('../create_group_failed')


def folder_data(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('../folders/')
    else:
        form = FolderForm()

    return render(request, 'SecureWitness/folder_detail.html', {'form': form})