from django import template 

register = template.Library()

from apps.productos.models import Categoria

@register.simple_tag
def saludar():
	return "Hola a todos esto es un tag personalizado"


@register.simple_tag
def saludar_a_alguien(nombre):
	return f"Hola {nombre}, como estas?"


@register.simple_tag
def get_categorias():
	return Categoria.objects.all()

def agregar_sufijo(valor, argumento):
	return f"{valor}_{argumento}"

register.filter("agregar_sufijo", agregar_sufijo)