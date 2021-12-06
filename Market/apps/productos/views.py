from django.shortcuts import render

def detalle(request):
	context = {}
	return render(request, "productos/detalle.html", context)
