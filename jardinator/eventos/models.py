from django.db import models
from django.core.exceptions import ValidationError
from clientes.models import Propiedad
from jardinator.settings import AUTH_USER_MODEL
from inventarios.models import Planta, Insumo
from django.db.models import Sum


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


# class StockPlantas(models.Model):
#     """ABM inventario de plantas disponibles para un evento."""
#     planta = models.OneToOneField(Planta)
#     cantidad = models.PositiveIntegerField()
#
#     def __str__(self):
#         return self.planta.nombre
#
#     class Meta:
#         verbose_name_plural = "Stock de plantas"


# class StockInsumos(models.Model):
#     """ABM inventario de insumos disponibles para un evento."""
#     insumo = models.OneToOneField(Insumo)
#     cantidad = models.PositiveIntegerField()
#
#     def __str__(self):
#         return self.insumo.descripcion
#
#     class Meta:
#         verbose_name_plural = "Stock de insumos"


class PlantasAsignadas(models.Model):
    """ABM plantas asignadas a un determinado evento."""
    evento = models.ForeignKey(Evento)
    planta = models.ForeignKey(Planta)
    cantidad = models.PositiveIntegerField()

    def clean(self):
        if self.cantidad <= 0:
            raise ValidationError('No se admiten valores no positivos')
        eventos_inicio = PlantasAsignadas.objects.filter(evento__inicio__lt=self.evento.inicio)\
                                                 .filter(evento__fin__gt=self.evento.inicio)

        eventos_fin = PlantasAsignadas.objects.filter(evento__inicio__lt=self.evento.fin)\
                                              .filter(evento__fin__gt=self.evento.fin)

        plantas_inicio = PlantasAsignadas.objects.filter(evento__id__in=eventos_inicio)\
                                                 .filter(planta=self.planta)\
                                                 .aggregate(Sum('cantidad'))['cantidad__sum']

        plantas_fin = PlantasAsignadas.objects.filter(evento__id__in=eventos_fin)\
                                              .filter(planta=self.planta)\
                                              .aggregate(Sum('cantidad'))['cantidad__sum']
        if plantas_inicio and plantas_fin:
            plantas_asignadas = plantas_inicio + plantas_fin
        elif plantas_inicio:
            plantas_asignadas = plantas_inicio
        else:
            plantas_asignadas = plantas_fin

        stock_total = Planta.objects.get(id=self.planta.id).stock
        if plantas_asignadas:
            disponibles = (stock_total - plantas_asignadas)
        else:
            disponibles = stock_total

        if self.cantidad > disponibles:
            raise ValidationError('Se han asignado más plantas que las disponibles para esa fecha')

        super(PlantasAsignadas, self).clean()

    def __str__(self):
        return self.planta.nombre + ' (evento "' + self.evento.nombre + '")'

    class Meta:
        verbose_name_plural = "Plantas asignadas"
        unique_together = ['evento', 'planta']


class InsumosAsignados(models.Model):
    """ABM insumos asignados a un determinado evento."""
    evento = models.ForeignKey(Evento)
    insumo = models.ForeignKey(Insumo)
    cantidad = models.PositiveIntegerField()

    def clean(self):
        if self.cantidad <= 0:
            raise ValidationError('No se admiten valores no positivos')
        eventos_inicio = InsumosAsignados.objects.filter(evento__inicio__lt=self.evento.inicio)\
                                          .filter(evento__fin__gt=self.evento.inicio)

        eventos_fin = InsumosAsignados.objects.filter(evento__inicio__lt=self.evento.fin)\
                                          .filter(evento__fin__gt=self.evento.fin)

        insumos_inicio = InsumosAsignados.objects.filter(evento__id__in=eventos_inicio)\
                                                 .filter(insumo=self.insumo)\
                                                 .aggregate(Sum('cantidad'))['cantidad__sum']

        insumos_fin = InsumosAsignados.objects.filter(evento__id__in=eventos_fin)\
                                              .filter(insumo=self.insumo)\
                                              .aggregate(Sum('cantidad'))['cantidad__sum']

        if insumos_inicio and insumos_fin:
            insumos_asignados = insumos_inicio + insumos_fin
        elif insumos_inicio:
            insumos_asignados = insumos_inicio
        else:
            insumos_asignados = insumos_fin

        stock_total = Insumo.objects.get(id=self.insumo.id).stock
        if insumos_asignados:
            disponibles = (stock_total - insumos_asignados)
        else:
            disponibles = stock_total

        if self.cantidad > disponibles:
            raise ValidationError('Se han asignado más insumos que las disponibles para esa fecha')

        super(InsumosAsignados, self).clean()

    def __str__(self):
        return self.insumo.descripcion + ' (evento "' + self.evento.nombre + '")'

    class Meta:
        verbose_name_plural = "Insumos asignados"
        unique_together = ['evento', 'insumo']