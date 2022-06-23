import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse
from httplib2 import Http

from ProyectoCoderApp.models import Curso

# Create your views here.

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})

def crear_curso(request):    # clase de creacion de curso por formulario de web

    if request.method=="POST":    #post
        
        info_formulario=request.POST
        curso=Curso(nombre=request.POST["nombre"],comision=int(request.POST["comision"]))
        curso.save()    #guarda en la DB
        return redirect("inicio")
    
    else:
        return render(request,'ProyectoCoderApp/formulario_curso.html',{})

def profesores(request):
    return render(request,'ProyectoCoderApp/profesores.html',{})

def estudiantes(request):
    return render(request,'ProyectoCoderApp/estudiantes.html',{})

def cursos(request):
    # return HttpResponse("Vista de cursos")
    cursos=Curso.objects.all()
    return render(request,'ProyectoCoderApp/cursos.html',{"cursos":cursos})

def entregables(request):
    return HttpResponse("Vista de entregable")

def base (request):
    return render(request,'ProyectoCoderApp/base.html',{})

