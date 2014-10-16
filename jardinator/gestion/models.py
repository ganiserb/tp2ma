from django.db import models
from django.core.validators import MaxValueValidator
from utilidades.models import Ciudad
from clientes.models import Jardin


class Empleado(models.Model):
    """ABM empleados."""
    hs_jornada_choices = tuple(
        [(hora, str(hora)) for hora in range(1, 9)]
    )

    apellido = models.CharField(max_length=250)
    nombre = models.CharField(max_length=250)
    dni = models.CharField(max_length=25)
    telefono = models.CharField(max_length=25)
    ciudad = Ciudad
    foto = models.ImageField(upload_to="fotos_empleados", blank=True)
    #jornada es cuántas horas trabaja por día
    jornada = models.IntegerField(choices=hs_jornada_choices,
                            default=8)
    sueldo_basico = models.FloatField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.apellido + ', ' + self.nombre

    class Meta:
        verbose_name_plural = "Empleados"


class Contrato(models.Model):
    """ABM contratos."""
    ejemplo = 'e'
    tipo_tarifa_choices = (
        (ejemplo, 'ejemplo'),
    )

    jardin = models.ForeignKey(Jardin)
    fecha_inicio = models.DateTimeField()
    fecha_fin_estimada = models.DateTimeField(null=True, blank=True)
    fecha_fin_real = models.DateTimeField(null=True, blank=True)
    tipo_tarifa = models.CharField(max_length=2,
                            choices=tipo_tarifa_choices,
                            default=ejemplo)

    def __str__(self):
        return self.jardin.nombre + ' (' + self.fecha_inicio.strftime(
            '%x %X') + ')'

    class Meta:
        verbose_name_plural = "Contratos"


class Tarea(models.Model):
    """ABM tareas."""
    contrato = models.ForeignKey(Contrato)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tareas"


class Log(models.Model):
    """ABM log de tareas."""
    horas = models.IntegerField(validators=[MaxValueValidator(16)])
    empleado = models.ForeignKey(Empleado)
    tarea = models.ForeignKey(Tarea)

    def __str__(self):
        return self.empleado.apellido + ', ' + self.empleado.nombre + ' (' + self.tarea.nombre + ')'

    class Meta:
        verbose_name_plural = "Log de tareas"