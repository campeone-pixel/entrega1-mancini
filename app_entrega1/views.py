from dataclasses import dataclass
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate

from app_entrega1.forms import *
from .models import *

def inicio(request):
  return render(request, 'app_entrega1/inicio.html', )
#------------------------guardar-datos---------------------------------------------------------------------------------------------
def guardar_productos(request):
  if request.method=='POST':
    form=productos_formulario(request.POST)
    if form.is_valid():
      information=form.cleaned_data
      id_pro=information['f_producto_id']
      nombre=information['f_nombre_producto']
      empresa=information['f_empresa']
      tipo=information['f_tipo_producto']
      precio=information['f_precio']
      guardar=productos(producto_id=id_pro, nombre_producto=nombre, empresa=empresa,tipo_producto=tipo,precio=precio )
      guardar.save()
      formulario=productos_formulario()
      all_productos = productos.objects.all()
      return render(request, 'app_entrega1/productos.html', {'formulario':formulario, 'all_productos':all_productos })
  else:
    formulario=productos_formulario()
    all_productos = productos.objects.all()
    return render(request, 'app_entrega1/productos.html', {'formulario':formulario,
    'all_productos':all_productos})

def guardar_proveedores(request):
  if request.method=='POST':
    form=proveedores_formularios(request.POST)
    if form.is_valid():
      information=form.cleaned_data
      proveedor_id=information['f_proveedor_id']
      nombre=information['f_nombre_proveedor']
      direccion=information['f_direccion_proveedor']
      cuit=information['f_cuit']
      guardar=proveedores(proveedor_id=proveedor_id, nombre_proveedor=nombre, direccion_proveedor=direccion,cuit=cuit)
      guardar.save()
      formulario=proveedores_formularios()
      all_proveedores = proveedores.objects.all()
      return render(request, 'app_entrega1/proveedores.html', {'formulario':formulario, 'all_proveedores':all_proveedores })
  else:
    formulario=proveedores_formularios()
    all_proveedores = proveedores.objects.all()
    return render(request, 'app_entrega1/proveedores.html', {'formulario':formulario,
    'all_proveedores':all_proveedores})

def guardar_ventas(request):
  if request.method=='POST':
    form=ventas_formularios(request.POST)
    if form.is_valid():
      information=form.cleaned_data
      venta_id=information['f_venta_id']
      fecha_venta=information['f_fecha_venta']
      cantidad_venta=information['f_cantidad_venta']
      usuario_id=information['f_usuario_id']
      
      guardar=ventas(venta_id=venta_id,fecha_venta=fecha_venta,cantidad_venta=cantidad_venta,usuario_id=usuario_id)
      guardar.save()
      formulario=ventas_formularios()
      all_ventas = ventas.objects.all()
      return render(request, 'app_entrega1/ventas.html', {'formulario':formulario, 'all_ventas':all_ventas })
  else:
    formulario=ventas_formularios()
    all_ventas = ventas.objects.all()
    return render(request, 'app_entrega1/ventas.html', {'formulario':formulario, 'all_ventas':all_ventas })


#---------------------buscador------------------------------------------------------------------------------------------------
def buscar_productos(request):
  if request.method=='POST':
    producto=request.POST['producto_id']
    
    busqueda=productos.objects.filter(producto_id=producto)
    
    return render(request, 'app_entrega1/buscar_productos.html', {'all_productos':busqueda })
  else:
    all_productos = productos.objects.all()
    return render(request, 'app_entrega1/buscar_productos.html', {'all_productos':all_productos})

  
def buscar_proveedores(request):
  

  if request.method=='POST':
    provedor=request.POST['proveedor_id']
    
    busqueda=proveedores.objects.filter(proveedor_id=provedor)
    return render(request, 'app_entrega1/buscar_proveedores.html', {'all_proveedores':busqueda })
  else:
    all_proveedores = proveedores.objects.all()
    return render(request, 'app_entrega1/buscar_proveedores.html', {'all_proveedores':all_proveedores})

  
def buscar_ventas(request):
  if request.method=='POST':
    venta=request.POST['venta_id']
    
    busqueda=ventas.objects.filter(venta_id=venta)
    return render(request, 'app_entrega1/buscar_ventas.html', {'all_ventas':busqueda })
  else:
    all_ventas = ventas.objects.all()
    return render(request, 'app_entrega1/buscar_ventas.html', {'all_ventas':all_ventas})

#-----------------------------------------------------------------------------------


def eliminar_proveedor(request,proveedor_id):
  proveedor_a_borrar=proveedores.objects.get(proveedor_id=proveedor_id)
  proveedor_a_borrar.delete()
  all_proveedores = proveedores.objects.all()
  return render(request, 'app_entrega1/buscar_proveedores.html', {'all_proveedores':all_proveedores})

