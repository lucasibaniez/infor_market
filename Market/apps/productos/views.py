from django.shortcuts     import render
from django.views.generic import ListView

from .models import Producto

def detalle(request):
	context = {}
	return render(request, "productos/detalle.html", context)


class ListarAdmin(ListView):
	template_name="productos/admin/listar.html"
	model = Producto
	context_object_name="productos"
