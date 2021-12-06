from django.urls import path 

from . import views

app_name = "productos"

urlpatterns = [
	path("Detalle/", views.detalle, name="detalle"),
	path("Admin/Listar/", views.ListarAdmin.as_view(), name="admin_listar")


]