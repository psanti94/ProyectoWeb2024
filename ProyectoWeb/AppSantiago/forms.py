from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppSantiago.models import Avatar

class TecnicoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    año_nacimiento = forms.IntegerField()
    partidos = forms.IntegerField()

class JugadoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    año_nacimiento = forms.IntegerField()
    partidos_jugados = forms.IntegerField()
    goles = forms.IntegerField()

class PartidosFormulario(forms.Form):

    categoria = forms.CharField(max_length=50)
    torneo = forms.CharField(max_length=50)
    fecha1 = forms.DateField()
    fecha = forms.CharField(max_length=50)
    rival = forms.CharField(max_length=50)
    rdo1 = forms.IntegerField()
    rdo2 = forms.IntegerField()
    resultado = forms.CharField(max_length=50)
    goles = forms.CharField(max_length=50)
    condicion = forms.CharField(max_length=50)
    estadio = forms.CharField(max_length=50)
    localidad = forms.CharField(max_length=50)

class RivalesFormulario(forms.Form):

    nombre = forms.CharField(max_length=100)
    localidad = forms.CharField(max_length=100)
    provincia = forms.CharField(max_length=100)
    partidos_disputados = forms.IntegerField()
    partidos_ganados = forms.IntegerField()
    partidos_empatados = forms.IntegerField()
    partidos_perdidos = forms.IntegerField()

class UsuarioRegistro(UserCreationForm):

    username = forms.CharField(label = 'Usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class EditarUsuario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]

class AvatarFormulario(forms.ModelForm):

    class Meta:

        model = Avatar
        fields= ['user', 'imagen']