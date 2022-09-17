from django.contrib import admin
from django.urls import path
from app_entrega1.views import *

urlpatterns = [
   
   path("bd/",bd,name="bd"),
   path("productos/",guardar_productos, name='guardar_productos'),
   path("proveedores/",guardar_proveedores, name='guardar_proveedores'),
   path("ventas/",guardar_ventas, name='guardar_ventas'),

   path("buscar_productos/",buscar_productos, name='buscar_productos'),
   path("buscar_proveedores/",buscar_proveedores, name='buscar_proveedores'),
   path("buscar_ventas/",buscar_ventas, name='buscar_ventas'),

   path("eliminar_venta/<venta_id>",eliminar_venta, name='eliminar_venta'),
   path("eliminar_proveedor/<proveedor_id>",eliminar_proveedor, name='eliminar_proveedor'),
   path("eliminar_producto/<producto_id>",eliminar_producto, name='eliminar_producto'),

   path("actualizar_proveedor/<proveedor_id>",actualizar_proveedor, name='actualizar_proveedor'),
   path("actualizar_producto/<producto_id>",actualizar_producto, name='actualizar_producto'),
   path("actualizar_venta/<venta_id>",actualizar_venta, name='actualizar_venta'),

   path("login_request/", login_request, name="login_request")
  
   

  
   
]