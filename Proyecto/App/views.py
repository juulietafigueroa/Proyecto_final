from contextlib import ContextDecorator
from dataclasses import field
import imp
from xml.etree.ElementTree import QName
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pydoc import describe
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from App.forms import MochilasFormulario, TotebagsFormulario, UserRegisterForm, UserEditForm

from App.models import Mochilas, Totebags
from django.urls import reverse_lazy
#LOGIN
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin

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
    totebagss = Totebags.objects.all()
    contexto= {'totebag':totebagss}
    return render (request, 'app/Totebags.html', contexto)
   

   





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
    template_name='App/Totebag_list.html'

#DETAILVIEW

class TotebagDetalle(DetailView):
    model= Totebags
    template_name='App/Totebag_detalle.html'

#CREATEVIEW

class TotebagCreacion(CreateView):
    model=Totebags
    successs_url= reverse_lazy('totebags_list')
    fields = ['precio', 'descripcion']

class TotebagEdicion(UpdateView):
    model=Totebags
    successs_url= reverse_lazy('totebags_list')
    fields = ['precio', 'descripcion']
    
class TotebagEliminacion(DeleteView):
    model=Totebags
    successs_url= reverse_lazy('totebags_list')
    
#-------------------------
#LOGIN

def login_request(request):


        if request.method == "POST":
            form = AuthenticationForm(request, request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  clave = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=clave)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"App/home.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"App/home.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"App/home.html" ,  {"mensaje":"Error, datos incorrectos"})
        else:
         form = AuthenticationForm()

         return render(request,"App/login.html", {'form':form} )



#REGISTER 

def register_request(request):

      if request.method == 'POST':

            
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,'App/home.html' ,  {'mensaje': f'Usuario {username} creado'})
            else:
                return render(request, 'App/home.html', {'mensaje': 'Error, no se pudo crear el usuario'})

      else:
                  
            form = UserRegisterForm()     

      return render(request,"App/register.html" ,  {"form":form})

 


def editarPerfil(request):

      #Instancia del login
      usuario = request.user
     
      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            formulario = UserEditForm(request.POST, instance=usuario) 
            if formulario.is_valid:   #Si pasó la validación de Django

                informacion = formulario
            
                #Datos que se modificarán
                usuario.email = informacion['email']
                usuario.password1 = informacion['password1']
                usuario.password2 = informacion['password1']
                usuario.save()

                return render(request, "App/home.html", {'usuario':usuario, 'mensaje': 'Datos cambiados exitosamente'}) #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            formulario= UserEditForm(initial={ 'email':usuario.email}) 

      #Voy al html que me permite editar
      return render(request, "App/editarPerfil.html", {"formulario":formulario, "usuario":usuario.username})

