from django import forms

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