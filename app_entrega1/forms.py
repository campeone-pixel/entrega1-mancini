from dataclasses import fields
from turtle import width
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class productos_formulario(forms.Form):
  f_producto_id=forms.IntegerField()
  f_nombre_producto=forms.CharField(max_length=50)
  f_empresa=forms.CharField(max_length=50)
  f_tipo_producto=forms.CharField(max_length=50)
  f_precio=forms.FloatField()

class proveedores_formularios(forms.Form):
  f_proveedor_id=forms.IntegerField()
  f_nombre_proveedor=forms.CharField(max_length=50)
  f_direccion_proveedor=forms.CharField(max_length=50)
  f_cuit=forms.IntegerField()

class ventas_formularios(forms.Form):
  f_venta_id=forms.IntegerField()
  f_fecha_venta=forms.DateField()
  f_cantidad_venta=forms.IntegerField()
  f_usuario_id=forms.IntegerField()

class UserRegisterForm(UserCreationForm):
  email=forms.EmailField()
  password1= forms.CharField(label="contraseña", widget=forms.PasswordInput)
  password2= forms.CharField(label="repetir contraseña", widget=forms.PasswordInput)

  class Meta:
    model = User
    fields=["username","email","password1","password2"]
    help_texts={k:"" for k in fields}