import datetime
from html.entities import html5
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from httplib2 import Http
from .forms import nuevo_banda, nuevo_estudio, nuevo_productor
from ProyectoCoderApp.models import Bandas, Estudios, Productores
from django.db.models import Q



# Create your views here.

def index(request):
    return render(request,"ProyectoCoderApp/index.html",)

def estudios(request):
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            estudios = Estudios.objects.filter( Q(nombre__icontains=search) | Q(genero__icontains=search) ).values()                
            return render(request,"ProyectoCoderApp/estudios.html",{"estudios":estudios, "search":True, "busqueda":search})

    estudios = Estudios.objects.all()

    return render(request,"ProyectoCoderApp/estudios.html",{"estudios":estudios})

def eliminar_estudio(request,estudio_id):

    estudio = Estudios.objects.get(id=estudio_id)
    estudio.delete()

    return redirect("estudios")

def editar_estudio(request,estudio_id):

    estudio = Estudios.objects.get(id=estudio_id)

    if request.method == "POST":

        formulario = nuevo_estudio(request.POST)

        if formulario.is_valid():
            
            info_estudio = formulario.cleaned_data
            
            estudio.nombre = info_estudio["nombre"]
            estudio.ubicacion = info_estudio["ubicacion"]
            estudio.cantidad_salas = info_estudio["cantidad_salas"]
            estudio.save()

            return redirect("estudios")

    # get
    formulario = nuevo_estudio(initial={"nombre":estudio.nombre, "ubicacion":estudio.ubicacion, "cantidad_salas": estudio.cantidad_salas})
    
    return render(request,"ProyectoCoderApp/formulario_estudio.html",{"form":formulario})

def bandas(request):
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            bandas = Bandas.objects.filter( Q(nombre__icontains=search) | Q(genero__icontains=search) ).values()                
            return render(request,"ProyectoCoderApp/bandas.html",{"bandas":bandas, "search":True, "busqueda":search})

    bandas = Bandas.objects.all()

    return render(request,"ProyectoCoderApp/bandas.html",{"bandas":bandas})

def eliminar_banda(request,banda_id):

    banda = Bandas.objects.get(id=banda_id)
    banda.delete()

    return redirect("bandas")

def editar_banda(request,banda_id):

    banda = Bandas.objects.get(id=banda_id)

    if request.method == "POST":

        formulario = nuevo_banda(request.POST)

        if formulario.is_valid():
            
            info_banda = formulario.cleaned_data
            
            banda.nombre = info_banda["nombre"]
            banda.genero = info_banda["genero"]
            banda.cantidad_integrantes = info_banda["cantidad_integrantes"]
            banda.save()

            return redirect("bandas")

    # get
    formulario = nuevo_banda(initial={"nombre":banda.nombre, "genero":banda.genero, "cantidad_integrantes": banda.cantidad_integrantes})
    
    return render(request,"ProyectoCoderApp/formulario_banda.html",{"form":formulario})

def productores(request):
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            productores = Productores.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search) ).values()                
            return render(request,"ProyectoCoderApp/productores.html",{"productores":productores, "search":True, "busqueda":search})

    productores = Productores.objects.all()

    return render(request,"ProyectoCoderApp/productores.html",{"productores":productores})

def eliminar_productor(request,productor_id):

    productor = Productores.objects.get(id=productor_id)
    productor.delete()

    return redirect("productores")

def editar_productor(request,productor_id):

    productor = Productores.objects.get(id=productor_id)

    if request.method == "POST":

        formulario = nuevo_productor(request.POST)

        if formulario.is_valid():
            
            info_productor = formulario.cleaned_data
            
            productor.nombre = info_productor["nombre"]
            productor.apellido = info_productor["apellido"]
            productor.email = info_productor["email"]
            productor.save()

            return redirect("productores")

    # get
    formulario = nuevo_productor(initial={"nombre":productor.nombre, "apellido":productor.apellido, "email": productor.email})
    
    return render(request,"ProyectoCoderApp/formulario_productor.html",{"form":formulario})

def crear_estudio(request):    # clase de creacion de curso por formulario de web

    if request.method=="POST":    #post
        
        formulario=nuevo_estudio(request.POST)
        
        if formulario.is_valid():
            
            info_estudio=formulario.cleaned_data
        
            estudio=Estudios(nombre=info_estudio["nombre"],ubicacion=info_estudio["ubicacion"],cantidad_salas=info_estudio["cantidad_salas"])
            
            estudio.save()    #guarda en la DB
            
            return redirect("estudios")
        
        else:
            return render(request,'ProyectoCoderApp/formulario_estudio.html',{"form":formulario})
    
    else:
        formulario=nuevo_estudio()
        
        return render(request,'ProyectoCoderApp/formulario_estudio.html',{"form":formulario})


def crear_productor(request):    # clase de creacion de curso por formulario de web

    if request.method=="POST":    #post
        
        formulario=nuevo_productor(request.POST)
        
        if formulario.is_valid():
            
            info_productor=formulario.cleaned_data
        
            productor=Productores(nombre=info_productor["nombre"],apellido=info_productor["apellido"],email=info_productor["email"])
            
            productor.save()    #guarda en la DB
            
            return redirect("productores")
        
        else:
            return render(request,'ProyectoCoderApp/formulario_productor.html',{"form":formulario})
    
    else:
        formulario=nuevo_productor()
        
        return render(request,'ProyectoCoderApp/formulario_productor.html',{"form":formulario})


def crear_banda(request):    # clase de creacion de curso por formulario de web

    if request.method=="POST":    #post
        
        formulario=nuevo_banda(request.POST)
        
        if formulario.is_valid():
            
            info_banda=formulario.cleaned_data
        
            banda=Bandas(nombre=info_banda["nombre"],genero=info_banda["genero"],cantidad_integrantes=info_banda["cantidad_integrantes"])
            
            banda.save()    #guarda en la DB
            
            return redirect("bandas")
        
        else:
            return render(request,'ProyectoCoderApp/formulario_banda.html',{"form":formulario})
    
    else:
        formulario=nuevo_banda()
        
        return render(request,'ProyectoCoderApp/formulario_banda.html',{"form":formulario})




def base (request):
    return render(request,'ProyectoCoderApp/base.html',{})

