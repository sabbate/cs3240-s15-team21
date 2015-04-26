from django.conf.urls import patterns, url, include
# from django.contrib import admin
# admin.autodiscover()
import django
from . import views

urlpatterns = [
    #url(r'^$', views.GroupIndexView.as_view(), name='index'),
    url(r'^groups', views.GroupDetailView.as_view(), name='group'),
    url(r'^(?P<pk>\d+)/$', views.GroupDetailView.as_view(), name='group'),
    url(r'^(?P<pk>\d+)/$', views.ReportIndexView.as_view(), name='report_index'),
    url(r'newreport/$', views.newreport, name='newreport'),
    url(r'^search_form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^submitreport/$', views.submitreport),
    url(r'^account/login/$', views.login),
    url(r'^account/auth/$', views.auth_view),
    url(r'^account/logout/$', views.logout),
    url(r'^account/loggedin/$', views.loggedin),
    url(r'^account/user_not_active/$', views.user_not_active),
    url(r'^account/invalid/$', views.invalid),
    url(r'^account/register/$', views.register_user),
    url(r'^account/register_success/$', views.register_success),
    url(r'^admin/$', views.admin),
    url(r'^admin_assigned/$', views.admin_assigned),
    url(r'^admin_already_assigned/$', views.admin_already_assigned),
    url(r'^assigning_admin_view/$', views.assigning_admin_view),
    url(r'^admin_assign_failed/$', views.admin_assign_failed),
    url(r'^user_suspended/$', views.user_suspended),
    url(r'^user_already_suspended/$', views.user_already_suspended),
    url(r'^suspend_user_view/$', views.suspend_user_view),
    url(r'^user_suspend_failed/$', views.user_suspend_failed),
    url(r'^admin/group_management/$', views.group_management),
    url(r'^admin/group_management/create_group/$', views.create_group),
    url(r'^admin/group_management/create_group_failed/$', views.create_group_failed),
    url(r'^activate_user_view/$', views.activate_user_view),
    url(r'^user_activate_failed/$', views.user_activate_failed),
    url(r'^user_activated/$', views.user_activated),
    url(r'^user_already_activated/$', views.user_already_activated),
    url(r'^admin_remove_failed/$', views.admin_remove_failed),
    url(r'^admin_removed/$', views.admin_removed),
    url(r'^not_admin/$', views.not_admin),
    url(r'^removing_admin_view/$', views.removing_admin_view),
    url(r'^register_confirm/$', views.removing_admin_view),
    url(r'^removing_admin_view/$', views.removing_admin_view),
    url(r'^account/confirmed/$', views.confirmed),
    url(r'^account/confirm_expired/$', views.confirm_expired),
    url(r'^account/confirm/(?P<activation_key>\w+)/', views.register_confirm),
    url(r'^account/register/duplicate_email/', views.duplicate_email),
    url(r'^account/resetpassword/', django.contrib.auth.views.password_reset, {'template_name': 'myregistration/password_reset_form.html'}),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            django.contrib.auth.views.password_reset_confirm, {'template_name': 'myregistration/password_reset_confirm.html'}),
    url(r'^resetpassword/passwordsent/$', django.contrib.auth.views.password_reset_done, {'template_name': 'myregistration/password_reset_done.html'}),
    url(r'^password_reset/done/$', django.contrib.auth.views.password_reset_complete, {'template_name': 'myregistration/password_reset_complete.html'}),
    url(r'', include('django.contrib.auth.urls')),
	url(r'^$', views.index, name='index'),
    #url(r'', include('myregistration.backends.default.urls'))
	url(r'map/$', views.map),








]


# url(r'^login/$', 'django.contrib.auth.views.login',
# {'template_name': 'admin/login.html'}),
# url(r'^register/$', views.register, name='register'),
'''
url(r'^newfolder/', views.new_folder),
url(r'^addfolder/', views.add_folder),
'''
