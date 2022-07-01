from django.urls import path
from App.views import home, Mochilas, Totebags, Informacion_sobre_mi, formulario_mochilas

urlpatterns = [
    path('', home, name='home' ),
    path('mochilas/', Mochilas, name='mochilas'  ),
    path('totebags/', Totebags, name='totebags' ),
    path('Informacion_sobre_mi/', Informacion_sobre_mi, name='Informacion_sobre_mi' ),
    path('formulariomochilas/', formulario_mochilas, name='formulario_mochilas' ),


    
]
