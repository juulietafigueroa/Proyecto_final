from unicodedata import name
from django.urls import path
from App.views import home, mochilas, totebags, Informacion_sobre_mi,   buscar, mochilasFormulario, busquedaCodigoMochilas, leerMochilas, eliminarMochila, editarMochila

urlpatterns = [
    path('', home, name='home' ),
    path('Mochilas/', mochilas, name='Mochilas'  ),
    path('totebags/', totebags, name='totebags' ),
    path('Informacion_sobre_mi/', Informacion_sobre_mi, name='Informacion_sobre_mi' ),
    path('mochilasFormulario/', mochilasFormulario, name='mochilasFormulario' ),
    path('busquedaCodigoMochilas', busquedaCodigoMochilas, name="busquedaCodigoMochilas"),
    path('buscar/', buscar, name='buscar'),
    path('leerMochilas/', leerMochilas, name='leerMochilas'),
    path('eliminarMochila/<codigo>', eliminarMochila, name='eliminarMochila'),
    path('editarMochila/<codigo>', editarMochila, name='editarMochila')

]
