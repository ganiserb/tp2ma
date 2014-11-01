from django.contrib import admin
from gestion.models import Empleado, Contrato, Tarea, Log

admin.site.register(Empleado)
admin.site.register(Contrato)
admin.site.register(Tarea)
admin.site.register(Log)
