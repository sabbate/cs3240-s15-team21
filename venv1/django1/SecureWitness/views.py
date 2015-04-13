from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
        if(user.is_superuser):
            return HttpResponseRedirect('../../admin')
        else:
            return HttpResponseRedirect('../loggedin')
    else:
        return HttpResponseRedirect('../invalid')

@login_required
def loggedin(request):
    return render_to_response('loggedin.html',
        {'full_name': request.user.username})

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



def invalid(request):
    return render_to_response('invalid.html')

@login_required
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

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
