from django.urls import path
from AppSantiago.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('buscador/', busqueda_rivales_localidad, name="Buscador"),
    path('jugadores/', agregar_Jugadores, name="Jugadores"),
    path('partidos/', agregar_Partidos, name="Partidos"),
    path('tecnicos/', agregar_Entrenadores, name="Tecnicos"),
    path('rivales/', agregar_Rivales, name="Rivales"),


]