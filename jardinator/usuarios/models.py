from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    nombre = models.CharField(max_length=25, blank=True)

    EMPRESA = 'em'
    PERSONA = 'pe'

    TIPO_PERSONA_CHOICES = (
        (EMPRESA, 'Empresa'),
        (PERSONA, 'Persona física')
    )

    tipo = models.CharField(max_length=2,
                            choices=TIPO_PERSONA_CHOICES,
                            default=EMPRESA)