from django.conf.urls import patterns, url

from SecureWitness import views

urlpatterns = patterns('',
                       url(r'^$', views.GroupIndexView.as_view(), name='index'),
                       # url(r'^/groups', views.GroupDetailView.as_view(), name='group'),
                       url(r'^(?P<pk>\d+)/$', views.GroupDetailView.as_view(), name='group'),
                       url(r'^(?P<pk>\d+)/$', views.ReportIndexView.as_view(), name='report_index'),
                       )