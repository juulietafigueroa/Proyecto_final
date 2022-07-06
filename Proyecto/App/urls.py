from re import template
from unicodedata import name
from django.urls import path
from App.views import home, Informacion_sobre_mi, mochilas2, totebags, buscar, mochilasFormulario, busquedaCodigoMochilas, eliminarMochila, editarMochila, TotebagsList, TotebagDetalle, TotebagCreacion, TotebagEdicion, TotebagEliminacion, login_request, register_request, editarPerfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home' ),
    path('Mochilas2/', mochilas2, name='Mochilas2'  ),
    path('Totebags/', totebags, name='Totebags'  ),
    path('InformacionSobreMi/', Informacion_sobre_mi, name='Informacion_sobre_mi' ),
    path('mochilasFormulario/', mochilasFormulario, name='mochilasFormulario' ),
    path('busquedaCodigoMochilas', busquedaCodigoMochilas, name="busquedaCodigoMochilas"),
    path('buscar/', buscar, name='buscar'),
    #path('leerMochilas/', leerMochilas, name='leerMochilas'),
    path('eliminarMochila/<codigo>', eliminarMochila, name='eliminarMochila'),
    path('editarMochila/<precio>', editarMochila, name='editarMochila'),
  #-----------------------
  path('totebags/list/', TotebagsList.as_view(), name='totebags_list' ),
  path('totebag/<pk>', TotebagDetalle.as_view(), name='totebag_detalle' ),
  path('totebag/nuevo/', TotebagCreacion.as_view(success_url="/App/totebags/list/"), name='totebag_crear' ),
  path('totebag/edicion/<pk>', TotebagEdicion.as_view(success_url="/App/totebags/list/"), name='totebag_editar' ),
  path('totebagg/<pk>', TotebagEliminacion.as_view(success_url="/App/totebags/list/"), name='totebags_borrar'),
  
  path('login/', login_request, name='login'),
  path('register/', register_request, name='registro'),
  path('logout/', LogoutView.as_view(template_name='App/logout.html'), name='logout'),
  path('editarPerfil/', editarPerfil, name='EditarPerfil')
]
