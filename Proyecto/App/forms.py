from django import forms 

class Mochilas(forms.Form):
    #texto  = forms.TextField()
    #imagen = models.ImageField()
    descripcion = forms.CharField(max_length=1000)
    precio= forms.IntegerField()

class Totebags (forms.Form):
    #texto  = forms.TextField()
    #imagen = models.ImageField()
    descripcion = forms.CharField(max_length=1000)
    precio= forms.IntegerField()
    
    
class Informacion_sobre_mi(forms.Form):
    autor = forms.CharField(max_length=40)
    #imagen = models.ImageField()
    #texto  = forms.TextField()
    fecha= forms.DateField()
    