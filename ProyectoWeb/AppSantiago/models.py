from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jugadores(models.Model):

    def __str__(self):

            return f'{self.nombre}'
    
    nombre = models.CharField(max_length=100)
    año_nacimiento = models.IntegerField()
    partidos_jugados = models.IntegerField()
    goles = models.IntegerField()
    
class Partidos(models.Model):

    def __str__(self):

            return f'{self.fecha1} -- {self.rival} -- {self.localidad}'

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

    def __str__(self):

            return f'{self.nombre}'
    
    nombre = models.CharField(max_length=100)
    año_nacimiento = models.IntegerField()
    partidos = models.IntegerField()

class Rivales(models.Model):

    def __str__(self):

            return f'{self.nombre} -- {self.localidad}'

    nombre = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    partidos_disputados = models.IntegerField()
    partidos_ganados = models.IntegerField()
    partidos_empatados = models.IntegerField()
    partidos_perdidos = models.IntegerField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', null=True, blank=True)

    def __str__(self):
          
        return f"{self.user} --- {self.imagen}"