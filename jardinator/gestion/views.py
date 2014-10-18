from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from gestion.models import Log, Empleado
from datetime import datetime


@login_required
def listar_pago_empleados(request):
    if request.user.is_staff:
        # De los logs, obtener todos los del mes actual
        logs_mes_actual = Log.objects.filter(fecha__month=datetime.now().month)
        detalle_sueldos = Empleado.objects.filter(id__in=logs_mes_actual)\
                                          .annotate(horas=Sum('log__horas'))

        return render(request,
                      'gestion/listado_pago_empleados.html',
                      {'detalle_sueldos': detalle_sueldos}
        )
    else:
        return HttpResponseRedirect('home')
