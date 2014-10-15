from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from publicidades.models import Publicidad


@login_required
def vista_publicidades(request):
    """vista equipos no devueltos."""
    publicidades = Publicidad.objects.all()

    return render(request, 'publicidades/lista.html',
                    {'publicidades': publicidades})
