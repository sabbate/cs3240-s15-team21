from django.conf.urls import patterns, url

from SecureWitness import views

urlpatterns = patterns('',
                       url(r'^$', views.GroupView.as_view(), name='index'),
                       #url(r'^/groups', views.GroupView.as_view(), name='group'),
                       url(r'^(?P<pk>\d+)/$', views.GroupDetail.as_view(), name='group_detail'),
                       )