from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
  return render(request, 'App/home.html')

def Historia_comunidad(request):
    return render(request, 'App/Historia_comu.html')

def Actividades_comunidad(request):
    return render(request, 'App/Actividades_comu.html')

def Informacion_sobre_mi(request):
    return render(request, 'App/Informacion_sobre_mi.html')

#def home(self):
 #   plantilla = loader.get_template('home.html')
  #  documento = plantilla.render()
   # return HttpResponse(documento)