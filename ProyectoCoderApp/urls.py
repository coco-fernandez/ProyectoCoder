from django.contrib import admin
from django.urls import path,include

from ProyectoCoderApp.models import *
from .views import *


urlpatterns = [
    path('',index,name="index"),
    path('productores/',productores,name="productores"),
    path('bandas/', bandas, name="bandas"),
    path('eliminar_banda/<banda_id>', eliminar_banda, name="eliminar_banda"),
    
    path('estudios/',estudios,name="estudios"),
    path('crear_estudio/',crear_estudio,name="crear_estudio"),
    path('crear_banda/',crear_banda,name="crear_banda"),
    path('crear_productor/',crear_productor,name="crear_productor"),
    # path('buscar_comision/',buscar_comision,name="buscar_comision"),
    # path('base',base),
]
