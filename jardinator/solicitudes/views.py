from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from solicitudes.forms import FormularioSolicitud


@login_required
def solicitar(request):
    if request.method == "POST":
        form = FormularioSolicitud(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario = request.user
            solicitud.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        form = FormularioSolicitud()
    return render(request, "solicitudes/formulario.html", {"formulario_solicitudes": form})