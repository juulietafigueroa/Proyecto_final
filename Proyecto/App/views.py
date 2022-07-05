from contextlib import ContextDecorator
from dataclasses import field
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from pydoc import describe
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from App.forms import MochilasFormulario, TotebagsFormulario 
from App.models import Mochilas, Totebags
from django.urls import reverse_lazy

# Create your views here.

def home(self):
    plantila = loader.get_template('App/home.html')
    documento = plantila.render()
    return HttpResponse(documento)

def mochilas2(request):
    mochilas = Mochilas.objects.all()
    contexto= {'mochilas':mochilas}
    return render (request, 'app/Mochilas2.html', contexto)

   

   


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

#CRUD Delete
def eliminarMochila(request, codigo):
    mochila = Mochilas.objects.get(codigo=codigo)
    mochila.delete()

    mochilas = Mochilas.objects.all()
    contexto= {'mochilas':mochilas}
    return render (request, 'app/Mochilas2.html', contexto)


def editarMochila(request, precio):
    mochila=Mochilas.objects.get(precio=precio)

    if request.method == 'POST':

            miFormulario = MochilasFormulario(request.POST)
            if miFormulario.is_valid():
                informacion=miFormulario.cleaned_data
                mochila.codigo=informacion['codigo']
                mochila.descripcion=informacion['descripcion']
                mochila.precio=informacion['precio']
                mochila.save()

                mochilas=Mochilas.objects.all()
                contexto={'mochilas':mochilas}

                return render(request, "app/Mochilas2.html", contexto) #Vuelvo al inicio o a donde quieran
     
    else: 
        miFormulario= MochilasFormulario(initial={'codigo': mochila.codigo, 'descripcion':mochila.descripcion , 'precio':mochila.precio}) 

        contexto={'miFormulario':miFormulario, 'precio':precio}
    return render(request, "app/editarMochila.html", contexto)

            
#LISTVIEW

class TotebagsList(ListView):
    model = Totebags
    template_name='App/Totebags.html'

#DETAILVIEW

class TotebagsDetail(DetailView):
    model= Totebags
    template_name='App/totebagsDetalle.html'

#CREATEVIEW

class TotebagsCreacion(CreateView):
    model=Totebags
    successs_url= reverse_lazy('Totebags')
    fields = ['precio', 'descripcion', 'codigo2']

class TotebagsEdicion(UpdateView):
    model=Totebags
    successs_url= reverse_lazy('Totebags')
    fields = ['precio', 'descripcion', 'codigo2']
    
