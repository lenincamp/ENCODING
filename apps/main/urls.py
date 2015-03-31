from django.conf.urls import patterns, include, url
from .views import *
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="main/login.html"), name='main_none_none'),
    url(r'^login/$', Login.as_view(), name='main_usuario_Login'),
    url(r'^logged_user/$', Login.as_view(), name='main_usuario_Login(get)'),
    url(r'^logout/$', LogoutUser.as_view(), name='main_usuario_Logout'),
)