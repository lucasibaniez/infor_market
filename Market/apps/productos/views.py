from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts           import render
from django.urls                import reverse_lazy
from django.views.generic       import ListView, CreateView 
from django.views.generic.edit  import UpdateView

from apps.core.mixins import AdminRequiredMixins

from .forms  import ProductoForm
from .models import Producto

def detalle(request):
	context = {}
	return render(request, "productos/detalle.html", context)


class ListarAdmin(LoginRequiredMixin, AdminRequiredMixins, ListView):
	template_name="productos/admin/listar.html"
	model = Producto
	context_object_name="productos"
	# permisos_requeridos = ["add_users"]

	
	def get_queryset(self):
		# self.request
		return Producto.objects.all().order_by("id")
	

class NuevoAdmin(LoginRequiredMixin, AdminRequiredMixins, CreateView):
	template_name = "productos/admin/nuevo.html"
	model = Producto
	form_class = ProductoForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("productos:admin_listar")

class EditarAdmin(UpdateView):
	template_name = "productos/admin/editar.html"
	model = Producto
	form_class = ProductoForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("productos:admin_listar") 

# MRO
	
