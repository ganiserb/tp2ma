from django.db import models


class Unidad(models.Model):
    """ABM unidad."""
    def __str__(self):
        return self.nombre
    nombre = models.CharField(max_length=250)


class InsumoAccesorio(models.Model):
    """ABM insumos y accesorios."""
    descripcion = models.CharField(max_length=250)
    cantidad = models.IntegerField()
    unidad = models.ForeignKey(Unidad, null=False)
    costo = models.FloatField()