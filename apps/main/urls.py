# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from .views import *
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="main/login.html"), name='main_none_none'),#--> login 
    url(r'^login/$', Login.as_view(), name='main_usuario_Login'),#--> metodo de verificación login
    url(r'^logged_user/$', Login.as_view(), name='main_usuario_Login(get)'),#--> carga home user logeado
    # ==> Users <== #
    url(r'^logged_user/create_user/$', Login.as_view(template_name="main/logged_user_users.html"), name='main_usuario_none'),#--> carga Crear Usuario Load Page
    url(r'^logged_user/create_user/load_users/$', LoadDataUsers.as_view(), name='main_usuario_LoadDataUsers'),#--> load user data for de table
    url(r'^logged_user/create_user/add_users/$', SaveDataUsers.as_view(), name='main_usuario_SaveDataUsers'),#--> save user data from table
    url(r'^logged_user/create_user/delete_users/$', DeleteDataUsers.as_view(), name='main_usuario_DeleteDataUsers'),#--> delete user data from table
    #================#
    # ==> Events <== #
    url(r'^logged_user/create_event/$', Login.as_view(template_name="main/logged_user_events.html"), name='main_events_load'),#--> load create events
    url(r'^logged_user/create_event/add_event/$', AddEvent.as_view(), name='main_eventos_AddEvent'),#--> load create events
    #================#
    url(r'^logout/$', LogoutUser.as_view(), name='main_usuario_Logout'),
    #======= Producto ======#
    url(r'^product/$', TemplateView.as_view(template_name="main/producto.html")),
    url(r'^module/getProduct/$','apps.main.views.getProduct'),    
    url(r'^module/saveProduct/$','apps.main.views.saveProduct'),
    url(r'^module/getCategory/$','apps.main.views.getCategory'),
    
    
)