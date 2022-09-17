from django.shortcuts import render



from app_entrega1.models import *


def index(request):
  return render(request, 'app_entrega1/index.html', )

