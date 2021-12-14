from django.contrib.auth.mixins  import LoginRequiredMixin
from django.shortcuts            import render
from django.urls                 import reverse_lazy
from django.views.generic        import ListView, CreateView 
from django.views.generic.detail import DetailView
from django.views.generic.edit   import UpdateView

from apps.core.mixins import AdminRequiredMixins

from .forms  import ProductoForm
from .models import Producto

"""
def detalle(request):
	context = {}
	return render(request, "productos/detalle.html", context)
"""

class ListarAdmin(LoginRequiredMixin, AdminRequiredMixins, ListView):
	template_name="productos/admin/listar.html"
	model = Producto
	context_object_name="productos"
	# permisos_requeridos = ["add_users"]
	paginate_by = 20

	def get_context_data(self, **kwargs):
		context = super(ListarAdmin, self).get_context_data(**kwargs)
		context["nombre_buscado"] = self.request.GET.get("nombre_producto", "")
		return context

	def get_queryset(self):
		busqueda_nombre = self.request.GET.get("nombre_producto", "") # ["nombre_producto"]
		query = Producto.objects.all().order_by("nombre")
		if len(busqueda_nombre) > 0:
			query = query.filter(nombre__icontains=busqueda_nombre)
		return query


class MisProductos(LoginRequiredMixin, AdminRequiredMixins, ListView):
	template_name="productos/admin/listar.html"
	model = Producto
	context_object_name="productos"
	
	def get_queryset(self):
		# self.request
		return Producto.objects.filter(usuario__id=self.request.user.id)# .order_by("id")	

class NuevoAdmin(LoginRequiredMixin, AdminRequiredMixins, CreateView):
	template_name = "productos/admin/nuevo.html"
	model = Producto
	form_class = ProductoForm

	def get_success_url(self, **kwargs):
		return reverse_lazy("productos:admin_listar")

	def form_valid(self, form):
		f = form.save(commit=False)
		f.usuario_id = self.request.user.id
		return super(NuevoAdmin, self).form_valid(form)

class EditarAdmin(UpdateView):
	template_name = "productos/admin/editar.html"
	model = Producto
	form_class = ProductoForm
	context_object_name="producto"

	def get_success_url(self, **kwargs):
		return reverse_lazy("productos:admin_listar") 

class Detalle(DetailView):
	template_name = "productos/detalle.html"
	model = Producto
	
