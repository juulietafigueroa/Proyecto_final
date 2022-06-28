from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Historia_comunidad(models.Model):
    texto  = models.TextField()
    #imagen = models.ImageField()
    autor = models.CharField(max_length=40)
    fecha_en_que_se_escribio= models.DateTimeField()

class Actividades_comunidad (models.Model):
    texto  = models.TextField()
    #imagen = models.ImageField()
    autor = models.CharField(max_length=40)
    fecha_en_que_se_escribio= models.DateTimeField()

class Informacion_sobre_mi(models.Model):
    autor = models.CharField(max_length=40)
    #imagen = models.ImageField()
    texto  = models.TextField()
    fecha= models.DateTimeField()



