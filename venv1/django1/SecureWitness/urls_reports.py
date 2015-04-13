from django.conf.urls import patterns, url

from SecureWitness import views

urlpatterns = patterns('',
                       url(r'^$', views.ReportIndexView.as_view(), name='report_index'),
                       )