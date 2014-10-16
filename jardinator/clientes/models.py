from django.db import models
from jardinator.settings import AUTH_USER_MODEL
from utilidades.models import Ciudad
# from django.contrib.auth import get_user_model
# User = get_user_model()


class Propiedad(models.Model):
    cliente = models.ForeignKey(AUTH_USER_MODEL)
    coordenada_x = models.FloatField()
    coordenada_y = models.FloatField()
    direccion = models.CharField(max_length=25)
    ciudad = models.ForeignKey(Ciudad)