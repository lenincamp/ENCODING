from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ENCODING.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^main/', include('apps.main.urls'), name='apps_main_urls'),
)
