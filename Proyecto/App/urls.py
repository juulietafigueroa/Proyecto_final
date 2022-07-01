from django.urls import path
from App.views import home, Mochilas, Totebags, Informacion_sobre_mi, mochilasFormulario, totebagsFormulario

urlpatterns = [
    path('', home, name='home' ),
    path('mochilas/', Mochilas, name='mochilas'  ),
    path('totebags/', Totebags, name='totebags' ),
    path('Informacion_sobre_mi/', Informacion_sobre_mi, name='Informacion_sobre_mi' ),
    path('formularioMochilas/', mochilasFormulario, name='formularioMochilas' ),
    path('formularioTotebags/', totebagsFormulario, name='formularioTotebags' ),


    
]
