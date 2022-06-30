from django.urls import path
from App.views import home, Historia_comunidad, Actividades_comunidad, Informacion_sobre_mi

urlpatterns = [
    path('', home, name='home' ),
    path('Historia_comunidad/', Historia_comunidad, name='Historia_comunidad'  ),
    path('Actividades_comunidad/', Actividades_comunidad, name='Actividades_comunidad' ),
    path('Informacion_sobre_mi/', Informacion_sobre_mi, name='Informacion_sobre_mi' ),


    
]
