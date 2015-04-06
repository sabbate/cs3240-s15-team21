from django.conf.urls import patterns, url
from SecureWitness import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'), 
url(r'newreport/$', views.newreport, name='newreport'), 
url(r'^search_form/$', views.search_form), 
url(r'^search/$', views.search),
url(r'^submitreport/$', views.submitreport) )
