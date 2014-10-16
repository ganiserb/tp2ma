from django.db import models


class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