def eliminar_producto(request,producto_id):
  producto_a_borrar=productos.objects.get(producto_id=producto_id)
  producto_a_borrar.delete()
  all_productos = productos.objects.all()
  return render(request, 'app_entrega1/buscar_productos.html', {'all_productos':all_productos})

def eliminar_venta(request,venta_id):
  venta_a_borrar=proveedores.objects.get(venta_id=venta_id)
  venta_a_borrar.delete()
  all_ventas = ventas.objects.all()
  return render(request, 'app_entrega1/buscar_venta.html', {'all_ventas':all_ventas})

#------------------------------------------------------------------------------------------

def actualizar_proveedor(request,proveedor_id):
  proveedor=proveedores.objects.get(proveedor_id=proveedor_id)
  if request.method=='POST':
    formulario = proveedores_formularios(request.POST)
    if formulario.is_valid():
      producto_actualizado = formulario.cleaned_data
      proveedor.proveedor_id = producto_actualizado['f_proveedor_id']
      proveedor.nombre_proveedor = producto_actualizado['f_nombre_proveedor']
      proveedor.direccion_proveedor = producto_actualizado['f_direccion_proveedor']
      proveedor.cuit = producto_actualizado['f_cuit']
      proveedor.save()
      return render(request,'app_entrega1/buscar_proveedores.html')
  else:
    miformulario=proveedores_formularios(initial={'f_proveedor_id':proveedor.proveedor_id,'f_nombre_proveedor':proveedor.nombre_proveedor,'f_direccion_proveedor':proveedor.direccion_proveedor,'f_cuit':proveedor.cuit})
    return render( request, 'app_entrega1/actualizar_proveedor.html',{'miformulario':miformulario,'proveedor':proveedor})

def actualizar_venta(request,venta_id):
  venta=ventas.objects.get(venta_id=venta_id)
  if request.method=='POST':
    formulario = ventas_formularios(request.POST)
    if formulario.is_valid():
      producto_actualizado = formulario.cleaned_data
      venta.venta_id = producto_actualizado['f_venta_id']
      venta.fecha_venta = producto_actualizado['f_fecha_venta']
      venta.cantidad_venta = producto_actualizado['f_cantidad_venta']
      venta.usuario_id = producto_actualizado['f_usuario_id']
      venta.save()
      return render(request,'app_entrega1/buscar_ventas.html')
  else:
    miformulario=ventas_formularios(initial={'f_venta_id':venta.venta_id,'f_fecha_venta':venta.fecha_venta,'f_cantidad_venta':venta.cantidad_venta,'f_usuario_id':venta.usuario_id})
    return render( request, 'app_entrega1/actualizar_venta.html',{'miformulario':miformulario,'venta':venta})

def actualizar_producto(request,producto_id):
  producto=productos.objects.get(producto_id=producto_id)
  if request.method=='POST':
    formulario = productos_formulario(request.POST)
    if formulario.is_valid():
      producto_actualizado = formulario.cleaned_data
      producto.producto_id = producto_actualizado['f_producto_id']
      producto.nombre_producto = producto_actualizado['f_nombre_producto']
      producto.empresa = producto_actualizado['f_empresa']
      producto.tipo_producto = producto_actualizado['f_tipo_producto']
      producto.precio = producto_actualizado['f_precio']
      producto.save()
      return render(request,'app_entrega1/buscar_ventas.html')
  else:
    miformulario=productos_formulario(initial={'f_producto_id':producto.producto_id,'f_nombre_producto':producto.nombre_producto,'f_empresa':producto.empresa,'f_tipo_producto':producto.tipo_producto,'f_precio':producto.precio})
    return render( request, 'app_entrega1/actualizar_producto.html',{'miformulario':miformulario,'producto':producto})



def login_request(request):
  if request.method =="POST":
    form=AuthenticationForm(request,data = request.POST)

    if form.is_valid():
      usuario = form.cleaned_data.get("username")
      contra = form.cleaned_data.get("password")

      user= authenticate(username=usuario, password=contra)

      if user is not None:
        login(request,user)
        return render(request, "app_entrega1/inicio.html", {"mensaje":f"Bienvenido {usuario}"})

      else:
        return render(request, "app_entrega1/inicio.html", {"mensaje":"Error, datos incorrectos"})

  else:
        return render(request, "app_entrega1/inicio.html", {"mensaje":"Error, Formulario erroneo"})

  form = AuthenticationForm()

  return render(request, "app_entrega1/login.html", {"form":form})

def register(request):
  if request.method =="POST":
    form = UserRegisterForm(request.POST)

    if form.is_valid():
      username = form.cleaned_data.get["username"]
      form.save()
      return render(request, "app_entrega1/inicio.html", {"mensaje":"{username} Usuario creado"})

  else:
    form=UserRegisterForm()

  return render(request, "app_entrega1/registro.html", {"form":form})

  


























































