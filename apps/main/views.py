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
			#cicle_key()-->Crea una nueva clave de sesión al tiempo que conserva los datos 
			# de la sesión actual. django.contrib.auth.login () llama a este método para 
			# mitigar la fijación de sesión.
			request.session.cycle_key ()
			request.session.set_expiry(300)
			return HttpResponseRedirect("/main/logged_user/")
		except Usuario.DoesNotExist:
			return HttpResponseRedirect("/main/")

class LoggedUserHome(View):

	template = "main/logged_user_home.html"
	def get(self, request, *args, **kwargs):
		try:
			#clear_expired --> elimina sessiones expiradas
			request.session.clear_expired ()
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
			request.session.clear_expired ()
			if 'user' in request.session:
				#...flush()-->método que elimina todas las sesiones y regenera el session id 
				# en el navegador para evitar la fuga de datos :)
				request.session.flush()
				return HttpResponseRedirect("/main/")
		except KeyError:
			return HttpResponseRedirect("/main/")