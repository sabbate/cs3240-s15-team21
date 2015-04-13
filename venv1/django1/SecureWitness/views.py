from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
=======
from SecureWitness.models import Reports
from SecureWitness.models import Files
from django import forms
from django.shortcuts import render
import datetime
>>>>>>> 705e127d3c7140da426a4a91d1cbae3f3ff5f203

from SecureWitness.models import *


class GroupIndexView(generic.ListView):
    template_name = 'SecureWitness/group_index.html'
    context_object_name = 'group_list'

    def get_queryset(self):
        """Return the last five published groups."""
        return Group.objects.order_by('-GID')[:5]


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
	reports = Reports.objects.raw('SELECT * FROM SecureWitness_reports')
	return render(request, 'all-reports.html', {'reports': reports})
	#return HttpResponse("Welcome to SecureWitness!")
		
def newreport(request):
	return render(request, 'newreport.html')

def submitreport(request):
	if request.POST['short'] and request.POST['long']:
		short = request.POST['short']
		long = request.POST['long']
		loc = request.POST['location']
		date = request.POST['date']
		keys = request.POST['keys']
		priv = request.POST.get('private', False)
		#files = HttpRequest.FILES;
		cur_time = datetime.datetime.now()
		r = Report(create_date = cur_time, last_update_date = cur_time, short_desc = short, long_desc = long, 
		location = loc, incident_date = date, keywords = keys, private = priv)
		r.save();
		for key, file in request.FILES.items():
			path = 'C:/Users/Sarah M/gitrepos/cs3240-s15-team21/venv1/django1/SecureWitness/files/' + file.name
			dest = open(path, 'wb+')
			dest.write(file.read())
			dest.close()
			f = File(authorID = 1, ReportID = 1, docfile = path);
			f.save();

		return HttpResponse('Thank you for submitting a report!')
	else:
		return HttpResponse('Your submission was unsuccessful.')
	
def search_form(request):
	return render(request, 'search_form.html')

def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		reports = Reports.objects.filter(keywords__icontains=q)
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
        if(user.is_superuser):
            return HttpResponseRedirect('../../admin')
        else:
            return HttpResponseRedirect('../loggedin')
    else:
        return HttpResponseRedirect('../invalid')

<<<<<<< HEAD
@login_required
=======

>>>>>>> 705e127d3c7140da426a4a91d1cbae3f3ff5f203
def loggedin(request):
    return render_to_response('loggedin.html',
        {'full_name': request.user.username})

<<<<<<< HEAD
@login_required
def admin(request):
    c = {}
    c.update(csrf(request))
    #c['username'] =  request.newAdmin.username
    return render_to_response('admin.html',
        c)

def suspend_user_view(request):
    username = request.POST.get('username_suspend', '')
    try:
        suspend = User.objects.get(username=username)
    except:
        return HttpResponseRedirect('../user_suspend_failed')

    if suspend.is_active:
        suspend.is_active = False
        suspend.save()
        if not suspend.is_active :
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


=======
>>>>>>> 705e127d3c7140da426a4a91d1cbae3f3ff5f203

def invalid(request):
    return render_to_response('invalid.html')

<<<<<<< HEAD
@login_required
=======

>>>>>>> 705e127d3c7140da426a4a91d1cbae3f3ff5f203
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

<<<<<<< HEAD
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

def user_already_suspended(request):
    return render_to_response('user_already_suspended.html')

def user_suspend_failed(request):
    return render_to_response('user_suspend_failed.html')
=======

>>>>>>> 705e127d3c7140da426a4a91d1cbae3f3ff5f203
