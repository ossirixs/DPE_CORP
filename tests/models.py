from django.db import models
from django import forms


class CIE_form(forms.Form):
    OPCIONES = ((0, "Falso"), (1, "Cierto"))

    q_1 = forms.ChoiceField(
        label='Hay muchas cosas que me hacen enojar.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_2 = forms.ChoiceField(
        label='Actualmente vivo momentos malos, tensos o de inquietud.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_3 = forms.ChoiceField(
        label='Hago un gran esfuerzo por demostrar que tengo razón, aún cuando tenga que luchar para lograrlo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
