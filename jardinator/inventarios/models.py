from django.db import models


class Unidad(models.Model):
    """Modelo unidad."""
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Unidades de medida"


class Insumo(models.Model):
    """Insumos y accesorios."""
    descripcion = models.CharField(max_length=150)
    unidad = models.ForeignKey(Unidad)
    costo = models.FloatField()

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Insumos de trabajo"


class StockInsumos(models.Model):
    insumo = models.OneToOneField(Insumo)
    cantidad = models.PositiveIntegerField()


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