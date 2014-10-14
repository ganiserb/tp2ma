from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from usuarios.forms import FormCreacionUsuario


def registro(request):
    """
    Muestra y procesa el formulario de registro
    """
    if request.method == 'POST':
        form_registro = FormCreacionUsuario(request.POST)
        if form_registro.is_valid():
            form_registro.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form_registro = FormCreacionUsuario()

    return render(request,
                  'usuarios/registro.html',
                  {'form_registro': form_registro})