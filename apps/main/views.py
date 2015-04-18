# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import TemplateView,View
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import *

class Login(View):
	
	template_name = "main/logged_user_home.html"
	
	def get(self, request, *args, **kwargs):
		try:
			#clear_expired --> elimina sessiones expiradas
			request.session.clear_expired()
			if 'user' in request.session:
				user = Usuario.objects.get(usu_cod=request.session['user']['id'])
				user_name = user.usu_nom.split(" ")[0]+" "+user.usu_ape.split(" ")[0]
				submenus = SubMenu.objects.filter(tip_cod = request.session['user']['tip_cod'])
				menus    = Menu.objects.filter(men_cod__in = submenus.values('men_cod')).order_by('men_des')
				sub_sub  = SubMenu.objects.filter(sbm_sbm__isnull=False).exclude(sbm_sbm=None)
				submenus = submenus.exclude(sbm_des=None)
				data = {
					"user_name":user_name,
					"menus":menus,
					"submenus":submenus.order_by('-sbm_des'), 
					"subs":sub_sub
				}				
					
				if self.template_name == "main/logged_user_users.html":
					user_types = TipoUsuario.objects.all().order_by('tip_des')
					data = {
						"user_name":user_name,
						"menus":menus,
						"submenus":submenus.order_by('-sbm_des'), 
						"subs":sub_sub,
						"user_types":user_types
					}

				return render(request,self.template_name,data)

			else:
				return HttpResponseRedirect("/main/")
		except KeyError:
			return HttpResponseRedirect("/main/")

	def post(self, request, *args, **kwargs):
		try:	
			user = Usuario.objects.get(usu_ced=request.POST['user'], usu_pass=request.POST['password'])		
			request.session['user']={
				"id"      : user.usu_cod,
				"tip_cod" : user.tip_cod_id
			}
			#cicle_key()-->Crea una nueva clave de sesión al tiempo que conserva los datos 
			# de la sesión actual. django.contrib.auth.login () llama a este método para 
			# mitigar la fijación de sesión.
			request.session.cycle_key ()
			request.session.set_expiry(3000)
			return HttpResponseRedirect("/main/logged_user/")
			
		except Usuario.DoesNotExist:
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

"""===> USERS <==="""
class LoadDataUsers(View):
	def post(self, request, *args, **kwargs):
		user = Usuario.objects.select_related('tip_cod').values('usu_cod','usu_ced','usu_nom','usu_ape','usu_tel','usu_dir','tip_cod__tip_des','tip_cod')
		
		return HttpResponse(
			json.dumps(list(user),cls=DjangoJSONEncoder),
	        content_type = "application/json; charset=utf8"
	    )

class SaveDataUsers(View):
	def post(self, request, *args, **kwargs):
		if json.loads(request.GET.get('edit')):
			user = Usuario.objects.get(usu_cod=request.GET.get('cdu'))
			user.usu_nom = request.POST['name']
			user.usu_ape = request.POST['lastname']
			user.usu_tel = request.POST['phone']
			user.usu_dir = request.POST['address']
			user.tip_cod_id = request.POST['typeUser']
			user.usu_ced = request.POST['ci']
			
		else:
			user = Usuario(
				usu_nom = request.POST['name'],
				usu_ape = request.POST['lastname'],
				usu_tel = request.POST['phone'],
				usu_dir = request.POST['address'],
				tip_cod_id = request.POST['typeUser'],
				#usu_pass = generar clave
				usu_ced = request.POST['ci']
			)
		user.save()
		return HttpResponse(
			json.dumps({"save":True},cls=DjangoJSONEncoder),
	        content_type = "application/json; charset=utf8"
	    )

class DeleteDataUsers(View):
	def post(self, request, *args, **kwargs):
		delete = False
		try:
			Usuario.objects.get(usu_cod=request.POST.get('idU')).delete()
			delete = True
		except Usuario.DoesNotExist:
			pass
		finally:
			return HttpResponse(
				json.dumps({"delete":delete}),
		        content_type = "application/json; charset=utf8"
		    )

"""===> END USERS <==="""
"""===> EVENTS <==="""
class AddEvent(View):
	def post(self, request, *args, **kwargs):
		try:
			events = Eventos(
				eve_nom = "probando",
				eve_fch = "2015-02-25",
				eve_inf = "",
				eve_url_img = (request.FILES['file'])
			)
			events.save()

			print request.FILES
			print request.FILES.get('file')
			
			print request.POST.get('file')
			print "************"
		except Exception, e:
			print e
"""===> END USERS <==="""

