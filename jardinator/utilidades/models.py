from django.db import models


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

