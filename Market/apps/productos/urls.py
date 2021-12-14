from django.urls import path 

from . import views

app_name = "productos"

urlpatterns = [
	path("Detalle/<int:pk>/", views.Detalle.as_view(), name="detalle"),

	# Admin
	path("Admin/Listar/", views.ListarAdmin.as_view(), name="admin_listar"),
	path("Admin/Nuevo/", views.NuevoAdmin.as_view(), name="admin_nuevo"),
	path("Admin/Editar/<int:pk>/", views.EditarAdmin.as_view(), name="admin_editar"),

	path("MisProductos/", views.MisProductos.as_view(), name="mis_productos")

]