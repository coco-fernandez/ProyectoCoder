from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('', inicio, name="inicio"),
    path('profesores/',profesores,name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('cursos/',cursos,name="cursos"),
    path('crear_curso/',crear_curso,name="crear_curso"),
    path('crear_estudiante/',crear_estudiante,name="crear_estudiante"),
    path('crear_profesor/',crear_profesor,name="crear_profesor"),
    path('buscar_comision/',buscar_comision,name="buscar_comision"),
    path('entregables/',entregables,name="entregables"),
    # path('base',base),
]
