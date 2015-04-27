from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'cs3240-s15-team21.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^groups/', include('SecureWitness.urls', namespace="SecureWitness")),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^SecureWitness/', include('SecureWitness.urls')),
                       )