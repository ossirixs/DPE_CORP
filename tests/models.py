from django.db import models
from django import forms


class CIE_form(forms.Form):
    OPCIONES = ((0, "Falso"), (1, "Cierto"))

    q_1 = forms.ChoiceField(
        label='Hay muchas cosas que me hacen enojar.',
        required=True, widget=forms.RadioSelect(attrs={'id':'1'}), choices=OPCIONES)
    q_2 = forms.ChoiceField(
        label='Actualmente vivo momentos malos, tensos o de inquietud.',
        required=True, widget=forms.RadioSelect(attrs={'id':'2'}), choices=OPCIONES)
    q_3 = forms.ChoiceField(
        label='Hago un gran esfuerzo por demostrar que tengo razón, aún cuando tenga que luchar para lograrlo.',
        required=True, widget=forms.RadioSelect(attrs={'id':'3'}), choices=OPCIONES)
    q_4 = forms.ChoiceField(
        label='Tengo mala suerte y a eso se debe que me sucedan muchas de las cosas que me pasan.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_5 = forms.ChoiceField(
        label='Me gusta ir a reuniones y fiestas donde hay mucha gente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_6 = forms.ChoiceField(
        label='Actúo con diplomacia y tengo tacto al decir lo que pienso.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_7 = forms.ChoiceField(
        label='Me gusta buscar el aplauso y la alabanza de los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_8 = forms.ChoiceField(
        label='Suelo hablar alto cuando siento enojo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_9 = forms.ChoiceField(
        label='Sí soy una persona formal y responsable, sin duda alguna.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_10 = forms.ChoiceField(
        label='Mi escala de valores e intereses cambia fácilmente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_11 = forms.ChoiceField(
        label='Antes de hacer las cosas por lo general tiendo a dudar bastante como hacerlas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_12 = forms.ChoiceField(
        label='Abandono fácilmente mis obligaciones.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_13 = forms.ChoiceField(
        label='Comunico con facilidad mis alegrías y tristezas a los demás y me encanta hacerlo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_14 = forms.ChoiceField(
        label='Me considero una persona estricta en el seguimiento de las normas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_15 = forms.ChoiceField(
        label='La gente puede, sin duda, confiar en mi.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_16 = forms.ChoiceField(
        label='Evito las discusiones que llevan a nada.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_17 = forms.ChoiceField(
        label='Siempre intento proyectar una buena imagen de mi.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_18 = forms.ChoiceField(
        label=' Mi estado de ánimo puede cambiar fácilmente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_19 = forms.ChoiceField(
        label='Actualmente vivo un poco estresado.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_20 = forms.ChoiceField(
        label='Soy una persona muy trabajadora y eficiente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)



class ObjectCIE(models.Model):

    q_1 = models.BooleanField()
    q_2 = models.BooleanField()
    q_3 = models.BooleanField()
    q_4 = models.BooleanField()
    q_5 = models.BooleanField()
    q_6 = models.BooleanField()
    q_7 = models.BooleanField()
    q_8 = models.BooleanField()
    q_9 = models.BooleanField()
    q_10 = models.BooleanField()
    q_11 = models.BooleanField()
    q_12 = models.BooleanField()
    q_13 = models.BooleanField()
    q_14 = models.BooleanField()
    q_15 = models.BooleanField()
    q_16 = models.BooleanField()
    q_17 = models.BooleanField()
    q_18 = models.BooleanField()
    q_19 = models.BooleanField()
    q_20 = models.BooleanField()



class TestCatalog(models.Model):
    """ Catalog for Tests. """

    TEST_TYPE = [
        ('CIE', 'CIE'),
        ('DPECON' , 'DPECon'),
    ]

    test_name = models.CharField( max_length=128, choices=TEST_TYPE, null=False, blank=False)
    active = models.BooleanField( null=False, blank=False, default=True)

