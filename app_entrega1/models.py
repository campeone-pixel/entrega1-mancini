from django.db import models

class productos(models.Model):
  producto_id=models.IntegerField()
  nombre_producto=models.CharField(max_length=50)
  empresa=models.CharField(max_length=50)
  tipo_producto=models.CharField(max_length=50)
  precio=models.FloatField()

class proveedores(models.Model):
  proveedor_id=models.IntegerField()
  nombre_proveedor=models.CharField(max_length=50)
  direccion_proveedor=models.CharField(max_length=50)
  cuit=models.IntegerField()

class ventas(models.Model):
  venta_id=models.IntegerField()
  fecha_venta=models.DateField()
  cantidad_venta=models.IntegerField()
  usuario_id=models.IntegerField()
