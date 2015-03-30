from django.conf.urls import patterns, include, url
from .views import *
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="main/home.html"), name='main_none_none'),
    url(r'^login/$', login.as_view(), name='main_usuario_login'),
    #url(r'^$', TemplateView.as_view(template_name="main/logged_user.html"), name='main_none_none'),
)