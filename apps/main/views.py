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
				eve_nom = request.POST['nameEvent'],
				eve_fch = request.POST['dateEvent'],
				eve_inf = request.POST['informationEvent'],
				eve_url_img = request.FILES['imageEvent']
			)
			events.save()

			return HttpResponse(
				json.dumps({"save":True}),
		        content_type = "application/json; charset=utf8"
		    )
		except Exception, e:
			print e
class LoadEvents(View):
	def post(self, request, *args, **kwargs):
		try:
			if request.is_ajax():
				eventos = Eventos.objects.all().values()
				return HttpResponse(
					json.dumps(list(eventos),cls=DjangoJSONEncoder),
					content_type = "application/json; charset=utf8"
				)
			else:
				raise Http404("Eventos No Existe")

		except Exception, e:
			raise e
class InfoEvents( View ):
	def post(self, request, *args, **kwargs):
		try:
			if request.is_ajax():
				
				return HttpResponse(
					json.loads(),
					content_type = "application/json; charset=utf8"
				)
			else: 
				raise Http404("Error en la lectura de información de eventos")	
		except Exception, e:
			raise e
			
"""===> END EVENTS <==="""

"""===> PRODUCT <==== """

def getProduct(request):
	if request.is_ajax():			
		product = Producto.objects.select_related('cat_cod').order_by('prd_cod')
		sendData = product.values('prd_cod','prd_nom','prd_pre','prd_des','prd_nro_piezas','prd_est','cat_cod__cat_nom' , 'cat_cod')
		return HttpResponse(json.dumps(list(sendData)),content_type = "application/json; charset=utf-8")
	else:
		raise Http404

def saveProduct(request):
	if request.is_ajax():

		print request.FILES 
		print request.POST
		if request.POST['edit'] == '1':
			#MODIFY
			print "==============	MODIFICANNNDOOOOO ========"			
			product = Producto.objects.get(prd_cod = request.POST['codeProduct'])
			product.prd_nom 		= request.POST['product']
			product.prd_des 		= request.POST['description']
			product.prd_pre 		= request.POST['price']			
			product.cat_cod_id 		= request.POST['category']
			product.prd_nro_piezas 	= request.POST['pieces']
			if request.POST['withImage'] == "true":
				print "==============	MODIFICANNNDOOOOO  CON IMAGEEEENNN ========"
				product.prd_url 		= request.FILES['imageFile']
			product.save()
			return HttpResponse(json.dumps({"mensaje":"Actualizado con Ëxito"}),content_type= "application/json; charset=utf-8")
		else:			
			#SAVE
			print "===============  ENTREEEE AL GUARDAR  ========="
			if request.POST['withImage'] == "true":
				print "======== CON IMAGEEEENNNN ========="
				product = Producto(				
					prd_nom 		= request.POST['product'],
					prd_des 		= request.POST['description'],
					prd_pre			= request.POST['price'],
					#prd_ofr	= request.POST['oferta'],				
					cat_cod_id		= request.POST['category'],				
					prd_url 		= request.FILES['imageFile'],
					prd_nro_piezas 	= request.POST['pieces'])
				product.save()
			else:
				print "======== SIN IMAGEEEENNNN ========="
				product = Producto(				
					prd_nom 		= request.POST['product'],
					prd_des 		= request.POST['description'],
					prd_pre			= request.POST['price'],
					#prd_ofr	= request.POST['oferta'],				
					cat_cod_id		= request.POST['category'],					
					prd_nro_piezas 	= request.POST['pieces'])
				product.save()
			return HttpResponse(json.dumps({"mensaje":"Guardado con Éxito"}),content_type= "application/json; charset=utf-8")
	else:
		raise Http404
	

def deleteProduct(request):
	if request.is_ajax():
		print "==========ELIMINANDO EL PRODUCTOOOOO================="
		product = Producto.objects.get(prd_cod = request.POST['prd_cod'])
		product.delete()
		return HttpResponse(json.dumps({"mensaje":"Producto Eliminado con Éxito"}),content_type= "application/json : charset=utf-8")
	else:
		raise Http404

def getCategory(request):
	if request.is_ajax():
		category = Categoria.objects.all()
		return HttpResponse(json.dumps(list(category.values())),content_type= "application/json ; charset=utf-8")
	else:
		raise Http404

def saveCategory(request):
	if request.is_ajax():
		category = Categoria(
			cat_nom 	= request.POST['cat_nom'],
			cat_des 	= request.POST['cat_des'],
			cat_est 	= request.POST['cat_est'],
			cat_url 	= request.POST['cat_url'])
		category.save()
		return HttpResponse(json.dumps({"mensaje":"Categoria Guardada con éxito"}),content_type= "application/json : charset=utf-8")
	else:
		raise Http404

def updateCategory(request):
	if request.is_ajax():
		category = Categoria.objects.get(cat_cod = request.POST['cat_cod'])
		category.cat_nom = request.POST['cat_nom']
		category.cat_des = request.POST['cat_des']
		category.cat_est = request.POST['cat_est']
		category.cat_url = request.POST['cat_url']
		category.save()
		return HttpResponse(json.dumps({"mensaje":"Categoria Actualizada con éxito"}),content_type= "application/json : charset=utf-8")
	else:
		raise Http404

def deleteCategory(request):
	if request.is_ajax():
		category = Categoria.objects.get(cat_cod = request.POST['cat_cod'])
		category.cat_est = False
		category.save()
		return HttpResponse(json.dumps({"mensaje":"Categoria Eliminada con Éxito"}), content_type="application/json : charset=utf-8")
	else:
		return Http404

def savePiece(request):
	if request.is_ajax():
		piece = Pieza(
			pie_cod		= request.POST['pie_cod'],
			pie_nom 	= request.POST['pie_nom'],
			prd_cod_id 	= request.POST['prd_cod'],
			pie_num 	= request.POST['pie_num'])
		piece.save()
	else:
		raise Http404
