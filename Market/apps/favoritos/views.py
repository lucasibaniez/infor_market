from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.productos.models import Producto

@login_required
def mis_favoritos(request):
	template_name = "favoritos/mis_favoritos.html"
	context = {"favorito": request.user.get_lista()}
	return render(request, template_name, context)


@login_required
def add_favorito(request, producto_id):
	lista = request.user.get_lista()
	# FALTA: Si el producto ya existe, que no se agregue
	lista.productos.add(Producto.objects.get(id=producto_id))
	return redirect("favoritos:mis_favoritos")

