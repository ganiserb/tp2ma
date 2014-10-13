from django.contrib import admin
from inventarios.models import InsumoAccesorio, Unidad


class AdminInsumoAccesorio(admin.ModelAdmin):
    """Administrador de insumos y accesorios."""
    list_display = ('id', 'descripcion', 'cantidad', 'unidad', 'costo')
    list_filter = ('descripcion', 'unidad')
    search_fields = ('descripcion', 'unidad')


class AdminUnidad(admin.ModelAdmin):
    """Administrador de unidades."""
    list_display = ('id', 'nombre')
    list_filter = ('nombre', )
    search_fields = ('nombre', )


admin.site.register(InsumoAccesorio, AdminInsumoAccesorio)
admin.site.register(Unidad, AdminUnidad)
