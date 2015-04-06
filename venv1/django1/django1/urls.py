from django.conf.urls import patterns, include, url
from django.contrib import admin

from SecureWitness import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'django1.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^groups/', include('SecureWitness.urls', namespace="SecureWitness")),
                       url(r'^reports/', include('SecureWitness.urls_reports', namespace="Reports")),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^SecureWitness/', include('SecureWitness.urls')),
                       )
