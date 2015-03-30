# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import TemplateView,View
from .models import *


class Login(View):

	def post(self, request, *args, **kwargs):
		try:	
			user = Usuario.objects.get(usu_ced=request.POST['user'], usu_pass=request.POST['password'])
			user_type = TipoUsuario.objects.get(tip_cod=user.tip_cod_id)
			
			request.session['user']={
				"id"      : user.usu_cod,
				"tip_des" : user_type.tip_des.upper() 
			}
			
			request.session.set_expiry(300)
			return HttpResponseRedirect("/main/logged_user/")
		except Usuario.DoesNotExist:
			return HttpResponseRedirect("/main/")

class LoggedUserHome(View):

	template = "main/logged_user_home.html"
	def get(self, request, *args, **kwargs):
		try:
			if 'user' in request.session:
				user = Usuario.objects.get(usu_cod=request.session['user']['id'])
				user_name = user.usu_nom+" "+user.usu_ape
				return render(request,self.template,{"user_name":user_name})

			else:
				return HttpResponseRedirect("/main/")
		except KeyError:
			return HttpResponseRedirect("/main/")

class LogoutUser(View):
	def get(self, request, *args, **kwargs):
		try:
			#...flush()-->método que elimina todas las sesiones y regenera el session id 
			# en el navegador para evitar la fuga de datos :)
			request.session.flush()
			return HttpResponseRedirect("/main/")
		except Exception, e:
			raise e