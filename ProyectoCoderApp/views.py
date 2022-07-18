import datetime
from html.entities import html5
from django.shortcuts import redirect, render
from django.http import HttpResponse
from httplib2 import Http
from .forms import nuevo_banda, nuevo_estudio, nuevo_productor
from ProyectoCoderApp.models import Bandas, Estudios, Productores



# Create your views here.

def index(request):
    return render(request,"ProyectoCoderApp/index.html",)

def estudios(request):
    estudios=Estudios.objects.all()
    ctx={"estudios":estudios}
    return render(request,'ProyectoCoderApp/estudios.html',ctx)

def bandas(request):
    bandas=Bandas.objects.all()
    ctx={"bandas":bandas}
    return render(request,'ProyectoCoderApp/bandas.html',ctx)

def productores(request):
    productores=Productores.objects.all()
    ctx={"productores":productores}
    return render(request,'ProyectoCoderApp/productores.html',ctx)

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

def buscar_comision(request):
    
    if request.method=="POST":
        
        comision=request.POST["comision"]
        
        comisiones=Curso.objects.filter(comision__icontains=comision)
        
        return render(request,'ProyectoCoderApp/buscar_comision.html',{"comisiones":comisiones})
    
    else:
    
        comisiones=[]    #Curso.objects.all()
        return render(request,'ProyectoCoderApp/buscar_comision.html',{"comisiones":comisiones})








