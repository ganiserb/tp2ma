# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from solicitudes.models import Solicitud


class FormularioSolicitud(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FormularioSolicitud, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Enviar solicitud'))

    class Meta:
        model = Solicitud
        fields = ['texto', 'tipo']
        widgets = {
            'texto': forms.Textarea()
        }

