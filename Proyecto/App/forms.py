from re import T
from django import forms 
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
class MochilasFormulario(forms.Form):
    #texto  = forms.TextField()
    #imagen = models.ImageField()
    descripcion = forms.CharField(max_length=50)
    precio= forms.IntegerField()
    codigo=forms.IntegerField()

class TotebagsFormulario (forms.Form):
    #texto  = forms.TextField()
    #imagen = models.ImageField()
    descripcion = forms.CharField(max_length=1000)
    precio= forms.IntegerField()
    
    
class Informacion_sobre_mi(forms.Form):
    autor = forms.CharField(max_length=40)
    #imagen = models.ImageField()
    #texto  = forms.TextField()
    fecha= forms.DateField()

class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar la contraseña', widget=forms.PasswordInput) 
   
    #last_name = forms.CharField()
    #first_name = forms.CharField()
    #imagen_avatar = forms.ImageField(required=False)

class Meta:
        model = User
        fields = ['username', 'email', 'password1'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):

    #Acá se definen las opciones que queres modificar del usuario, 
    #Ponemos las básicas
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 


    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
      
        help_texts = {k:"" for k in fields}


