from django.db import models

class productos(models.Model):
  producto_id=models.IntegerField()
  nombre_producto=models.CharField(max_length=50)
  empresa=models.CharField(max_length=50)
  tipo_producto=models.CharField(max_length=50)
  precio=models.FloatField()

  def __str__(self):
    return f"{self.producto_id}"

class proveedores(models.Model):
  proveedor_id=models.IntegerField()
  nombre_proveedor=models.CharField(max_length=50)
  direccion_proveedor=models.CharField(max_length=50)
  cuit=models.IntegerField()

  def __str__(self):
    return f"{self.proveedor_id}"

class ventas(models.Model):
  venta_id=models.IntegerField()
  fecha_venta=models.DateField()
  cantidad_venta=models.IntegerField()
  usuario_id=models.IntegerField()

  def __str__(self):
    return f"{self.venta_id}"
