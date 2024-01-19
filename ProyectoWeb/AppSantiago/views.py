from django.shortcuts import render
from django.http import HttpResponse
from AppSantiago.models import Entrenadores, Jugadores, Partidos, Rivales, Avatar
from AppSantiago.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def InicioSesion(request):
     
    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
              
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contra)

            if user:
                 
                login(request, user)

                return render(request, "AppSantiago/inicio.html", {'mensaje':f'Bienvenido {user}.'})
            
        else:

            return render(request, "AppSantiago/inicio.html", {'mensaje':'Datos incorrectos.'})

    else:
         
        form = AuthenticationForm()

    return render(request, "AppSantiago/login.html", {'formulario':form})

def registro(request):
     
    if request.method == "POST":
         
        form = UsuarioRegistro(request.POST)

        if form.is_valid():
             
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'AppSantiago/inicio.html', {'mensaje':"Usuario creado."})
        
    else:

        form = UsuarioRegistro()

    return render(request, "AppSantiago/registro.html", {'formulario':form})

@login_required 
def editar_perfil(request):

    usuario_actual = request.user

    if request.method == "POST":
         
        form = EditarUsuario(request.POST)

        if form.is_valid():
             
            info = form.cleaned_data
            
            usuario_actual.first_name = info['first_name']
            usuario_actual.last_name = info['last_name']
            usuario_actual.email = info['email']
                        
            usuario_actual.save()
            
            return render(request, 'AppSantiago/inicio.html')
        
    else:

        form = EditarUsuario(initial = {"first_name": usuario_actual.first_name,
                                        "last_name": usuario_actual.last_name,
                                        "email": usuario_actual.email})

    return render(request, "AppSantiago/editar_usuario.html", {'formulario':form})

@login_required
def agregar_avatar(request):
    
    if request.method=='POST':
        
        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
 
            avatar = Avatar(user=request.user, imagen=informacion['imagen'])

            avatar.save()

            return render(request, 'AppSantiago/inicio.html')
    
    else:
         
        miFormulario = AvatarFormulario()

    return render(request, "AppSantiago/agregarImg.html", {'form':miFormulario})

def cerrar_sesion(request):
    logout(request) 

    return render(request, 'AppSantiago/logout.html')

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

def about_me(request):

    return render(request, 'AppSantiago/about.html')

def notfound(request):

    return render(request, 'AppSantiago/notfound.html')

# FORMULAS AGREGAR DATOS

@login_required
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

@login_required
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

@login_required
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

@login_required
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

# LEER RESULTADOS
    
def leerEntrenadores(request):
     
    entrenadores = Entrenadores.objects.all()

    contexto = {"DTs": entrenadores}

    return render(request, "AppSantiago/leerEntrenadores.html", contexto)

def leerJugadores(request):
     
    jugadores = Jugadores.objects.all()

    contexto = {"JUG": jugadores}

    return render(request, "AppSantiago/leerJugadores.html", contexto)

def leerRivales(request):
     
    rivales = Rivales.objects.all()

    contexto = {"RIV": rivales}

    return render(request, "AppSantiago/leerRivales.html", contexto)

def leerPartidos(request):
     
    partidos = Partidos.objects.all()

    contexto = {"PART": partidos}

    return render(request, "AppSantiago/leerPartidos.html", contexto)

# ELIMINAR RESULTADOS

@login_required
def eliminarEntrenadores(request, DTNombre):
     
    entrenadores = Entrenadores.objects.get(nombre=DTNombre)
    entrenadores.delete()

    entrenadores = Entrenadores.objects.all()

    contexto = {"DTs":entrenadores}

    return render(request, "AppSantiago/leerEntrenadores.html", contexto)

@login_required
def eliminarJugadores(request, JUGNombre):
     
    jugadores = Jugadores.objects.get(nombre=JUGNombre)
    jugadores.delete()

    jugadores = Jugadores.objects.all()

    contexto = {"JUG":jugadores}

    return render(request, "AppSantiago/leerJugadores.html", contexto)

@login_required
def eliminarRivales(request, RIVNombre):
     
    rivales = Rivales.objects.get(nombre=RIVNombre)
    rivales.delete()

    rivales = Rivales.objects.all()

    contexto = {"RIV":rivales}

    return render(request, "AppSantiago/leerRivales.html", contexto)

@login_required
def eliminarPartidos(request, PARTFecha1):
     
    partidos = Partidos.objects.get(fecha1=PARTFecha1)
    partidos.delete()

    partidos = Partidos.objects.all()

    contexto = {"PART":partidos}

    return render(request, "AppSantiago/leerPartidos.html", contexto)

# EDITAR RESULTADOS

