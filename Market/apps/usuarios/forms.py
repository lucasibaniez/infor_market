from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import Usuario

class UsuarioForm(UserCreationForm):
	username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese nombre de usuario"}))
	first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese nombre"}))
	last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese su apellido"}))
	
	password = forms.CharField(widget=forms.PasswordInput())
	password1 = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Usuario
		fields = ["username", "first_name", "last_name", "email", "dni"]