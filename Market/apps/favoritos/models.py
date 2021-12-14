from django.db import models

from apps.usuarios.models import Usuario
from apps.productos.models import Producto

class Lista(models.Model):
	usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, null=True)
	productos = models.ManyToManyField(Producto)

	class Meta:
		db_table="lista_favoritos"