from django.db import models


class Unidad(models.Model):
    """Modelo unidad."""
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Unidades de medida"


class Material(models.Model):
    """Modelo insumos y accesorios."""
    descripcion = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    unidad = models.ForeignKey(Unidad)
    costo = models.FloatField()

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Materiales de trabajo"


class Familia(models.Model):
    """Modelo familia"""
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Familias de plantas"


class Planta(models.Model):
    """Modelo plantas."""
    nombre = models.CharField(max_length=150)
    foto = models.ImageField(upload_to="imagenes_inventarios")

    CADUCA = 'ca'
    PERENNE = 'pe'

    TIPO_HOJA_CHOICES = (
        (CADUCA, 'Caduca'),
        (PERENNE, 'Perenne')
    )

    tipo_hoja = models.CharField(max_length=2,
                            choices=TIPO_HOJA_CHOICES,
                            default=CADUCA)

    tipo_flor = models.CharField(max_length=150, blank=True)
    fecha_inicio_temporada_plantacion = models.DateField(null=True, blank=True)
    fecha_fin_temporada_plantacion = models.DateField(null=True, blank=True)
    fecha_inicio_temporada_floracion = models.DateField(null=True, blank=True)
    fecha_fin_temporada_floracion = models.DateField(null=True, blank=True)
    familia = models.ForeignKey(Familia)
    origen = models.CharField(max_length=150)
    costo = models.FloatField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Plantas"