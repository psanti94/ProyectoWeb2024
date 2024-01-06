from django import forms

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