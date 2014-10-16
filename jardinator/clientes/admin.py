from django.contrib import admin
from clientes import models
from utilidades.models import Ciudad

# Register your models here.
admin.site.register(models.Propiedad)
admin.site.register(Ciudad)
