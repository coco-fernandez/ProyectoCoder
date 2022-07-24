from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estudios(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    ubicacion = models.CharField(max_length=30)
    cantidad_salas = models.IntegerField()

    class Meta:
        verbose_name_plural="Estudios"

class Bandas(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    genero = models.CharField(max_length=30) # Texto
    cantidad_integrantes = models.IntegerField() # Email - Opcional
    class Meta:
        verbose_name_plural="Bandas"

class Productores(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    apellido = models.CharField(max_length=30) # Texto
    email = models.EmailField(blank=True, null=True) # Email - Opcional
    class Meta:
        verbose_name_plural="Productores"

class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)
