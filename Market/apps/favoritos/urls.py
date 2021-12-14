from django.urls import path 

from . import views

app_name = "favoritos"

urlpatterns = [
	path("MisFavoritos/", views.mis_favoritos, name="mis_favoritos"),
	path("Agregar/<int:producto_id>/", views.add_favorito, name="add_favorito")

]