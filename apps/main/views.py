from django.shortcuts import render, HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import TemplateView,View
from .models import *

# return render(request,"main/home.html",{})
class login(View):
	def post(self, request, *args, **kwargs):
		try:
			
			user = Usuario.objects.get(usu_ced=request.POST['user'], usu_pass=request.POST['password'])
			user_type = TipoUsuario.objects.get(tip_cod=user.tip_cod)
			request.session['user']={
				"id"      : user.usu_cod,
				"tip_des" : user_type.tip_des.upper() 
			}
			request.session.set_expiry(300)
			
			return HttpResponseRedirect("/main/logged_user/")
		except Usuario.DoesNotExist:
			return HttpResponseRedirect("/main/")
	

	