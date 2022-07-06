import datetime
from html.entities import html5
from django.shortcuts import redirect, render
from django.http import HttpResponse
from httplib2 import Http
from .forms import nuevo_curso, nuevo_estudiante, nuevo_profesor
from ProyectoCoderApp.models import Curso, Estudiante, Profesor



# Create your views here.

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})

def cursos(request):
    cursos=Curso.objects.all()
    ctx={"cursos":cursos}
    return render(request,'ProyectoCoderApp/cursos.html',ctx)

def estudiantes(request):
    estudiantes=Estudiante.objects.all()
    ctx={"estudiantes":estudiantes}
    return render(request,'ProyectoCoderApp/estudiantes.html',ctx)

def profesores(request):
    profesores=Profesor.objects.all()
    ctx={"profesores":profesores}
    return render(request,'ProyectoCoderApp/profesores.html',ctx)

def crear_curso(request):    # clase de creacion de curso por formulario de web

    if request.method=="POST":    #post
        
        formulario=nuevo_curso(request.POST)
        
        if formulario.is_valid():
            
            info_curso=formulario.cleaned_data
        
            curso=Curso(nombre=info_curso["nombre"],comision=info_curso["comision"])
            
            curso.save()    #guarda en la DB
            
            return redirect("cursos")
        
        else:
            return render(request,'ProyectoCoderApp/formulario_curso.html',{"form":formulario})
    
    else:
        formulario=nuevo_curso()
        
        return render(request,'ProyectoCoderApp/formulario_curso.html',{"form":formulario})


def crear_profesor(request):    # clase de creacion de curso por formulario de web

    if request.method=="POST":    #post
        
        formulario=nuevo_profesor(request.POST)
        
        if formulario.is_valid():
            
            info_profesor=formulario.cleaned_data
        
            profesor=Profesor(nombre=info_profesor["nombre"],apellido=info_profesor["apellido"],email=info_profesor["email"])
            
            profesor.save()    #guarda en la DB
            
            return redirect("profesores")
        
        else:
            return render(request,'ProyectoCoderApp/formulario_profesor.html',{"form":formulario})
    
    else:
        formulario=nuevo_profesor()
        
        return render(request,'ProyectoCoderApp/formulario_profesor.html',{"form":formulario})


def crear_estudiante(request):    # clase de creacion de curso por formulario de web

    if request.method=="POST":    #post
        
        formulario=nuevo_estudiante(request.POST)
        
        if formulario.is_valid():
            
            info_estudiante=formulario.cleaned_data
        
            estudiante=Estudiante(nombre=info_estudiante["nombre"],apellido=info_estudiante["apellido"],email=info_estudiante["email"])
            
            estudiante.save()    #guarda en la DB
            
            return redirect("estudiantes")
        
        else:
            return render(request,'ProyectoCoderApp/formulario_estudiante.html',{"form":formulario})
    
    else:
        formulario=nuevo_estudiante()
        
        return render(request,'ProyectoCoderApp/formulario_estudiante.html',{"form":formulario})



def entregables(request):
    return HttpResponse("Vista de entregable")

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