@login_required
def editarEntrenadores(request, DTNombre):
     
    entrenadores = Entrenadores.objects.get(nombre=DTNombre)
    
    if request.method == "POST":

        nuevo_formulario_Entrenadores = TecnicoFormulario(request.POST)
        
        if nuevo_formulario_Entrenadores.is_valid():

                info = nuevo_formulario_Entrenadores.cleaned_data

                entrenadores.nombre = info["nombre"]
                entrenadores.año_nacimiento = info["año_nacimiento"]
                entrenadores.partidos = info["partidos"]

                entrenadores.save()

                return render(request, "AppSantiago/inicio.html")

    else :
         
         nuevo_formulario_Entrenadores = TecnicoFormulario(initial={"nombre":entrenadores.nombre, 
                                                                    "año_nacimiento":entrenadores.año_nacimiento, 
                                                                    "partidos":entrenadores.partidos}) 

    return render(request, "AppSantiago/editarEntrenador.html", {"mi_formu_entrenador":nuevo_formulario_Entrenadores, "nombre":DTNombre})

@login_required
def editarJugadores(request, JUGNombre):
     
    jugadores = Jugadores.objects.get(nombre=JUGNombre)
    
    if request.method == "POST":

        nuevo_formulario_Jugadores = JugadoresFormulario(request.POST)
        
        if nuevo_formulario_Jugadores.is_valid():

                info = nuevo_formulario_Jugadores.cleaned_data

                jugadores.nombre = info["nombre"]
                jugadores.año_nacimiento = info["año_nacimiento"]
                jugadores.partidos_jugados = info["partidos_jugados"]
                jugadores.goles = info["goles"]

                jugadores.save()

                return render(request, "AppSantiago/inicio.html")

    else :
         
         nuevo_formulario_Jugadores = JugadoresFormulario(initial={"nombre":jugadores.nombre, "año_nacimiento":jugadores.año_nacimiento, 
                                                                   "partidos_jugados":jugadores.partidos_jugados, 
                                                                   "goles": jugadores.goles})

    return render(request, "AppSantiago/editarJugador.html", {"mi_formu_jugador":nuevo_formulario_Jugadores, "nombre":JUGNombre})

@login_required
def editarRivales(request, RIVNombre):
     
    rivales = Rivales.objects.get(nombre=RIVNombre)
    
    if request.method == "POST":

        nuevo_formulario_Rivales = RivalesFormulario(request.POST)
        
        if nuevo_formulario_Rivales.is_valid():

                info = nuevo_formulario_Rivales.cleaned_data

                rivales.nombre = info["nombre"]
                rivales.localidad = info["localidad"]
                rivales.provincia = info["provincia"]
                rivales.partidos_disputados = info["partidos_disputados"]
                rivales.partidos_ganados = info["partidos_ganados"]
                rivales.partidos_empatados = info["partidos_empatados"]
                rivales.partidos_perdidos = info["partidos_perdidos"]

                rivales.save()

                return render(request, "AppSantiago/inicio.html")

    else :
         
         nuevo_formulario_Rivales = RivalesFormulario(initial={"nombre":rivales.nombre, "localidad":rivales.localidad, 
                                                                "provincia":rivales.provincia,   
                                                                "partidos_disputados":rivales.partidos_disputados,
                                                                "partidos_ganados":rivales.partidos_ganados,
                                                                "partidos_empatados":rivales.partidos_empatados,
                                                                "partidos_perdidos":rivales.partidos_perdidos})

    return render(request, "AppSantiago/editarRival.html", {"mi_formu_rival":nuevo_formulario_Rivales, "nombre":RIVNombre})

@login_required
def editarPartidos(request, PARTFecha1):
     
    partidos = Partidos.objects.get(fecha1=PARTFecha1)
    
    if request.method == "POST":

        nuevo_formulario_Partidos = PartidosFormulario(request.POST)
        
        if nuevo_formulario_Partidos.is_valid():

                info = nuevo_formulario_Partidos.cleaned_data

                partidos.categoria = info["categoria"]
                partidos.torneo = info["torneo"]
                partidos.fecha1 = info["fecha1"]
                partidos.fecha = info["fecha"]
                partidos.rival = info["rival"]
                partidos.rdo1 = info["rdo1"]
                partidos.rdo2 = info["rdo2"]
                partidos.resultado = info["resultado"]
                partidos.goles = info["goles"]
                partidos.condicion = info["condicion"]
                partidos.estadio = info["estadio"]
                partidos.localidad = info["localidad"]

                partidos.save()

                return render(request, "AppSantiago/inicio.html")

    else :
         
         nuevo_formulario_Partidos = PartidosFormulario(initial={"categoria":partidos.categoria, 
                                                                "torneo":partidos.torneo, 
                                                                "fecha1":partidos.fecha1,
                                                                "fecha":partidos.fecha,
                                                                "rival":partidos.rival,                                                                
                                                                "rdo1":partidos.rdo1,
                                                                "rdo2":partidos.rdo2,
                                                                "resultado":partidos.resultado,
                                                                "goles":partidos.goles,
                                                                "condicion":partidos.condicion,
                                                                "estadio":partidos.estadio,
                                                                "localidad":partidos.localidad,
                                                                                                                     
                                                                })

    return render(request, "AppSantiago/editarPartido.html", {"mi_formu_partido":nuevo_formulario_Partidos, "nombre":PARTFecha1})

