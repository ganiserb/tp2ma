from django.db import models
import inventarios


class Region(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Regiones"


class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    region = models.ForeignKey(Region)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Ciudades"


class ProxyUnidad(inventarios.models.Unidad):
    class Meta:
        proxy = True
        verbose_name_plural = inventarios.models.Unidad._meta.verbose_name_plural
        verbose_name = inventarios.models.Unidad._meta.verbose_name


class ProxyFamilia(inventarios.models.Familia):
    class Meta:
        proxy = True
        verbose_name_plural = inventarios.models.Familia._meta.verbose_name_plural
        verbose_name = inventarios.models.Familia._meta.verbose_name