from django.db import models
from clientes.models import Propiedad
from jardinator.settings import AUTH_USER_MODEL
from inventarios.models import Planta, Insumo


class Evento(models.Model):
    """ABM eventos."""
    nombre = models.CharField(max_length=150)
    cliente = models.ForeignKey(AUTH_USER_MODEL)
    propiedad = models.ForeignKey(Propiedad)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    plantas = models.ManyToManyField(Planta,
                                     through='PlantasAsignadas',
                                     related_name='eventos')
    insumos = models.ManyToManyField(Insumo,
                                     through='InsumosAsignados',
                                     related_name='eventos')

    def __str__(self):
        return self.nombre + " (cliente " + self.cliente.nombre + ")"

    class Meta:
        verbose_name_plural = "Eventos"


class StockPlantas(models.Model):
    """ABM inventario de plantas disponibles para un evento."""
    planta = models.ForeignKey(Planta)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return self.planta.nombre

    class Meta:
        verbose_name_plural = "Plantas disponibles"


class StockInsumos(models.Model):
    """ABM inventario de insumos disponibles para un evento."""
    insumo = models.ForeignKey(Insumo)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return self.insumo.descripcion

    class Meta:
        verbose_name_plural = "Insumos disponibles"


class PlantasAsignadas(models.Model):
    """ABM plantas asignadas a un determinado evento."""
    evento = models.ForeignKey(Evento)
    planta = models.ForeignKey(Planta)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return self.planta.nombre + ' (Evento "' + self.evento.nombre + '")'

    class Meta:
        verbose_name_plural = "Plantas asignadas"


class InsumosAsignados(models.Model):
    """ABM insumos asignados a un determinado evento."""
    evento = models.ForeignKey(Evento)
    insumo = models.ForeignKey(Insumo)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return self.insumo.descripcion + ' (evento "' + self.evento.nombre + '")'

    class Meta:
        verbose_name_plural = "Insumos asignados"