from django.conf.urls import patterns, include, url
from django.contrib import admin

from SecureWitness import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'django1.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^groups/', views.GroupView.as_view(), name='groups'),
                       url(r'^admin/', include(admin.site.urls)),
                       )

# Added a comment - smm8ec
