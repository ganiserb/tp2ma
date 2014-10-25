from django.db import models
from jardinator.settings import AUTH_USER_MODEL


class Solicitud(models.Model):
    """ABM solicitudes."""
    usuario = models.ForeignKey(AUTH_USER_MODEL)
    texto = models.CharField(max_length=250)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username + " - " + str(self.fecha.strftime(
            '%x %X'))

    class Meta:
        verbose_name_plural = "Solicitudes de clientes"