from django.db import models


class Unidad(models.Model):
    """Modelo unidad."""
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Unidades"


class Material(models.Model):
    """Modelo insumos y accesorios."""
    descripcion = models.CharField(max_length=250)
    cantidad = models.IntegerField()
    unidad = models.ForeignKey(Unidad, null=False)
    costo = models.FloatField()

    class Meta:
        verbose_name_plural = "Materiales"


class Familia(models.Model):
    """Modelo familia"""
    nombre = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Familias"


class Planta(models.Model):
    """Modelo plantas."""
    nombre = models.CharField(max_length=250)
    foto = models.ImageField(upload_to="imagenes_inventario")

    CADUCA = 'ca'
    PERENNE = 'pe'

    TIPO_HOJA_CHOICES = (
        (CADUCA, 'Caduca'),
        (PERENNE, 'Perenne')
    )

    tipo_hoja = models.CharField(max_length=2,
                            choices=TIPO_HOJA_CHOICES,
                            default=CADUCA)

    tipo_flor = models.CharField(max_length=250)
    fecha_inicio_temporada_plantacion = models.DateField()
    fecha_fin_temporada_plantacion = models.DateField()
    fecha_inicio_temporada_floracion = models.DateField()
    fecha_fin_temporada_floracion = models.DateField()
    familia = models.ForeignKey(Familia, null=False)
    origen = models.CharField(max_length=250)
    costo = models.FloatField()

    class Meta:
        verbose_name_plural = "Plantas"