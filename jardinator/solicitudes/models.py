from django.db import models
from jardinator.settings import AUTH_USER_MODEL


class Solicitud(models.Model):
    """ABM solicitudes."""
    usuario = AUTH_USER_MODEL
    texto = models.CharField(max_length=250)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Solicitudes"