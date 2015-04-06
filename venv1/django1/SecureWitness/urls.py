__author__ = 'Yixuan1'
from django.conf.urls import patterns, url

from . import views
from SecureWitness import views

urlpatterns = [ url(r'^/login/$', views.login),
                        url(r'^/auth/$', views.auth_view),
                        url(r'^/logout/$', views.logout),
                        url(r'^/loggedin/$', views.loggedin),
                        url(r'^/invalid/$', views.invalid),
						url(r'^$', views.index, name='index'), 
						url(r'newreport/$', views.newreport, name='newreport'), 
						url(r'^search_form/$', views.search_form), 
						url(r'^search/$', views.search),
						url(r'^submitreport/$', views.submitreport),
                    ]
'''
                       url(r'^login/$', 'django.contrib.auth.views.login',name="my_login"),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

'''
                    #  url(r'^login/$', 'django.contrib.auth.views.login',
                     #      {'template_name': 'admin/login.html'}),
                     #  url(r'^register/$', views.register, name='register'),

