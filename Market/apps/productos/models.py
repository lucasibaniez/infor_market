from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=255)

	class Meta:
		db_table="categorias"
	def __str__(self):
		return self.nombre

# OneToOne (Investigar)

class Producto(models.Model):
	nombre = models.CharField(max_length=255)
	precio = models.DecimalField(max_digits=9, decimal_places=2)

	# categorias = models.ManyToManyField(Categoria)

	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

	imagen = models.ImageField(upload_to="productos", null=True)

	class Meta:
		db_table="productos"

	def __str__(self):
		return self.nombre
