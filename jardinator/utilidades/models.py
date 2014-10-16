from django.db import models


class Region(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Regiones"


class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    region = models.ForeignKey(Region)

    class Meta:
        verbose_name_plural = "Ciudades"

