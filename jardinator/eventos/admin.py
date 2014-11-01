from django.contrib import admin
from eventos import models

admin.site.register(models.Evento)
admin.site.register(models.StockPlantas)
admin.site.register(models.StockInsumos)
admin.site.register(models.PlantasAsignadas)
admin.site.register(models.InsumosAsignados)