from unicodedata import name
from django.urls import path
from App.views import home,  totebags, Informacion_sobre_mi, mochilas2, buscar, mochilasFormulario, busquedaCodigoMochilas, eliminarMochila, editarMochila

urlpatterns = [
    path('', home, name='home' ),
    path('Mochilas2/', mochilas2, name='Mochilas2'  ),
    path('totebags/', totebags, name='totebags' ),
    path('Informacion_sobre_mi/', Informacion_sobre_mi, name='Informacion_sobre_mi' ),
    path('mochilasFormulario/', mochilasFormulario, name='mochilasFormulario' ),
    path('busquedaCodigoMochilas', busquedaCodigoMochilas, name="busquedaCodigoMochilas"),
    path('buscar/', buscar, name='buscar'),
    #path('leerMochilas/', leerMochilas, name='leerMochilas'),
    path('eliminarMochila/<codigo>', eliminarMochila, name='eliminarMochila'),
    path('editarMochila/<precio>', editarMochila, name='editarMochila'),

]
