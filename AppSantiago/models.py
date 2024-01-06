from django.db import models

# Create your models here.

class Jugadores(models.Model):

    nombre = models.CharField(max_length=100)
    año_nacimiento = models.IntegerField()
    partidos_jugados = models.IntegerField()
    goles = models.IntegerField()
    
class Partidos(models.Model):

    categoria = models.CharField(max_length=50)
    torneo = models.CharField(max_length=50)
    fecha1 = models.DateField()
    fecha = models.CharField(max_length=50)
    rival = models.CharField(max_length=50)
    rdo1 = models.IntegerField()
    rdo2 = models.IntegerField()
    resultado = models.CharField(max_length=50)
    goles = models.CharField(max_length=50)
    condicion = models.CharField(max_length=50)
    estadio = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    
class Entrenadores(models.Model):

    nombre = models.CharField(max_length=100)
    año_nacimiento = models.IntegerField()
    partidos = models.IntegerField()

class Rivales(models.Model):

    nombre = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    partidos_disputados = models.IntegerField()
    partidos_ganados = models.IntegerField()
    partidos_empatados = models.IntegerField()
    partidos_perdidos = models.IntegerField()