import datetime
from html.entities import html5
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from httplib2 import Http
from .forms import UserEditForm, nuevo_banda, nuevo_estudio, nuevo_productor
from ProyectoCoderApp.models import Avatar, Bandas, Estudios, Productores
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *



# Create your views here.

def index(request):
    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]
    diccionario = {"nombre":"Juan","apellido":"Perez","edad":20}
    
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url = "/media/avatar/generica.jpg"
        return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas, "url":url})
    return render(request,"ProyectoCoderApp/index.html",)

def base (request):
    return render(request,'ProyectoCoderApp/base.html',{})


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return redirect("login")
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request,"ProyectoCoderApp/login.html",{"form":form})

def register_request(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        # form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') # es la primer contraseña, no la confirmacion

            form.save() # registramos el usuario
            # iniciamos la sesion
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return redirect("login")

        return render(request,"ProyectoCoderApp/register.html",{"form":form})

    form = UserCreationForm()
    # form = UserRegisterForm()

    return render(request,"ProyectoCoderApp/register.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect("index")

@login_required
def editar_perfil(request):

    user = request.user # usuario con el que estamos loggueado
    try:
        avatar = Avatar.objects.get(usuario=user)
    except:
        avatar = Avatar(usuario=user)
        avatar.save()

    if request.method == "POST":
        
        form = UserEditForm(request.POST,request.FILES) # cargamos datos llenados

        if form.is_valid():

            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            avatar.imagen = info["imagen"]
            # user.password = info["password1"]

            user.save()
            avatar.save()
            
            return redirect("index")
        else:
            return render(request,"ProyectoCoderApp/editar_perfil.html",{"form":form})

    else:
        form = UserEditForm(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name, "imagen":avatar.imagen})

    return render(request,"ProyectoCoderApp/editar_perfil.html",{"form":form})

@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
            
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.get(username=request.user.username) # usuario con el que estamos loggueados

            avatar = Avatar(usuario=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            # avatar = Avatar()
            # avatar.usuario = request.user
            # avatar.imagen = form.cleaned_data["imagen"]
            # avatar.save()

            return redirect("index")

    else:
        form = AvatarForm()
    
    return render(request,"ProyectoCoderApp/agregar_avatar.html",{"form":form})



@login_required
def estudios(request):
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            estudios = Estudios.objects.filter( Q(nombre__icontains=search) | Q(genero__icontains=search) ) # .values()                
            return render(request,"ProyectoCoderApp/estudios.html",{"estudios":estudios, "search":True, "busqueda":search})

    estudios = Estudios.objects.all()

    return render(request,"ProyectoCoderApp/estudios.html",{"estudios":estudios})
@login_required
def crear_estudio(request):    # clase de creacion de curso por formulario de web

    if request.method=="POST":    #post
        
        formulario=nuevo_estudio(request.POST)
        
        if formulario.is_valid():
            
            info_estudio=formulario.cleaned_data
        
            estudio=Estudios(
                nombre=info_estudio["nombre"],
                ubicacion=info_estudio["ubicacion"],
                cantidad_salas=info_estudio["cantidad_salas"], 
                detalle=info_estudio["detalle"],
                imagen=info_estudio["imagen"]
                )
            
            estudio.save()    #guarda en la DB
            
            return redirect("estudios")
        
        else:
            return render(request,'ProyectoCoderApp/formulario_estudio.html',{"form":formulario})
    
    else:
        formulario=nuevo_estudio()
        
        return render(request,'ProyectoCoderApp/formulario_estudio.html',{"form":formulario})
@staff_member_required
def eliminar_estudio(request,estudio_id):

    estudio = Estudios.objects.get(id=estudio_id)
    estudio.delete()

    return redirect("estudios")
@staff_member_required
def editar_estudio(request,estudio_id):

    estudio = Estudios.objects.get(id=estudio_id)

    if request.method == "POST":

        formulario = nuevo_estudio(request.POST)

        if formulario.is_valid():
            
            info_estudio = formulario.cleaned_data
            
            estudio.nombre = info_estudio["nombre"]
            estudio.ubicacion = info_estudio["ubicacion"]
            estudio.cantidad_salas = info_estudio["cantidad_salas"]
            estudio.detalle = info_estudio["detalle"]
            estudio.save()

            return redirect("estudios")

    # get
    formulario = nuevo_estudio(initial={"nombre":estudio.nombre, "ubicacion":estudio.ubicacion, "cantidad_salas": estudio.cantidad_salas, "detalle":estudio.detalle})
    
    return render(request,"ProyectoCoderApp/formulario_estudio.html",{"form":formulario})



def bandas(request):
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            bandas = Bandas.objects.filter( Q(nombre__icontains=search) | Q(genero__icontains=search) ).values()                
            return render(request,"ProyectoCoderApp/bandas.html",{"bandas":bandas, "search":True, "busqueda":search})

    bandas = Bandas.objects.all()

    return render(request,"ProyectoCoderApp/bandas.html",{"bandas":bandas})
@login_required
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
@staff_member_required
def eliminar_banda(request,banda_id):

    banda = Bandas.objects.get(id=banda_id)
    banda.delete()

    return redirect("bandas")
@staff_member_required
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


@login_required
def productores(request):
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            productores = Productores.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search) ).values()                
            return render(request,"ProyectoCoderApp/productores.html",{"productores":productores, "search":True, "busqueda":search})

    productores = Productores.objects.all()

    return render(request,"ProyectoCoderApp/productores.html",{"productores":productores})
@login_required
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
@staff_member_required
def eliminar_productor(request,productor_id):

    productor = Productores.objects.get(id=productor_id)
    productor.delete()

    return redirect("productores")
@staff_member_required
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


def no_page(request):
    return render(request,"ProyectoCoderApp/no_page.html",{})

def acerca_de(request):
    return render(request,"ProyectoCoderApp/acerca_de.html",{})



class EstudioDetail(DetailView):

    model = Estudios
    template_name = "ProyectoCoderApp/estudio_detail.html"
