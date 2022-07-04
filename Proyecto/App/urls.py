from unicodedata import name
from django.urls import path
from App.views import home, Mochilas, Totebags, Informacion_sobre_mi,   buscar, mochilasFormulario, busquedaCodigoMochilas, leerMochilas

urlpatterns = [
    path('', home, name='home' ),
    path('Mochilas/', Mochilas, name='Mochilas'  ),
    path('totebags/', Totebags, name='totebags' ),
    path('Informacion_sobre_mi/', Informacion_sobre_mi, name='Informacion_sobre_mi' ),
    path('mochilasFormulario/', mochilasFormulario, name='mochilasFormulario' ),
    path('busquedaCodigoMochilas', busquedaCodigoMochilas, name="busquedaCodigoMochilas"),
    path('buscar/', buscar, name='buscar'),
    path('leerMochilas/', leerMochilas, name='leerMochilas'),
]
