from django.shortcuts import render
from django.http import HttpResponse
from AppSantiago.models import Entrenadores, Jugadores, Partidos, Rivales
from AppSantiago.forms import TecnicoFormulario, JugadoresFormulario, PartidosFormulario, RivalesFormulario

# Create your views here.

def inicio(request):

    return render(request, 'AppSantiago/inicio.html')

def jugadores(request):

    return render(request, 'AppSantiago/jugadores.html')

def partidos(request):

    return render(request, 'AppSantiago/partidos.html')

def tecnicos(request):

    return render(request, 'AppSantiago/tecnicos.html')

def rivales(request):

    return render(request, 'AppSantiago/rivales.html')

# FORMULAS AGREGAR DATOS

def agregar_Entrenadores(request):

    if request.method == "POST":

        nuevo_formulario_Entrenadores = TecnicoFormulario(request.POST)
        
        if nuevo_formulario_Entrenadores.is_valid():

                info = nuevo_formulario_Entrenadores.cleaned_data

                entrenador_nuevo = Entrenadores(nombre=info["nombre"], año_nacimiento=info["año_nacimiento"], partidos=info["partidos"])

                entrenador_nuevo.save()

                return render(request, "AppSantiago/inicio.html")

    else :
         
         nuevo_formulario_Entrenadores = TecnicoFormulario()  

    return render(request, "AppSantiago/formu_entrenador.html", {"mi_formu_entrenador":nuevo_formulario_Entrenadores})

def agregar_Jugadores(request):

    if request.method == "POST":

        nuevo_formulario_Jugadores = JugadoresFormulario(request.POST)
        
        if nuevo_formulario_Jugadores.is_valid():

                info = nuevo_formulario_Jugadores.cleaned_data

                jugador_nuevo = Jugadores(nombre=info["nombre"], año_nacimiento=info["año_nacimiento"], partidos_jugados=info["partidos_jugados"], goles=info["goles"])

                jugador_nuevo.save()

                return render(request, "AppSantiago/inicio.html")

    else :
         
         nuevo_formulario_Jugadores = JugadoresFormulario()  

    return render(request, "AppSantiago/formu_jugador.html", {"mi_formu_jugador":nuevo_formulario_Jugadores})

def agregar_Partidos(request):

    if request.method == "POST":

        nuevo_formulario_Partidos = PartidosFormulario(request.POST)
        
        if nuevo_formulario_Partidos.is_valid():

                info = nuevo_formulario_Partidos.cleaned_data

                partido_nuevo = Partidos(categoria=info["categoria"], torneo=info["torneo"], fecha1=info["fecha1"], fecha=info["fecha"], rival=info["rival"],
                                         rdo1=info["rdo1"], rdo2=info["rdo2"], resultado=info["resultado"], goles=info["goles"], 
                                         condicion=info["condicion"], estadio=info["estadio"], localidad=info["localidad"],) 

                partido_nuevo.save()

                return render(request, "AppSantiago/inicio.html")

    else :
         
         nuevo_formulario_Partidos = PartidosFormulario()  

    return render(request, "AppSantiago/formu_partido.html", {"mi_formu_partido":nuevo_formulario_Partidos})

def agregar_Rivales(request):

    if request.method == "POST":

        nuevo_formulario_Rivales = RivalesFormulario(request.POST)
        
        if nuevo_formulario_Rivales.is_valid():

                info = nuevo_formulario_Rivales.cleaned_data

                rival_nuevo = Rivales(nombre=info["nombre"], localidad=info["localidad"], provincia=info["provincia"], partidos_disputados=info["partidos_disputados"], 
                                      partidos_ganados=info["partidos_ganados"], partidos_empatados=info["partidos_empatados"], partidos_perdidos=info["partidos_perdidos"],) 

                rival_nuevo.save()

                return render(request, "AppSantiago/inicio.html")

    else :
         
         nuevo_formulario_Rivales = RivalesFormulario()  

    return render(request, "AppSantiago/formu_rival.html", {"mi_formu_rival":nuevo_formulario_Rivales})

# FORMULAS BUSCAR DATOS

def busqueda_rivales_localidad(request):
     
    return render(request, "AppSantiago/buscar_rival_localidad.html")     

def resultado_busqueda_rivales_localidad(request):
     
    if request.method == "GET":
          
        localidad_pedido = request.GET['localidad']
        resultados_rival = Rivales.objects.filter(localidad__icontains=localidad_pedido)
 
        return render(request, "AppSantiago/buscar_rival_localidad.html", {"rivales":resultados_rival})

    else:

        return render(request, "AppSantiago/buscar_rival_localidad.html") 

