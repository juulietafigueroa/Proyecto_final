from django.contrib import admin

#from App.forms import Informacion_sobre_mi, Mochilas, Totebags
from .models import * 

# Register your models here.

admin.site.register(Mochilas)
admin.site.register(Totebags)
#admin.site.register(Informacion_sobre_mi)

