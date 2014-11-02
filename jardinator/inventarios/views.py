from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from inventarios.models import Planta


def vista_plantas(request):
    """vista equipos no devueltos."""
    plantas = Planta.objects.all()

    return render(request, 'inventarios/lista.html',
                    {'plantas': plantas})
