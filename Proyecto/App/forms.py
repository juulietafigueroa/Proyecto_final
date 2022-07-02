from django import forms 

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


    