from django.shortcuts import render

from apps.productos.models import Producto

def inicio(request):
	productos = Producto.objects.all()
	p1 = Producto.objects.get(id=1)
	print("===================")
	print(p1)
	# print(p1.query)
	print("===================")

	usuario = {
		"nombre": "Lucas",
		"apellido": "Ibañez"
	}

	context = {
		"usuario": usuario,
		"productos": productos
	}
	return render(request, "inicio.html", context)