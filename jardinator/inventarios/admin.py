from django.contrib import admin
from inventarios.models import Insumo, Unidad, Planta, Familia

admin.site.register(Insumo)
#admin.site.register(Unidad)    -> Se registra en app utilidades
admin.site.register(Planta)
#admin.site.register(Familia)   -> Se registra en app utilidades
