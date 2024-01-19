from django.urls import path
from AppSantiago.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('login/', InicioSesion, name='Login'),
    path('register/', registro, name='Registro'),
    path('logout/', cerrar_sesion, name='Logout'),
    path('edit/', editar_perfil, name='Editar'),
    path('agregarAvatar/', agregar_avatar, name="Subir Avatar"),

    path('buscador/', busqueda_rivales_localidad, name="Buscador"),
    path('resultados/', resultado_busqueda_rivales_localidad, name="resultados"),    
    path('jugadores/', jugadores, name="Jugadores"),
    path('partidos/', partidos, name="Partidos"),
    path('tecnicos/', tecnicos, name="Tecnicos"),
    path('rivales/', rivales, name="Rivales"),
    path('about/', about_me, name="About"),
    path('notfound/', notfound, name="NotFound"),

    #CRUD DE ENTRENADORES
    path('nuevoTecnico/', agregar_Entrenadores, name="EntrenadoresCrear"),       
    path('leerEntrenadores/', leerEntrenadores, name="EntrenadoresLeer"),
    path('eliminarEntrenadores/<DTNombre>', eliminarEntrenadores, name="EntrenadoresEliminar"),
    path('editarEntrenadores/<DTNombre>', editarEntrenadores, name="EntrenadoresEditar"),
    
    #CRUD DE JUGADORES
    path('nuevoJugador/', agregar_Jugadores, name="JugadoresCrear"),
    path('leerJugadores/', leerJugadores, name="JugadoresLeer"),
    path('eliminarJugadores/<JUGNombre>', eliminarJugadores, name="JugadoresEliminar"),
    path('editarJugadores/<JUGNombre>', editarJugadores, name="JugadoresEditar"),
    
    #CRUD DE RIVALES
    path('nuevoRival/', agregar_Rivales, name="RivalesCrear"),
    path('leerRivales/', leerRivales, name="RivalesLeer"),
    path('eliminarRivales/<RIVNombre>', eliminarRivales, name="RivalesEliminar"),
    path('editarRivales/<RIVNombre>', editarRivales, name="RivalesEditar"),

    #CRUD DE PARTIDOS
    path('nuevoPartido/', agregar_Partidos, name="PartidosCrear"),
    path('leerPartidos/', leerPartidos, name="PartidosLeer"),
    path('eliminarPartidos/<PARTFecha1>', eliminarPartidos, name="PartidosEliminar"),
    path('editarPartidos/<PARTFecha1>', editarPartidos, name="PartidosEditar"),

]

