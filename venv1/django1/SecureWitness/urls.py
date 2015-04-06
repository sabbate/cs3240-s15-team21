from django.conf.urls import patterns, url

from SecureWitness import views

urlpatterns = patterns('',
                       url(r'^$', views.GroupIndexView.as_view(), name='index'),
                       # url(r'^/groups', views.GroupDetailView.as_view(), name='group'),
                       url(r'^(?P<pk>\d+)/$', views.GroupDetailView.as_view(), name='group'),
                       url(r'^(?P<pk>\d+)/$', views.ReportIndexView.as_view(), name='report_index'),
                       url(r'^login/$', views.login),
                       url(r'^auth/$', views.auth_view),
                       url(r'^logout/$', views.logout),
                       url(r'^loggedin/$', views.loggedin),
                       url(r'^invalid/$', views.invalid),
                       )

'''
                       url(r'^login/$', 'django.contrib.auth.views.login',name="my_login"),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

'''