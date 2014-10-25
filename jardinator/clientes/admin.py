from django.contrib import admin
from clientes import models


class JardinDetallePlantasInline(admin.TabularInline):
    model = models.DetallePlantas
    extra = 1


class JardinDetalleMaterialesInline(admin.TabularInline):
    model = models.DetalleMateriales
    extra = 1


class JardinAdmin(admin.ModelAdmin):
    inlines = (JardinDetallePlantasInline, JardinDetalleMaterialesInline)

# Register your models here.
admin.site.register(models.Propiedad)
admin.site.register(models.Jardin, JardinAdmin)
