from django.contrib import admin
from inventarios.models import Material, Unidad, Planta, Familia

admin.site.register(Material)
#admin.site.register(Unidad)    -> Se registra en app utilidades
admin.site.register(Planta)
#admin.site.register(Familia)   -> Se registra en app utilidades
