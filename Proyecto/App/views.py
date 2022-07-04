from pydoc import describe
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from App.forms import MochilasFormulario, TotebagsFormulario 
from App.models import Mochilas, Totebags


# Create your views here.

def home(self):
    plantila = loader.get_template('App/home.html')
    documento = plantila.render()
    return HttpResponse(documento)

def mochilas(request):
    return render(request, 'app/Mochilas.html')


def totebags(request):
    return render(request, 'App/totebags.html')


def Informacion_sobre_mi(request):
   return render(request, 'App/Informacion_sobre_mi.html')



#def mochilasFormulario(request):
    
 #   if request.method == 'POST':
  #      print(request.POST)
   #     descripcion = request.POST['descripcion']
    #    precio = request.POST['precio']
     #   codigo = request.POST['codigo'] 
      #  mochila = Mochilas ( descripcion=descripcion, precio=precio, codigo=codigo   )
       # mochila.save()
       # return render(request, 'App/home.html')
    #return render(request, 'App/formulario_mochilas.html')


def busquedaCodigoMochilas(request):
    return render(request, 'App/busquedaCodigoMochilas.html')

def buscar(request):
    if request.GET['codigo']:
        codigo = request.GET['codigo']
        mochilas = Mochilas.objects.filter(codigo=codigo)
        return render(request, "App/resultadosBusqueda.html", {'mochilas':mochilas, 'codigo':codigo})
    
    else:
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)

#CRUD Read
def leerMochilas(request):
    mochilas = Mochilas.objects.all()
    contexto= {'mochilas':mochilas}
    return render (request, 'app/leerMochilas.html', contexto)

#CRUD Create

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

        