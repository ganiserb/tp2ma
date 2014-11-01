from django.contrib import admin
from eventos import models


class EventoDetallePlantasInline(admin.TabularInline):
    model = models.PlantasAsignadas
    extra = 1


class EventoDetalleMaterialesInline(admin.TabularInline):
    model = models.InsumosAsignados
    extra = 1


class EventoAdmin(admin.ModelAdmin):
    inlines = (EventoDetallePlantasInline, EventoDetalleMaterialesInline)

# Register your models here.
admin.site.register(models.Evento, EventoAdmin)
admin.site.register(models.StockPlantas)
admin.site.register(models.StockInsumos)
