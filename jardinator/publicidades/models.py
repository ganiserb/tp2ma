from django.db import models


class Publicidad(models.Model):
    """ABM publicidades."""
    titulo = models.CharField(max_length=250)
    texto = models.CharField(max_length=250)
    foto = models.ImageField(upload_to="imagenes_publicidades")
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Publicidades"