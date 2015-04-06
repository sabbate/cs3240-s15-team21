from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponse #, HttpResposeDirect
from SecureWitness.models import Reports
from django import forms
from django.shortcuts import render
import datetime

def index(request):
	return HttpResponse("Welcome to SecureWitness!")
		
def newreport(request):
	return render(request, 'newreport.html')

def submitreport(request):
	if request.POST['short'] and request.POST['long']:
		short = request.POST['short']
		long = request.POST['long']
		loc = request.POST['location']
		date = request.POST['date']
		keys = request.POST['keys']
		priv = request.POST['private']
		#files = HttpRequest.FILES;
		cur_time = datetime.datetime.now()
		r = Reports(create_date = cur_time, last_update_date = cur_time, short_desc = short, long_desc = long, 
		location = loc, incident_date = date, keywords = keys, private = priv)
		r.save();
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
		
# Create your views here.

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
        return HttpResponseRedirect('../loggedin')
    else:
        return HttpResponseRedirect('../invalid')

def loggedin(request):
    return render_to_response('loggedin.html',
        {'full_name': request.user.username})

def invalid(request):
    return render_to_response('invalid.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
