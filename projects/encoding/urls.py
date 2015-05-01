from django.conf.urls import patterns, include, url
#from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ENCODING.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^main/', include('apps.main.urls'), name='apps_main_urls'),
)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
