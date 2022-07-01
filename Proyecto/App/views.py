from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from App.forms import Mochilas, Totebags, Informacion_sobre_mi  

# Create your views here.

def home(self):
    plantila = loader.get_template('App/home.html')
    documento = plantila.render()
    return HttpResponse(documento)

def Mochilas(request):
    return render(request, 'app/mochilas.html')


def Totebags(request):
    return render(request, 'App/totebags.html')


def Informacion_sobre_mi(request):
   return render(request, 'App/Informacion_sobre_mi.html')

def formulario_mochilas(request):
    if request.method == 'POST':
        miFormulario = formulario_historia_comunidad(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
         
        precio = informacion['precio']
        descripcion = informacion['descripcion']
        formulario_historia_comunidad = formulario_historia_comunidad( descripcion=descripcion, precio=precio)
        formulario_historia_comunidad.save()
        return render(request, 'app/home.html')
    return render(request, 'app/formulario_mochilas.html')

