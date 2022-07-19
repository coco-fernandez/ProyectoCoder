from django import forms

class nuevo_estudio(forms.Form):
    nombre=forms.CharField(max_length=30,label="Nombre")
    ubicacion=forms.CharField(max_length=30,label="Ubicación")
    cantidad_salas=forms.IntegerField()
    
class nuevo_banda(forms.Form):
    nombre=forms.CharField(max_length=30,label="Nombre")
    genero=forms.CharField(max_length=30,label="Género")
    cantidad_integrantes=forms.IntegerField()
    
class nuevo_productor(forms.Form):
    nombre=forms.CharField(max_length=30,label="Nombre")
    apellido=forms.CharField(max_length=30,label="Apellido")
    email=forms.EmailField()