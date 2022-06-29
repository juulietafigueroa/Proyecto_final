from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(self):
    plantila = loader.get_template('App/home.html')
    documento = plantila.render()
    return HttpResponse(documento)

def Historia_comunidad(request):
    return render(request, 'app/Historia_comu.html')

#def Historia_comunidad(self):
 #   documento = f"Página para historia de la comunidad"
  #  return HttpResponse(documento)

#def Actividades_comunidad(request):
 #   return render(request, 'App/Actividades_comu.html')

def Actividades_comunidad(self):
    documento = f"Página para actividades de la comunidad"
    return HttpResponse(documento)

#def Informacion_sobre_mi(request):
 #  return render(request, 'App/Informacion_sobre_mi.html')

def Informacion_sobre_mi(self):
    documento = f"Página para Informacion_sobre_mi"
    return HttpResponse(documento)
