from django import forms

from . models import Producto

class ProductoForm(forms.ModelForm):
	nombre = forms.CharField(label="Nombre del Producto", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese nombre del producto"}))
	# attrs={'cols': 80, 'rows': 20}
	descripcion = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

	class Meta:
		model = Producto
		fields = ["nombre", "precio", "imagen", "categoria", "descripcion"]