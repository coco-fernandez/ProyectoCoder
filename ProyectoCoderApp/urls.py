from django.contrib import admin
from django.urls import path,include

from ProyectoCoderApp.models import *
from .views import *


urlpatterns = [
    path('',index,name="index"),
    path('productores/',productores,name="productores"),
    path('eliminar_productor/<productor_id>', eliminar_productor, name="eliminar_productor"),
    path('editar_productor/<productor_id>', editar_productor, name="editar_productor"),
    path('bandas/', bandas, name="bandas"),
    path('eliminar_banda/<banda_id>', eliminar_banda, name="eliminar_banda"),
    path('editar_banda/<banda_id>', editar_banda, name="editar_banda"),
    
    path('estudios/',estudios,name="estudios"),
    path('eliminar_estudio/<estudio_id>', eliminar_estudio, name="eliminar_estudio"),
    path('editar_estudio/<estudio_id>', editar_estudio, name="editar_estudio"),
    path('crear_estudio/',crear_estudio,name="crear_estudio"),
    path('crear_banda/',crear_banda,name="crear_banda"),
    path('crear_productor/',crear_productor,name="crear_productor"),
    # path('buscar_comision/',buscar_comision,name="buscar_comision"),
    # path('base',base),
]
