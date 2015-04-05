__author__ = 'Yixuan1'
from django.conf.urls import patterns, url

from . import views

urlpatterns = [ url(r'^/login/$', views.login),
                        url(r'^/auth/$', views.auth_view),
                        url(r'^/logout/$', views.logout),
                        url(r'^/loggedin/$', views.loggedin),
                        url(r'^/invalid/$', views.invalid),
                    ]
'''
                       url(r'^login/$', 'django.contrib.auth.views.login',name="my_login"),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

'''
                    #  url(r'^login/$', 'django.contrib.auth.views.login',
                     #      {'template_name': 'admin/login.html'}),
                     #  url(r'^register/$', views.register, name='register'),