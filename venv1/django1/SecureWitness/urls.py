__author__ = 'Yixuan1'
from django.conf.urls import patterns, url

from . import views

urlpatterns = [ url(r'^/account/login/$', views.login),
                        url(r'^/account/auth/$', views.auth_view),
                        url(r'^/account/logout/$', views.logout),
                        url(r'^/account/loggedin/$', views.loggedin),
                        url(r'^/account/invalid/$', views.invalid),
                        url(r'^/account/register/$', views.register_user),
                        url(r'^/account/register_success/$', views.register_success),
                        url(r'^/admin/$', views.admin),
                        url(r'^/admin_assigned/$', views.admin_assigned),
                        url(r'^/admin_already_assigned/$', views.admin_already_assigned),
                        url(r'^/assigning_admin_view/$', views.assigning_admin_view),
                        url(r'^/admin_assign_failed/$', views.admin_assign_failed),
                        url(r'^/user_suspended/$', views.user_suspended),
                        url(r'^/user_already_suspended/$', views.user_already_suspended),
                        url(r'^/suspend_user_view/$', views.suspend_user_view),
                        url(r'^/user_suspend_failed/$', views.user_suspend_failed)




                    ]
'''
                       url(r'^login/$', 'django.contrib.auth.views.login',name="my_login"),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

'''
                    #  url(r'^login/$', 'django.contrib.auth.views.login',
                     #      {'template_name': 'admin/login.html'}),
                     #  url(r'^register/$', views.register, name='register'),