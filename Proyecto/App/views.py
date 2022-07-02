from pydoc import describe
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from App.forms import MochilasFormulario, TotebagsFormulario 
from App.models import Mochilas


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

def mochilasFormulario(request):
    if request.method == 'POST':
        miFormulario = MochilasFormulario(request.POST)
       
        if miFormulario.is_valid():
         informacion = miFormulario.cleaned_data
        descripcion=informacion['descripcion']
        precio=informacion['precio']
        codigo=informacion['codigo']
      

        mochila = Mochilas (descripcion = descripcion, precio=precio, codigo=codigo)
        mochila.save()
        return render(request, 'app/home.html')
    else:
        miFormulario = MochilasFormulario()
    return render(request, 'app/formulario_mochilas.html',{'miFormulario':miFormulario})


def totebagsFormulario(request):
    if request.method == 'POST':
        miFormulario = TotebagsFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        descripcion=informacion['descripcion']
        precio=informacion['precio']
        totebags = Totebags (descripcion = descripcion, precio=precio)
        totebags.save()
        return render(request, 'app/home.html')
    else:
        miFormulario = TotebagsFormulario()
    return render(request, 'app/formulario_totebags.html',{'miFormulario':miFormulario})

def busquedaCodigoMochilas(request):
        return render(request, 'App/busquedaCodigoMochilas.html')

def buscar(request):
    if request.GET['codigo']:
        codigo = request.GET['codigo']
        mochilass = Mochilas.objects.filter(codigo=codigo)
        return render(request, 'app/resultadosBusqueda.html', {'codigo':codigo})
    else:
        respuesta = "No se ha ingresado ningún código"
    return HttpResponse(respuesta)