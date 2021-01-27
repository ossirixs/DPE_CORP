from django.db import models
from company.models import TestCode


class ObjectCIE(models.Model):
    # El código de la prueba al que está relacionado este cuestionario
    codigo = models.ForeignKey(TestCode, blank=True, null=True, on_delete=models.CASCADE)
    # Datos del candidato
    nombre = models.CharField(max_length=50, default='', help_text='Nombre completo del candidato')
    edad = models.IntegerField(default=1, help_text='Edad del candidato')
    profesion = models.CharField(max_length=50, default='', help_text='Profesion del candidato')
    sexo = models.CharField(max_length=50, default='', help_text='Sexo del candidato')
    estado = models.CharField(max_length=50, default='', help_text='Estado de nacimiento del candidato')
    rfc = models.CharField(max_length=50, default='', help_text='RFC del candidato')
    # Preguntas del cuestionario
    q_1 = models.BooleanField(null=True)
    q_2 = models.BooleanField(null=True)
    q_3 = models.BooleanField(null=True)
    q_4 = models.BooleanField(null=True)
    q_5 = models.BooleanField(null=True)
    q_6 = models.BooleanField(null=True)
    q_7 = models.BooleanField(null=True)
    q_8 = models.BooleanField(null=True)
    q_9 = models.BooleanField(null=True)
    q_10 = models.BooleanField(null=True)
    q_11 = models.BooleanField(null=True)
    q_12 = models.BooleanField(null=True)
    q_13 = models.BooleanField(null=True)
    q_14 = models.BooleanField(null=True)
    q_15 = models.BooleanField(null=True)
    q_16 = models.BooleanField(null=True)
    q_17 = models.BooleanField(null=True)
    q_18 = models.BooleanField(null=True)
    q_19 = models.BooleanField(null=True)
    q_20 = models.BooleanField(null=True)
    q_21 = models.BooleanField(null=True)
    q_22 = models.BooleanField(null=True)
    q_23 = models.BooleanField(null=True)
    q_24 = models.BooleanField(null=True)
    q_25 = models.BooleanField(null=True)
    q_26 = models.BooleanField(null=True)
    q_27 = models.BooleanField(null=True)
    q_28 = models.BooleanField(null=True)
    q_29 = models.BooleanField(null=True)
    q_30 = models.BooleanField(null=True)
    q_31 = models.BooleanField(null=True)
    q_32 = models.BooleanField(null=True)
    q_33 = models.BooleanField(null=True)
    q_34 = models.BooleanField(null=True)
    q_35 = models.BooleanField(null=True)
    q_36 = models.BooleanField(null=True)
    q_37 = models.BooleanField(null=True)
    q_38 = models.BooleanField(null=True)
    q_39 = models.BooleanField(null=True)
    q_40 = models.BooleanField(null=True)
    q_41 = models.BooleanField(null=True)

