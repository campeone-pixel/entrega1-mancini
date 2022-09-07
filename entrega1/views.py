from django.shortcuts import render



from app_entrega1.models import *


def inicio(request):
  return render(request, 'app_entrega1/inicio.html', )

