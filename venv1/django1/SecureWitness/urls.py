from django.conf.urls import patterns, url

from SecureWitness import views

urlpatterns = patterns('',
                       url(r'^$', views.GroupView.as_view(), name='index'),
                       #url(r'^/groups', views.GroupView.as_view(), name='group'),
                       url(r'^/groups/$', views.GroupDetail.as_view(), name='group_detail'),
                       )