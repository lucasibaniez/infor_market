from django.shortcuts import render

from apps.productos.models import Producto

def inicio(request):
	context = {
		"productos": Producto.objects.all()
	}
	return render(request, "inicio.html", context)