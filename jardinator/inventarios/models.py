from django.db import models


class Unidad(models.Model):
    """ABM unidad."""
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Unidades"


class Material(models.Model):
    """ABM insumos y accesorios."""
    descripcion = models.CharField(max_length=250)
    cantidad = models.IntegerField()
    unidad = models.ForeignKey(Unidad, null=False)
    costo = models.FloatField()

    class Meta:
        verbose_name_plural = "Materiales"