from django.contrib import admin
from publicidades.models import Publicidad


class AdminPublicidad(admin.ModelAdmin):
    """Administrador de publicidad."""
    list_display = ('id', 'titulo', 'texto', 'foto', 'fecha')
    list_filter = ('titulo', 'foto', 'fecha')
    search_fields = ('titulo', 'fecha')


admin.site.register(Publicidad, AdminPublicidad)