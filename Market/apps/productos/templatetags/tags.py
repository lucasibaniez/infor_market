from django import template 

register = template.Library()

from apps.productos.models import Categoria

@register.simple_tag
def saludar():
	return "Hola a todos esto es un tag personalizado"

@register.simple_tag
def get_categorias():
	return Categoria.objects.all()