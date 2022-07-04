from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Totebags(models.Model):
    precio  = models.IntegerField()
    #imagen = models.ImageField()
    descripcion = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.descripcion+" "+str(self.precio)

class  Mochilas(models.Model):
    
    #imagen = models.ImageField()
    
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    codigo=models.IntegerField()

    def __str__(self):
        return str(self.codigo)
    



    




