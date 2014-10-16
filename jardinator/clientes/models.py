from django.db import models
from jardinator.settings import AUTH_USER_MODEL
from utilidades.models import Ciudad
import inventarios
# from django.contrib.auth import get_user_model
# User = get_user_model()


class Propiedad(models.Model):
    cliente = models.ForeignKey(AUTH_USER_MODEL)
    coordenada_x = models.FloatField()
    coordenada_y = models.FloatField()
    direccion = models.CharField(max_length=25)
    ciudad = models.ForeignKey(Ciudad)


class Jardin(models.Model):
    propiedad = models.ForeignKey(Propiedad)
    nombre = models.CharField(max_length=30)
    area = models.IntegerField(help_text="Areal del jardín, en metros cuadrados")
    plantas = models.ManyToManyField(inventarios.models.Planta,
                                     related_name='jardines')
    accesorios = models.ManyToManyField(inventarios.models.Material,
                                        related_name='jardines')
