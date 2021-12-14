from django.db import models

from django.contrib.auth.models import AbstractUser



class Usuario(AbstractUser):
	dni = models.IntegerField(null=True, blank=True)
	es_administrador = models.BooleanField(default=False)

	class Meta:
		db_table="usuarios"

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

	def get_lista(self):
		from apps.favoritos.models import Lista
		favorito = Lista.objects.filter(usuario=self).first()

		if favorito is None:
			favorito = Lista.objects.create(usuario=request.user)

		return favorito

