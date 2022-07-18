from django.contrib import admin

from ProyectoCoderApp.models import *
from .models import *

# Register your models here.

class EstudiosAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'ubicacion','cantidad_salas')
    search_fields = ('nombre', 'ubicacion','cantidad_salas')


class BandasAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'genero', 'cantidad_integrantes')


class ProductoresAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'email')
    # readonly_fields=("profesion",)


    



admin.site.register(Estudios,EstudiosAdmin)
admin.site.register(Bandas,BandasAdmin)
admin.site.register(Productores,ProductoresAdmin)


# admin, admin -> python manage.py createsuperuser