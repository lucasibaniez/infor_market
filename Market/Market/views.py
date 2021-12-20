from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic        import ListView

from apps.core.decorators  import admin_required
from apps.productos.models import Producto

	
"""
# Inicio basado en funcion
# @admin_required()
def inicio(request):
	context = {
		"productos": Producto.objects.all()
	}
	return render(request, "inicio.html", context)

class Inicio(TemplateView):
	template_name = "inicio.html"

	
	def get_context_data(self, **kwargs):
		context = super(Inicio, self).get_context_data(**kwargs)
		context["productos"] = Producto.objects.all()
		return context
"""

class Inicio(ListView):
	template_name="inicio.html"
	model = Producto
	context_object_name="productos"
	
	def get_context_data(self, **kwargs):
		context = super(Inicio, self).get_context_data(**kwargs)
		context["nombre_parametro"] = None
		return context

	def get_queryset(self):
		return Producto.objects.filter(estado__in=[1,3])