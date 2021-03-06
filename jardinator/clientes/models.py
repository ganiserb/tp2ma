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

    def __str__(self):
        return self.ciudad.region.nombre + ', ' + self.ciudad.nombre\
                                         + ' - ' + self.direccion

    class Meta:
        verbose_name_plural = "Propiedades"


class Jardin(models.Model):
    propiedad = models.ForeignKey(Propiedad)
    nombre = models.CharField(max_length=30)
    area = models.IntegerField(help_text="Area del jardín, en metros cuadrados")
    plantas = models.ManyToManyField(inventarios.models.Planta,
                                     through='DetallePlantas',
                                     related_name='jardines')
    accesorios = models.ManyToManyField(inventarios.models.Material,
                                        through='DetalleMateriales',
                                        related_name='jardines')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Jardines"


class DetallePlantas(models.Model):
    jardin = models.ForeignKey(Jardin)
    tipo_planta = models.ForeignKey(inventarios.models.Planta,
                                    name='Tipo de planta')
    cantidad = models.IntegerField()

    def __str__(self):
        return ""

    class Meta:
        verbose_name_plural = "Plantas que posee"


class DetalleMateriales(models.Model):
    jardin = models.ForeignKey(Jardin)
    tipo_material = models.ForeignKey(inventarios.models.Material,
                                      name='Tipo de material')
    cantidad = models.IntegerField()

    def __str__(self):
        return ""

    class Meta:
        verbose_name_plural = "Accesorios que contiene"