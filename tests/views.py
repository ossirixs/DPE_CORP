# Django
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
import tempfile
# Models
from tests.models import ObjectCIE, ObjectIntegrity, ObjectMax, MaxPositions
from company.models import TestCode
# Libraries
from formtools.wizard.views import SessionWizardView
from django.shortcuts import get_object_or_404
from tests.utils import clean_data, score_tag_CIE
from weasyprint import HTML
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.http import HttpResponse
# Utils
from tests.utils import *
from users.utils import check_code
# Forms
from tests.forms import *


class CIE(SessionWizardView):
    form_list = [candidato,
                 CIE_form_1,
                 CIE_form_2,
                 CIE_form_3,
                 CIE_form_4,
                 CIE_form_5,
                 CIE_form_6,
                 CIE_form_7,
                 CIE_form_8,
                 CIE_form_9,
                 CIE_form_10,
                 CIE_form_11,
                 CIE_form_12,]

    def get_template_names(self):
        return 'test.html'

    def done(self, form_list, **kwargs):
        code = kwargs['test_code']
        test_code = TestCode.objects.get(code=code)
        cuestionario = ObjectCIE()

        for form in form_list:
            form_data = form.cleaned_data
            for key, value in form_data.items():
                setattr(cuestionario, key, value)
                # print(key, value)
        cuestionario.codigo = test_code
        cuestionario.save()
        return render(self.request, 'finish.html', dict(form_data = [form.cleaned_data for form in form_list],
                                                        title = 'CIE',
                                                        name = cuestionario.nombre))

def test_result(request, test_type, test_id):

    cuestionario = get_object_or_404(ObjectCIE, pk=test_id)

    try:
        q_1 = cuestionario.q_1
        q_2 = cuestionario.q_2
        q_3 = cuestionario.q_3
        q_4 = cuestionario.q_4
        q_5 = cuestionario.q_5
        q_6 = cuestionario.q_6
        q_7 = cuestionario.q_7
        q_8 = cuestionario.q_8
        q_9 = cuestionario.q_9
        q_10 = cuestionario.q_10
        q_11 = cuestionario.q_11
        q_12 = cuestionario.q_12
        q_13 = cuestionario.q_13
        q_14 = cuestionario.q_14
        q_15 = cuestionario.q_15
        q_16 = cuestionario.q_16
        q_17 = cuestionario.q_17
        q_18 = cuestionario.q_18
        q_19 = cuestionario.q_19
        q_20 = cuestionario.q_20
        q_21 = cuestionario.q_21
        q_22 = cuestionario.q_22
        q_23 = cuestionario.q_23
        q_24 = cuestionario.q_24
        q_25 = cuestionario.q_25
        q_26 = cuestionario.q_26
        q_27 = cuestionario.q_27
        q_28 = cuestionario.q_28
        q_29 = cuestionario.q_29
        q_30 = cuestionario.q_30
        q_31 = cuestionario.q_31
        q_32 = cuestionario.q_32
        q_33 = cuestionario.q_33
        q_34 = cuestionario.q_34
        q_35 = cuestionario.q_35
        q_36 = cuestionario.q_36
        q_37 = cuestionario.q_37
        q_38 = cuestionario.q_38
        q_39 = cuestionario.q_39
        q_40 = cuestionario.q_40
        q_41 = cuestionario.q_41
        q_42 = cuestionario.q_42
        q_43 = cuestionario.q_43
        q_44 = cuestionario.q_44
        q_45 = cuestionario.q_45
        q_46 = cuestionario.q_46
        q_47 = cuestionario.q_47
        q_48 = cuestionario.q_48
        q_49 = cuestionario.q_49
        q_50 = cuestionario.q_50
        q_51 = cuestionario.q_51
        q_52 = cuestionario.q_52
        q_53 = cuestionario.q_53
        q_54 = cuestionario.q_54
        q_55 = cuestionario.q_55
        q_56 = cuestionario.q_56
        q_57 = cuestionario.q_57
        q_58 = cuestionario.q_58
        q_59 = cuestionario.q_59
        q_60 = cuestionario.q_60
        q_61 = cuestionario.q_61
        q_62 = cuestionario.q_62
        q_63 = cuestionario.q_63
        q_64 = cuestionario.q_64
        q_65 = cuestionario.q_65
        q_66 = cuestionario.q_66
        q_67 = cuestionario.q_67
        q_68 = cuestionario.q_68
        q_69 = cuestionario.q_69
        q_70 = cuestionario.q_70
        q_71 = cuestionario.q_71
        q_72 = cuestionario.q_72
        q_73 = cuestionario.q_73
        q_74 = cuestionario.q_74
        q_75 = cuestionario.q_75
        q_76 = cuestionario.q_76
        q_77 = cuestionario.q_77
        q_78 = cuestionario.q_78
        q_79 = cuestionario.q_79
        q_80 = cuestionario.q_80
        q_81 = cuestionario.q_81
        q_82 = cuestionario.q_82
        q_83 = cuestionario.q_83
        q_84 = cuestionario.q_84
        q_85 = cuestionario.q_85
        q_86 = cuestionario.q_86
        q_87 = cuestionario.q_87
        q_88 = cuestionario.q_88
        q_89 = cuestionario.q_89
        q_90 = cuestionario.q_90
        q_91 = cuestionario.q_91
        q_92 = cuestionario.q_92
        q_93 = cuestionario.q_93
        q_94 = cuestionario.q_94
        q_95 = cuestionario.q_95
        q_96 = cuestionario.q_96
        q_97 = cuestionario.q_97
        q_98 = cuestionario.q_98
        q_99 = cuestionario.q_99
        q_100 = cuestionario.q_100
        q_101 = cuestionario.q_101
        q_102 = cuestionario.q_102
        q_103 = cuestionario.q_103
        q_104 = cuestionario.q_104
        q_105 = cuestionario.q_105
        q_106 = cuestionario.q_106
        q_107 = cuestionario.q_107
        q_108 = cuestionario.q_108
        q_109 = cuestionario.q_109
        q_110 = cuestionario.q_110
        q_111 = cuestionario.q_111
        q_112 = cuestionario.q_112
        q_113 = cuestionario.q_113
        q_114 = cuestionario.q_114
        q_115 = cuestionario.q_115
        q_116 = cuestionario.q_116
        q_117 = cuestionario.q_117
        q_118 = cuestionario.q_118
        q_119 = cuestionario.q_119
        q_120 = cuestionario.q_120
        q_121 = cuestionario.q_121
        q_122 = cuestionario.q_122
        q_123 = cuestionario.q_123
        q_124 = cuestionario.q_124
        q_125 = cuestionario.q_125
        q_126 = cuestionario.q_126
        q_127 = cuestionario.q_127
        q_128 = cuestionario.q_128
        q_129 = cuestionario.q_129
        q_130 = cuestionario.q_130
        q_131 = cuestionario.q_131
        q_132 = cuestionario.q_132
        q_133 = cuestionario.q_133
        q_134 = cuestionario.q_134
        q_135 = cuestionario.q_135
        q_136 = cuestionario.q_136
        q_137 = cuestionario.q_137
        q_138 = cuestionario.q_138
        q_139 = cuestionario.q_139
        q_140 = cuestionario.q_140
        q_141 = cuestionario.q_141
        q_142 = cuestionario.q_142
        q_143 = cuestionario.q_143
        q_144 = cuestionario.q_144
        q_145 = cuestionario.q_145
        q_146 = cuestionario.q_146
        q_147 = cuestionario.q_147
        q_148 = cuestionario.q_148
        q_149 = cuestionario.q_149
        q_150 = cuestionario.q_150
        q_151 = cuestionario.q_151
        q_152 = cuestionario.q_152
        q_153 = cuestionario.q_153
        q_154 = cuestionario.q_154
        q_155 = cuestionario.q_155
        q_156 = cuestionario.q_156
        q_157 = cuestionario.q_157
        q_158 = cuestionario.q_158
        q_159 = cuestionario.q_159
        q_160 = cuestionario.q_160
        q_161 = cuestionario.q_161
        q_162 = cuestionario.q_162
        q_163 = cuestionario.q_163
        q_164 = cuestionario.q_164
        q_165 = cuestionario.q_165
        q_166 = cuestionario.q_166
        q_167 = cuestionario.q_167
        q_168 = cuestionario.q_168
        q_169 = cuestionario.q_169
        q_170 = cuestionario.q_170
        q_171 = cuestionario.q_171
        q_172 = cuestionario.q_172
        q_173 = cuestionario.q_173
        q_174 = cuestionario.q_174
        q_175 = cuestionario.q_175
        q_176 = cuestionario.q_176
        q_177 = cuestionario.q_177
        q_178 = cuestionario.q_178
        q_179 = cuestionario.q_179
        q_180 = cuestionario.q_180
        q_181 = cuestionario.q_181
        q_182 = cuestionario.q_182
        q_183 = cuestionario.q_183
        q_184 = cuestionario.q_184
        q_185 = cuestionario.q_185
        q_186 = cuestionario.q_186
        q_187 = cuestionario.q_187
        q_188 = cuestionario.q_188
        q_189 = cuestionario.q_189
        q_190 = cuestionario.q_190
        q_191 = cuestionario.q_191
        q_192 = cuestionario.q_192
        q_193 = cuestionario.q_193
        q_194 = cuestionario.q_194
        q_195 = cuestionario.q_195
        q_196 = cuestionario.q_196
        q_197 = cuestionario.q_197
        q_198 = cuestionario.q_198
        q_199 = cuestionario.q_199
        q_200 = cuestionario.q_200
        q_201 = cuestionario.q_201
        q_202 = cuestionario.q_202
        q_203 = cuestionario.q_203
        q_204 = cuestionario.q_204
        q_205 = cuestionario.q_205
        q_206 = cuestionario.q_206
        q_207 = cuestionario.q_207
        q_208 = cuestionario.q_208
        q_209 = cuestionario.q_209
        q_210 = cuestionario.q_210
        q_211 = cuestionario.q_211
        q_212 = cuestionario.q_212
        q_213 = cuestionario.q_213
        q_214 = cuestionario.q_214
        q_215 = cuestionario.q_215
        q_216 = cuestionario.q_216
        q_217 = cuestionario.q_217
        q_218 = cuestionario.q_218
        q_219 = cuestionario.q_219
        q_220 = cuestionario.q_220
        q_221 = cuestionario.q_221
        q_222 = cuestionario.q_222
        q_223 = cuestionario.q_223
        q_224 = cuestionario.q_224
        q_225 = cuestionario.q_225
        q_226 = cuestionario.q_226
        q_227 = cuestionario.q_227
        q_228 = cuestionario.q_228
        q_229 = cuestionario.q_229
        q_230 = cuestionario.q_230
        q_231 = cuestionario.q_231
        q_232 = cuestionario.q_232
        q_233 = cuestionario.q_233

    except:
        pass

    EST_DICT = {'Alto': "Presenta estabilidad y ajuste emocional. Es un individuo sosegado, sereno y equilibrado, "
                        "que difícilmente mostrará impulsividad. De buen carácter, con ausencia de tensión y "
                        "preocupaciones.",
                'Medio': "Se trata de un individuo con control y estabilidad emocionales.",
                'Bajo': "Impulsiva, nerviosa e irritable, esta persona se sobreexcita ante las circunstancias que no "
                        "puede controlar. Es susceptible e irritable emocionalmente. Se altera fácilmente. "
                        "Manifiesta cambios de ánimo y mal humor.",
                '26': 97,
                '25': 87,
                '24': 83,
                '23': 76,
                '22': 67,
                '21': 63,
                '20': 58,
                '19': 55,
                '18': 50,
                '17': 48,
                '16': 42,
                '15': 40,
                '14': 37,
                '13': 33,
                '12': 29,
                '11': 24,
                '10': 24,
                '9': 17,
                '8': 17,
                '7': 15,
                '6': 12,
                '5': 9,
                '4': 3,
                '3': 3,
                '2': 3,
                '1': 3,
                '0': 3}

    ANS_DICT = {'Alto': "Presenta preocupación alta, por lo que se muestra irritable, nerviosa, impaciente e inquieta. "
                         "Le falta concentración y es susceptible de distracciones. Muestra miedos, temores y tensión.",
                'Medio': "Persona equilibrada, que no muestra reacciones ansiosas frente a las distintas situaciones.",
                'Bajo': "No muestra irritabilidad, perturbación ni impaciencia. Es una persona que se muestra relajada "
                        "y tranquila, con ausencia de tensión, miedos y conductas excéntricas.",
                '25': 97,
                '24': 97,
                '23': 97,
                '22': 97,
                '21': 91,
                '20': 85,
                '19': 83,
                '18': 76,
                '17': 71,
                '16': 71,
                '15': 67,
                '14': 60,
                '13': 58,
                '12': 55,
                '11': 52,
                '10': 48,
                '9': 45,
                '8': 42,
                '7': 40,
                '6': 37,
                '5': 33,
                '4': 29,
                '3': 24,
                '2': 17,
                '1': 9,
                '0': 3}

    AUC_DICT = {'Alto': "Con alta opinión de sí y elevada autoestima, esta persona tiene una buena autoimagen de sí. "
                        "Con alto sentimiento de valía de su imagen física, psíquica y social.",
                'Medio': "Posee una adecuada valoración personal y aceptación de su imagen física, psíquica y social. " \
                         "Con apropiado sentimiento de valía.",
                'Bajo': "Esta persona puede tener una pobre visión y aceptación de sí misma. Con sentimientos de "
                        "inferioridad y pobre autoimagen, depende de la estima de los demás. Es indecisa ante las "
                        "situaciones sociales.",
                '25': 97,
                '24': 87,
                '23': 76,
                '22': 71,
                '21': 63,
                '20': 55,
                '19': 50,
                '18': 45,
                '17': 40,
                '16': 37,
                '15': 33,
                '14': 29,
                '13': 24,
                '12': 24,
                '11': 17,
                '10': 15,
                '9': 12,
                '8': 9,
                '7': 9,
                '6': 3,
                '5': 3,
                '4': 3,
                '3': 3,
                '2': 3,
                '1': 3,
                '0': 3}

    EFI_DICT = {'Alto': "Es un individuo con iniciativas propias, que se lanza a la actividad con seguridad. "
                        "Acepta las responsabilidades confiado en sí mismo, siendo eficaz. Es competente, eficiente y emprendedor.",
                'Medio': "Es un sujeto con competencia y eficacia en la realización de distintas conductas interactivas.",
                'Bajo': "Evidencia poca confianza y seguridad en sí misma, por lo que duda de lo que hace y es insegura "
                        "ante las adversidades.",
                '25': 91,
                '24': 71,
                '23': 60,
                '22': 52,
                '21': 42,
                '20': 37,
                '19': 29,
                '18': 24,
                '17': 17,
                '16': 17,
                '15': 12,
                '14': 9,
                '13': 3,
                '12': 3,
                '11': 3,
                '10': 3,
                '9': 3,
                '8': 3,
                '7': 3,
                '6': 3,
                '5': 3,
                '4': 3,
                '3': 3,
                '2': 3,
                '1': 3,
                '0': 3}

    SEG_DICT = {'Alto': "Esta persona confía en sus posibilidades, por lo que está segura de lo que hace y de cómo lo hace.",
                'Medio': "Esta persona posee confianza en sus posibilidades y recursos propios, al mismo tiempo que "
                         "seguridad para enfrentarse a los acontecimientos de la vida.",
                'Bajo': "Al ser una persona de poca confianza, duda de lo que hace y es insegura ante las adversidades.",
                '24': 97,
                '23': 76,
                '22': 60,
                '21': 52,
                '20': 45,
                '19': 42,
                '18': 37,
                '17': 33,
                '16': 29,
                '15': 29,
                '14': 29,
                '13': 24,
                '12': 17,
                '11': 17,
                '10': 17,
                '9': 15,
                '8': 15,
                '7': 12,
                '6': 12,
                '5': 12,
                '4': 12,
                '3': 12,
                '2': 12,
                '1': 12,
                '0': 3}

    IND_DICT = {'Alto': "La persona muestra libertad de acción. Es independiente, autónoma y autosuficiente. "
                        "Por lo que les da primacía a sus intereses frente a los del grupo. Puede soslayar las "
                        "necesidades de los demás. Toma sus propias decisiones e iniciativas.",
                'Medio': "Este individuo actúa sin tener en cuenta las opiniones o puntos de vista de otras personas o del grupo.",
                'Bajo': "Depende de los demás, por lo que es una seguidora fiel, que busca apoyos de los otros. "
                        "Asimismo, intenta no desagradar, por lo que busca aprobación.",
                '19': 97,
                '18': 97,
                '17': 97,
                '16': 97,
                '15': 97,
                '14': 97,
                '13': 91,
                '12': 83,
                '11': 76,
                '10': 67,
                '9': 58,
                '8': 52,
                '7': 45,
                '6': 37,
                '5': 33,
                '4': 24,
                '3': 17,
                '2': 12,
                '1': 9,
                '0': 9}

    DOM_DICT = {'Alto': "Es enérgica, asertiva y activa. Le gusta organizar y mandar, siendo dominante. "
                        "Dirige al grupo y su trabajo. Con orientación al liderazgo, puede ser intolerante y agresiva,"
                        " pero competitiva e independiente.",
                'Medio': " Este individuo tiende a dirigir a los demás y a organizar actividades.",
                'Bajo': "Se trata de una persona que acepta órdenes y no fuerza las situaciones. "
                        "Intenta agradar a los demás, siendo dócil y obediente.",
                '24': 97,
                '23': 97,
                '22': 97,
                '21': 91,
                '20': 91,
                '19': 85,
                '18': 83,
                '17': 83,
                '16': 76,
                '15': 71,
                '14': 71,
                '13': 67,
                '12': 63,
                '11': 58,
                '10': 55,
                '9': 52,
                '8': 48,
                '7': 42,
                '6': 37,
                '5': 33,
                '4': 24,
                '3': 17,
                '2': 12,
                '1': 3,
                '0': 3}

    COG_DICT = {'Alto': "Al poseer buen control cognitivo, es una persona analítica y reflexiva, lo que le permite ser "
                        "precavida y organizada. Tiene control verbal y de sus acciones, pues primero analiza y luego "
                        "responde. Procura solucionar los problemas por sí misma.",
                'Medio': "Es un individuo con adecuado manejo de los procesos y habilidades de autocontrol verbal y en "
                         "sus respuestas ante distintas situaciones.",
                'Bajo': "Con pobre control cognitivo es un individuo de impulsividad verbal, que puede dar respuestas sin pensar.",
                '24': 97,
                '23': 76,
                '22': 63,
                '21': 50,
                '20': 42,
                '19': 33,
                '18': 29,
                '17': 24,
                '16': 17,
                '15': 12,
                '14': 9,
                '13': 3,
                '12': 3,
                '11': 3,
                '10': 3,
                '9': 3,
                '8': 3,
                '7': 3,
                '6': 3,
                '5': 3,
                '4': 3,
                '3': 3,
                '2': 3,
                '1': 3,
                '0': 3}

    SOC_DICT = {'Alto': "De carácter alegre y amigable, a este sujeto sociable, le resulta fácil ser abierto y espontáneo. "
                        "Es expresivo y comunicativo, con gusto y facilidad por las relaciones sociales. "
                        "Por su iniciativa social, participa en actividades en las que pueda estar y trabajar con gente.",
                'Medio': "Es un sujeto con facilidad para las relaciones sociales.",
                'Bajo': "No le gustan mucho las situaciones sociales, por lo que es inhibida, retraída, tímida y distante. "
                        "Es una persona reservada y poco comunicativa.",
                '25': 97,
                '24': 76,
                '23': 63,
                '22': 55,
                '21': 50,
                '20': 45,
                '19': 42,
                '18': 40,
                '17': 37,
                '16': 33,
                '15': 33,
                '14': 33,
                '13': 29,
                '12': 29,
                '11': 29,
                '10': 24,
                '9': 24,
                '8': 24,
                '7': 24,
                '6': 24,
                '5': 24,
                '4': 0,
                '3': 24,
                '2': 24,
                '1': 24,
                '0': 24}

    AJS_DICT = {'Alto': "Preocupada por las normas sociales, esta persona acepta y sigue bien las reglas y tradiciones. "
                        "Cumple las obligaciones, siendo conservadora y convencional.",
                'Medio': "Esta persona muestra una adecuada captación social o sociabilización al medio familiar, profesional o laboral.",
                'Bajo': "A esta persona le cuesta seguir las normas y reglas, pues tiende a despreciarlas, "
                        "lo mismo que las tradiciones. Al ser rebelde y no convencional, tiene bajo ajuste social, "
                        "por lo que suele aparecer a los demás como conflictiva e inadaptada.",
                '19': 97,
                '18': 97,
                '17': 76,
                '16': 60,
                '15': 52,
                '14': 42,
                '13': 37,
                '12': 29,
                '11': 29,
                '10': 24,
                '9': 17,
                '8': 17,
                '7': 17,
                '5': 17,
                '4': 15,
                '3': 15,
                '2': 15,
                '1': 15,
                '0': 3}

    AGR_DICT = {'Alto': "Al ser un individuo agresivo, belicoso y hostil, muestra intolerancia y se vuelve crítico a "
                        "las acciones de los demás. Dando respuestas inadecuadas ante las dificultades y frustraciones. "
                        "Discute e incluso puede llegar a insultar.",
                'Medio': "Esta persona ofrece un adecuado tipo de respuestas ante las dificultades y frustraciones que presenta la vida.",
                'Bajo': "Es un individuo tolerante, sociable, amable y comprensivo. Da respuestas adecuadas ante las "
                        "frustraciones y situaciones difíciles.",
                '21': 97,
                '20': 97,
                '19': 97,
                '18': 97,
                '17': 97,
                '16': 97,
                '15': 87,
                '14': 85,
                '13': 83,
                '12': 76,
                '11': 71,
                '10': 67,
                '9': 63,
                '8': 58,
                '7': 52,
                '6': 48,
                '5': 42,
                '4': 37,
                '3': 33,
                '2': 24,
                '1': 17,
                '0': 0}

    TOL_DICT = {'Alto': "Tolerante y comprensiva, es una persona con intereses amplios, liberal y sociable. Como tolera "
                        "las ideas de los demás, sabe vivir con los valores y creencias ajenas.",
                'Medio': "Es una persona con independencia de pensamiento y acción, respecto a la forma de ser y actuar "
                         "y a la procedencia de los demás.",
                'Bajo': "Es una persona inflexible e intransigente que actúa con rigidez e intolerancia. "
                        "Todo lo evalúa desde su propia perspectiva o valores. Le resulta difícil convivir con las "
                        "ideas y valores de los otros.",
                '19': 97,
                '18': 83,
                '17': 71,
                '16': 63,
                '15': 55,
                '14': 50,
                '13': 42,
                '12': 37,
                '11': 29,
                '10': 24,
                '9': 17,
                '8': 12,
                '7': 9,
                '6': 3,
                '5': 3,
                '4': 3,
                '3': 3,
                '2': 3,
                '1': 3,
                '0': 3}

    HAB_DICT = {'Alto': "Socialmente inteligente y hábil, este individuo sabe enfrentarse y adaptarse a las distintas "
                        "situaciones sociales con desenvoltura.",
                'Medio': "Este individuo posee capacidad para la adaptación inteligente a los distintos ambientes y "
                         "situaciones sociales, así como facilidad de actuación en los mismos.",
                'Bajo': "Individuo poco hábil socialmente y a veces torpe, lo cual le impide adaptarse adecuadamente a "
                        "los distintos ambientes, pues no usa bien las estrategias de conducta.",
                '20': 83,
                '19': 63,
                '18': 50,
                '17': 40,
                '16': 33,
                '15': 24,
                '14': 17,
                '13': 17,
                '12': 12,
                '11': 9,
                '10': 9,
                '9': 9,
                '8': 3,
                '7': 3,
                '6': 3,
                '5': 3,
                '4': 3,
                '3': 3,
                '2': 3,
                '1': 3,
                '0': 3}

    DISC_DICT = {'Alto': "Cumplidora, responsable, formal, seria y disciplinada, esta persona cumple con el deber que "
                         "asume y se adapta adecuadamente a las situaciones de trabajo.",
                 'Medio': "Tiene capacidad para actuar como una persona responsable, seria, cumplidora de su deber, "
                          "de sus obligaciones y de su trabajo.",
                 'Bajo': "Es una persona informal y poco responsable de sus deberes. Puede ser inadaptada al trabajo y "
                         "conflictiva, por lo que desdeña la disciplina o la puntualidad.",
                 '25': 97,
                 '24': 67,
                 '23': 48,
                 '22': 37,
                 '21': 29,
                 '20': 24,
                 '19': 24,
                 '18': 24,
                 '17': 24,
                 '16': 24,
                 '15': 24,
                 '14': 24,
                 '13': 24,
                 '12': 24,
                 '11': 24,
                 '10': 24,
                 '9': 24,
                 '8': 24,
                 '7': 24,
                 '6': 24,
                 '5': 24,
                 '4': 24,
                 '3': 24,
                 '2': 24,
                 '1': 24,
                 '0': 17}

    LID_DICT = {'Alto': "Le gusta mandar, dirigir y organizar. Se siente líder. Es autosuficiente, independiente y "
                        "dominante. Entusiasta y segura de sí misma, sabe dirigir y organizar actividades.",
                'Medio': "Tiene capacidad para dirigir grupos, asociaciones y equipos, organizar las actividades y el "
                         "trabajo de los demás y conseguir los objetivos y metas.",
                'Bajo': "Se muestra desinteresado por mandar o dirigir. No muestra garra ni transmite entusiasmo, "
                        "o los demás lo perciben así.",
                '19': 97,
                '18': 97,
                '17': 87,
                '16': 83,
                '15': 76,
                '14': 71,
                '13': 67,
                '12': 63,
                '11': 60,
                '10': 55,
                '9': 52,
                '8': 48,
                '7': 42,
                '6': 37,
                '5': 29,
                '4': 24,
                '3': 17,
                '2': 12,
                '1': 9,
                '0': 3}

    VER_DICT = {'Alto': "Se expresa libre de fingimiento. Es una persona veraz, sencilla y sincera.",
                'Medio': "Muestra libertad para expresarse sin fingimiento, reconociendo esas pequeñas debilidades "
                         "humanas referidas a sí misma para quedar bien consigo.",
                'Bajo': "Trata de esconder sus debilidades.",
                '21': 97,
                '20': 97,
                '19': 97,
                '18': 97,
                '17': 97,
                '16': 97,
                '15': 97,
                '14': 97,
                '13': 91,
                '12': 83,
                '11': 76,
                '10': 76,
                '9': 67,
                '8': 60,
                '7': 55,
                '6': 48,
                '5': 40,
                '4': 29,
                '3': 17,
                '2': 12,
                '1': 3,
                '0': 3}

    IMG_DICT = {'Alto': "Presenta mucho control de su imagen personal, por lo que se preocupa de dar una buena impresión.",
                'Medio': "Evitó distorsionar sus respuestas.",
                'Bajo': "Ofrece una adecuada imagen de sí misma.",
                '28': 76,
                '27': 58,
                '26': 48,
                '25': 40,
                '24': 37,
                '23': 29,
                '22': 24,
                '21': 24,
                '20': 17,
                '19': 17,
                '18': 15,
                '17': 12,
                '16': 9,
                '15': 3,
                '14': 3,
                '13': 3,
                '12': 3,
                '11': 3,
                '10': 3,
                '9': 3,
                '8': 3,
                '7': 3,
                '6': 3,
                '5': 3,
                '4': 3,
                '3': 3,
                '2': 3,
                '1': 3,
                '0': 3}

    CONG_DICT = {'Alto': "Buena coherencia entre las respuestas dadas por la evaluada o evaluado.",
                 'Medio': "Existe coherencia en las respuestas ofrecidas por la evaluada o evaluado.",
                 'Bajo': "Dudosa fiabilidad de las respuestas dadas por la evaluada o evaluado.",
                 '13': 97,
                 '12': 97,
                 '11': 76,
                 '10': 58,
                 '9': 45,
                 '8': 37,
                 '7': 29,
                 '6': 29,
                 '5': 24,
                 '4': 24,
                 '3': 24,
                 '2': 24,
                 '1': 17,
                 '0': 15}

    EST_true = [q_144, q_188]
    EST_false = [q_1, q_8, q_18, q_26, q_47, q_57, q_68, q_70, q_79, q_91, q_104, q_105, q_125, q_130, q_154, q_167,
                 q_170, q_186, q_190, q_202, q_203, q_215, q_221, q_230]

    ANS_true = [q_2, q_19, q_27, q_38, q_48, q_58, q_69, q_80, q_91, q_92, q_103, q_105, q_118, q_131, q_143, q_148,
                q_154, q_170, q_180, q_189, q_191, q_203, q_216, q_222]
    ANS_false = [q_144]

    AUC_true = [q_39, q_49, q_50, q_53, q_67, q_93, q_106, q_152, q_165, q_177, q_181, q_192, q_223]
    AUC_false = [q_59, q_70, q_104, q_119, q_120, q_156, q_157, q_169, q_182, q_204, q_221]

    EFI_true = [q_9, q_20, q_49, q_60, q_66, q_71, q_81, q_93, q_106, q_121, q_152, q_163, q_165, q_176, q_181, q_200,
                q_127]
    EFI_false = [q_11, q_12, q_36, q_42, q_136, q_204, q_208, q_220]

    SEG_true = [q_50, q_82, q_106, q_115, q_158, q_192, q_200]
    SEG_false = [q_28, q_42, q_68, q_70, q_91, q_104, q_116, q_120, q_132, q_134, q_136, q_156, q_157, q_175, q_182,
                 q_204, q_221]

    IND_true = [q_40, q_71, q_86, q_94, q_95, q_107, q_113, q_139, q_140, q_158, q_224]
    IND_false = [q_30, q_108, q_134, q_145, q_147, q_151, q_187, q_205]

    DOM_true = [q_3, q_31, q_37, q_52, q_53, q_61, q_67, q_72, q_82, q_96, q_101, q_109, q_113, q_121, q_126, q_135,
                q_172, q_177, q_183, q_195, q_225, q_229]
    DOM_false = [q_147]

    COG_true = [q_6, q_32, q_83, q_84, q_97, q_102, q_107, q_115, q_127, q_188, q_190, q_201, q_213, q_226, q_227]
    COG_false = [q_4, q_92, q_123, q_136, q_148, q_175, q_184, q_198, q_204]

    SOC_true = [q_5, q_13, q_22, q_33, q_43, q_74, q_85, q_124, q_137, q_149, q_161, q_185, q_196, q_209]
    SOC_false = [q_23, q_29, q_41, q_62, q_89, q_98, q_111, q_117, q_141, q_146, q_232]

    AJS_true = [q_14, q_24, q_35, q_65, q_75, q_124, q_137, q_151, q_171, q_187, q_218]
    AJS_false = [q_64, q_87, q_94, q_100, q_140, q_159, q_166, q_190]

    AGR_true = [q_44, q_54, q_63, q_86, q_99, q_109, q_112, q_128, q_138, q_150, q_159, q_160, q_162, q_174, q_186,
                q_195, q_197, q_199, q_207, q_210, q_219]
    AGR_false = []

    TOL_true = [q_110, q_192, q_194]
    TOL_false = [q_34, q_37, q_88, q_109, q_114, q_122, q_128, q_133, q_138, q_150, q_164, q_193, q_195, q_207, q_211,
                 q_219]

    HAB_true = [q_6, q_16, q_55, q_66, q_83, q_84, q_97, q_102, q_115, q_127, q_165, q_188, q_200, q_201, q_213, q_227]
    HAB_false = [q_59, q_89, q_123, q_208]

    DISC_true = [q_9, q_15, q_45, q_60, q_65, q_73, q_75, q_76, q_78, q_163, q_171, q_173, q_176, q_201, q_206, q_218]
    DISC_false = [q_10, q_12, q_36, q_51, q_87, q_168, q_179, q_212, q_220]

    LID_true = [q_3, q_21, q_31, q_37, q_39, q_50, q_52, q_53, q_61, q_67, q_72, q_121, q_126, q_135, q_177, q_181, q_200,
                q_225, q_229]
    LID_false = []

    VER_true = [q_7, q_17, q_25, q_37, q_46, q_55, q_56, q_77, q_90, q_116, q_119, q_129, q_142, q_145, q_153, q_155,
                q_178, q_214, q_228, q_231, q_233]
    VER_false = []

    IMG_true = [q_14, q_20, q_50, q_102, q_106, q_165, q_176]
    IMG_false = [q_1, q_36, q_96, q_104, q_128, q_136, q_140, q_148, q_162, q_164, q_171, q_172, q_175, q_183, q_186,
                  q_202, q_204, q_215, q_220, q_221, q_228]

    EST = 0
    ANS = 0
    AUC = 0
    EFI = 0
    SEG = 0
    IND = 0
    DOM = 0
    COG = 0
    SOC = 0
    AJS = 0
    AGR = 0
    TOL = 0
    HAB = 0
    DISC = 0
    LID = 0
    VER = 0
    IMG = 0
    CONG = 0

    for pregunta in EST_true:
        EST += clean_data(pregunta, invert=0)
    for pregunta in EST_false:
        EST += clean_data(pregunta, invert=1)
    score = EST_DICT.get(f'{EST}')
    result = score_tag_CIE(score)
    description = EST_DICT.get(f'{result}')
    EST = {'score': score, 'result': result, 'description': description}

    for pregunta in ANS_true:
        ANS += clean_data(pregunta, invert=0)
    for pregunta in ANS_false:
        ANS += clean_data(pregunta, invert=1)
    score = ANS_DICT.get(f'{ANS}')
    result = score_tag_CIE(score)
    description = ANS_DICT.get(f'{result}')
    ANS = {'score': score, 'result': result, 'description': description}

    for pregunta in AUC_true:
        AUC += clean_data(pregunta, invert=0)
    for pregunta in AUC_false:
        AUC += clean_data(pregunta, invert=1)
    score = AUC_DICT.get(f'{AUC}')
    result = score_tag_CIE(score)
    description = AUC_DICT.get(f'{result}')
    AUC = {'score': score, 'result': result, 'description': description}

    for pregunta in EFI_true:
        EFI += clean_data(pregunta, invert=0)
    for pregunta in EFI_false:
        EFI += clean_data(pregunta, invert=1)
    score = EFI_DICT.get(f'{EFI}')
    result = score_tag_CIE(score)
    description = EFI_DICT.get(f'{result}')
    EFI = {'score': score, 'result': result, 'description': description}

    for pregunta in SEG_true:
        SEG += clean_data(pregunta, invert=0)
    for pregunta in SEG_false:
        SEG += clean_data(pregunta, invert=1)
    score = SEG_DICT.get(f'{SEG}')
    result = score_tag_CIE(score)
    description = SEG_DICT.get(f'{result}')
    SEG = {'score': score, 'result': result, 'description': description}

    for pregunta in IND_true:
        IND += clean_data(pregunta, invert=0)
    for pregunta in IND_false:
        IND += clean_data(pregunta, invert=1)
    score = IND_DICT.get(f'{IND}')
    result = score_tag_CIE(score)
    description = IND_DICT.get(f'{result}')
    IND = {'score': score, 'result': result, 'description': description}

    for pregunta in DOM_true:
        DOM += clean_data(pregunta, invert=0)
    for pregunta in DOM_false:
        DOM += clean_data(pregunta, invert=1)
    score = DOM_DICT.get(f'{DOM}')
    result = score_tag_CIE(score)
    description = DOM_DICT.get(f'{result}')
    DOM = {'score': score, 'result': result, 'description': description}

    for pregunta in COG_true:
        COG += clean_data(pregunta, invert=0)
    for pregunta in COG_false:
        COG += clean_data(pregunta, invert=1)
    score = COG_DICT.get(f'{COG}')
    result = score_tag_CIE(score)
    description = COG_DICT.get(f'{result}')
    COG = {'score': score, 'result': result, 'description': description}

    for pregunta in SOC_true:
        SOC += clean_data(pregunta, invert=0)
    for pregunta in SOC_false:
        SOC += clean_data(pregunta, invert=1)
    score = SOC_DICT.get(f'{SOC}')
    result = score_tag_CIE(score)
    description = SOC_DICT.get(f'{result}')
    SOC = {'score': score, 'result': result, 'description': description}

    for pregunta in AJS_true:
        AJS += clean_data(pregunta, invert=0)
    for pregunta in AJS_false:
        AJS += clean_data(pregunta, invert=1)
    score = AJS_DICT.get(f'{AJS}')
    result = score_tag_CIE(score)
    description = AJS_DICT.get(f'{result}')
    AJS = {'score': score, 'result': result, 'description': description}

    for pregunta in AGR_true:
        AGR += clean_data(pregunta, invert=0)
    for pregunta in AGR_false:
        AGR += clean_data(pregunta, invert=1)
    score = AGR_DICT.get(f'{AGR}')
    result = score_tag_CIE(score)
    description = AGR_DICT.get(f'{result}')
    AGR = {'score': score, 'result': result, 'description': description}

    for pregunta in TOL_true:
        TOL += clean_data(pregunta, invert=0)
    for pregunta in TOL_false:
        TOL += clean_data(pregunta, invert=1)
    score = TOL_DICT.get(f'{TOL}')
    result = score_tag_CIE(score)
    description = TOL_DICT.get(f'{result}')
    TOL = {'score': score, 'result': result, 'description': description}

    for pregunta in HAB_true:
        HAB += clean_data(pregunta, invert=0)
    for pregunta in HAB_false:
        HAB += clean_data(pregunta, invert=1)
    score = HAB_DICT.get(f'{HAB}')
    result = score_tag_CIE(score)
    description = HAB_DICT.get(f'{result}')
    HAB = {'score': score, 'result': result, 'description': description}

    for pregunta in DISC_true:
        DISC += clean_data(pregunta, invert=0)
    for pregunta in DISC_false:
        DISC += clean_data(pregunta, invert=1)
    score = DISC_DICT.get(f'{DISC}')
    result = score_tag_CIE(score)
    description = DISC_DICT.get(f'{result}')
    DISC = {'score': score, 'result': result, 'description': description}

    for pregunta in LID_true:
        LID += clean_data(pregunta, invert=0)
    for pregunta in LID_false:
        LID += clean_data(pregunta, invert=1)
    score = LID_DICT.get(f'{LID}')
    result = score_tag_CIE(score)
    description = LID_DICT.get(f'{result}')
    LID = {'score': score, 'result': result, 'description': description}

    for pregunta in VER_true:
        VER += clean_data(pregunta, invert=0)
    for pregunta in VER_false:
        VER += clean_data(pregunta, invert=1)
    score = VER_DICT.get(f'{VER}')
    result = score_tag_CIE(score)
    description = VER_DICT.get(f'{result}')
    VER = {'score': score, 'result': result, 'description': description}

    for pregunta in IMG_true:
        IMG += clean_data(pregunta, invert=0)
    for pregunta in IMG_false:
        IMG += clean_data(pregunta, invert=1)
    score = IMG_DICT.get(f'{IMG}')
    result = score_tag_CIE(score)
    description = IMG_DICT.get(f'{result}')
    IMG = {'score': score, 'result': result, 'description': description}

    CONG = ((bool(q_6) and bool(q_200)) + (bool(q_9) and bool(q_65)) + (bool(q_23) and bool(q_41)) +
            (bool(q_76) and bool(q_206)) + (bool(q_90) and bool(q_214)) + (bool(q_93) and bool(q_106)) +
            (bool(q_94) and bool(q_140)) + (bool(q_102) and bool(q_127)) + (bool(q_136) and bool(q_204)) +
            (bool(q_156) and bool(q_221)) + (bool(q_194) and bool(q_205)))
    score = CONG_DICT.get(f'{CONG}')
    result = score_tag_CIE(score)
    description = CONG_DICT.get(f'{result}')
    CONG = {'score': score, 'result': result, 'description': description}


    print(CONG)

    context = dict(cuestionario=cuestionario,
                   pdf='',
                   EST=EST,
                   ANS=ANS,
                   AUC=AUC,
                   EFI=EFI,
                   SEG=SEG,
                   IND=IND,
                   DOM=DOM,
                   COG=COG,
                   SOC=SOC,
                   AJS=AJS,
                   AGR=AGR,
                   TOL=TOL,
                   HAB=HAB,
                   DISC=DISC,
                   LID=LID,
                   VER=VER,
                   IMG=IMG,
                   CONG=CONG)

    if 'export_button' in request.POST:

        html_template = get_template('test_result.html')
        context['pdf'] = True
        print(context)
        html = html_template.render(context)
        pdf_file = HTML(string=html).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="TEST"'

        # Return the response to preview the PDF in a new tab
        return response

    return render(request, 'test_result.html', context)

def cie_instructions(request, test_code):
    if request.method == 'GET':
        if TestCode.objects.filter(code=test_code).exists():
            test_code_object = TestCode.objects.get(code=test_code)
            # Check if code is valid
            code_errors = check_code(test_code_object)
            if code_errors == None:
                return render(request,'cie_instructions.html',{'code': test_code})
        return redirect('login')

    else:
        start = request.POST.get('start', False)
        if start:
            return redirect('cie_test',test_code=test_code)
        return render(request,'cie_instructions.html',{'code': test_code})

def integrity_instructions(request, test_code):
    if request.method == 'GET':
        if TestCode.objects.filter(code=test_code).exists():
            test_code_object = TestCode.objects.get(code=test_code)
            # Check if code is valid
            code_errors = check_code(test_code_object)
            if code_errors == None:
                return render(request,'integrity/integrity_instructions.html',{'test_code_object':test_code_object})
        return redirect('login')

    else:
        start_test = request.POST.get('start_test', False)
        if start_test:
            return redirect('integrity_test',test_code=test_code)
        return redirect('login')


def integrity_test(request, test_code):

    # Dictionary with all forms
    test_steps = {
        0: 'integrity_test_0.html',
        1: 'integrity_test_1.html',
        2: 'integrity_test_2.html',
        3: 'integrity_test_3.html',
        4: 'integrity_test_4.html',
        5: 'integrity_test_5.html',
        6: 'integrity_test_6.html',
        7: 'integrity_test_7.html',
        8: 'integrity_test_8.html',
        9: 'integrity_test_9.html',
        10: 'integrity_test_10.html',
        11: 'integrity_test_11.html',
        12: 'integrity_test_12.html',
        13: 'integrity_test_13.html',
        14: 'integrity_test_14.html',
        15: 'integrity_test_15.html',
        16: 'integrity_test_16.html',
        17: 'integrity_test_17.html',
        18: 'integrity_test_18.html',
        19: 'integrity_test_19.html',
        20: 'integrity_test_20.html',
    }

    # Display the candidate's info form
    if request.method == 'GET':
        test_template = 'integrity/'+str(test_steps.get(0))
        return render(request, test_template, {'form': candidato})

    # Start saving all the forms
    elif request.method == 'POST':
        current_step = int(request.POST.get('step'))
        next_step = int(current_step) + 1
        # Get the next form template to display
        next_test_template = 'integrity/'+str(test_steps.get(next_step))
        # Get the text_code to obtain the time assigned por each page
        test_code_object = TestCode.objects.get(code=test_code)
        seconds_integrity = test_code_object.seconds_integrity
        # If current step is 0, save the ObjectIntegrity object with the candidate's info
        if current_step == 0:
            test_form = candidato(request.POST)
            if test_form.is_valid():
                integrity_object = ObjectIntegrity()
                test_code_object = TestCode.objects.get(code=test_code)
                integrity_object.code = test_code_object
                integrity_object.name = test_form.cleaned_data['nombre']
                integrity_object.age = test_form.cleaned_data['edad']
                integrity_object.email = test_form.cleaned_data['email']
                integrity_object.sex = test_form.cleaned_data['sexo']
                integrity_object.save()
                integrity_object.id
            else:
                # Display errors
                return render(request, 'integrity/'+str(test_steps.get(current_step)), {'form': candidato})
            # Go to the next template, for this case the next template is integrity_test_1.html
            return render(request, next_test_template, {'integrity_object_id': integrity_object.id,'seconds_integrity':seconds_integrity,})
        else:
            # Get the saved integrity_object to update
            integrity_object_id = int(request.POST.get('integrity_object_id'))
            integrity_object = ObjectIntegrity.objects.get(id=integrity_object_id)
            # Sum the values from the form to the saved values
            integrity_object.adictions = integrity_object.adictions + int(request.POST.get('adictions', 0))
            integrity_object.judgement = integrity_object.judgement + int(request.POST.get('judgement', 0))
            integrity_object.discipline = integrity_object.discipline + int(request.POST.get('discipline', 0))
            integrity_object.veracity = integrity_object.veracity + int(request.POST.get('veracity', 0))
            integrity_object.loyalty = integrity_object.loyalty + int(request.POST.get('loyalty', 0))
            integrity_object.intentionality = integrity_object.intentionality + int(request.POST.get('intentionality', 0))
            integrity_object.ethic = integrity_object.ethic + int(request.POST.get('ethic', 0))
            integrity_object.reliability = integrity_object.reliability + int(request.POST.get('reliability', 0))
            # Update the form with the new sum of values
            integrity_object.save()
            # if final step return the finish template
            if current_step == 20:
                return render(
                                request, 
                                'finish.html', 
                                dict(title = 'Integridad',name = integrity_object.name))            
            
            # Go to the next template
            return render(request, next_test_template, {'step': current_step, 'integrity_object_id': integrity_object.id, 'seconds_integrity':seconds_integrity})
    return redirect('login')

def integrity_test_result(request, test_type, test_id):

    integrity_object = get_object_or_404(ObjectIntegrity, pk=test_id)

    # adictions Description
    adictions_desc = {
        "passed": "Es una persona que no muestra dependencia por el consumo, tanto de bebidas alcohólicas, drogas, psicofármacos, tabaco o alimentos en exceso. Señala interés en el cuidado de su salud física, psíquica y equilibrio emocional.",
        "passed_cond": "Pudiera ser proclive ya sea a la ingesta de alcohol, fármacos, tabaco, o alimentos. Se puede reflejar ante situaciones de conflicto, presión o en fines de semana.",
        "failed": "Elevada dependencia hacia alguna sustancia farmacológica o alcohol, lo mismo que hacia alguna actividad o relación, que le puede causar graves consecuencias en su vida, que la afectan negativamente en su salud (física-mental) y le impiden desempeñarse de un modo efectivo. El individuo puede no ser capaz de controlar su dependencia al juego, la pornografía, la comida, las drogas, la televisión o incluso a las nuevas tecnologías.",
    }

    # judgement Description
    judgement_desc = {
        "passed": "Muestra un razonamiento correcto para juzgar, responder y desempeñarse en las situaciones que se le presentan.",
        "passed_cond": "Su sentido común puede ser incorrecto al responder o desenvolverse en situaciones difíciles, de conflicto o para su conveniencia.",
        "failed": "Puede juzgar y comparar respecto de una circunstancia u otra y dar una opinión o proceder inadecuada y erradamente respecto a lo correcto.",
    }

    # discipline Description
    discipline_desc = {
        "passed": "Es una persona estructurada, sigue un orden, procesos y disciplinas estandarizadas en la Compañía, familiares y personales, señalando un amplio sentido, observancia y sujeción de su conducta a las reglas.",
        "passed_cond": " No se acopla a ciertas reglas que estipule la Compañía, o en el entorno en el que se desenvuelve, sigue sus propias convicciones y cuando sea necesario para sus fines desdeñará disciplinas.",
        "failed": "Realiza las actividades sin rumbo ni orden. Busca libertad para actuar y seguir sus propias iniciativas de acción sin considerar las políticas, reglamentos o reglas ya sean empresariales o familiares; incluso pudiera mostrar bajo compromiso para con el equipo de trabajo, supervisor o la Compañía.",
    }

    # veracity Description
    veracity_desc = {
        "passed": "Las respuestas que vierte en el cuestionario son congruentes y adecuadas entre lo que piensa y lo que dice, así como lo que hace.",
        "passed_cond": "Trata de dar una buena imagen de sí, distorsionando algunas respuestas a los planteamientos del cuestionario.",
        "failed": "Es baja la concordancia entre lo que piensa y dice o hace, a partir de las respuestas que ofrece a los planteamientos y situaciones del cuestionario.",
    }

    # loyalty Description
    loyalty_desc = {
        "passed": "La persona hace aquello con lo que se ha comprometido, incluso en circunstancias cambiantes o adversas. Está comprometida y defiende aquello en lo que cree y a quien le tiene confianza. Asume el deber de cumplir y mantiene las reglas que libremente ha decidido asumir.",
        "passed_cond": "Eventualmente puede recurrir al engaño o bien no ser leal en circunstancias muy puntuales en las que pueda perder o ser vulnerable en asuntos que involucren su estabilidad.",
        "failed": "Niega con sus actos aquello que había ofrecido realizar o cumplir. Es infiel a personas o incluso a su palabra, tratando de sacar provecho de las situaciones para sus propios fines ya sean personales o de trabajo y es capaz de engañar a otros.",
    }

    # intentionality Description
    intentionality_desc = {
        "passed": "Posee honradez e integridad de sus acciones y dichos. La persona se desempeña bajo el principio de “buena fe”, buscando impedir actuaciones abusivas, aplicando en cambio la rectitud y transparencia a su proceder.",
        "passed_cond": "Puede descuidar cuestiones de honradez como modificar decisiones en situaciones que desde su propia perspectiva considera que no perjudica a terceros y le benefician ante una importante problemática. También puede reflejarse por apropiarse de ideas o materiales aunque estos sean pequeños como por ejemplo lápices.",
        "failed": "Es capaz de alterar escritos, decisiones o dichos, buscar cohecho, adjudicarse ideas o materiales aunque estos sean pequeños como por ejemplo lápices. Es un individuo corrupto o fácilmente corruptible.",
    }

    # ethic Description
    ethic_desc = {
        "passed": "Muestra objetividad en el sentido valorativo de su ambiente personal, profesional y/ o laboral, procede con base en una adecuada percepción de lo correcto e incorrecto, bueno o malo, valioso o reprobable de su comportamiento.",
        "passed_cond": "Puede llevar a cabo comportamientos errados respecto a lo valioso o reprobable, causados por una mala percepción ante ciertas circunstancias o por convicciones o aprendizajes pasados.",
        "failed": "Desdeña lineamientos como legalidad y profesionalismo, pudiendo ir en contra de lo correcto, lo bueno y no aceptar valores.",
    }

    # reliability Description
    reliability_desc = {
        "passed": "Toma acciones o decisiones siendo consciente de las consecuencias que puedan generar tanto para su propia persona como para las personas involucradas y / o la Compañía. Muestra un amplio sentido de las reglas y la ley.",
        "passed_cond": "Puede tomar acciones imprudentes e incluso brincarse reglas al tomar decisiones con cierta frecuencia, sin considerar en forma inmediata las consecuencias que ello pueda tener en su seguridad económica o física.",
        "failed": " Generalmente se involucra en situaciones de incertidumbre, exponiéndose al peligro, lo que puede ocasionar un perjuicio o daño. Se deja llevar por la suerte, procede o toma decisiones de manera azarosa, de forma casual e imprevista, poniendo en riesgo su patrimonio, lo mismo que bienes o activos ajenos.",
    }

    # Addictions percentage
    if integrity_object.adictions <= 67 : addiction_percentage = 99
    if integrity_object.adictions <= 61 : addiction_percentage = 95
    if integrity_object.adictions <= 58 : addiction_percentage = 90
    if integrity_object.adictions <= 56 : addiction_percentage = 85
    if integrity_object.adictions <= 54 : addiction_percentage = 80
    if integrity_object.adictions <= 53 : addiction_percentage = 75
    if integrity_object.adictions <= 51 : addiction_percentage = 70
    if integrity_object.adictions <= 50 : addiction_percentage = 65
    if integrity_object.adictions <= 49 : addiction_percentage = 60
    if integrity_object.adictions <= 47 : addiction_percentage = 55
    if integrity_object.adictions <= 46 : addiction_percentage = 50
    if integrity_object.adictions <= 45 : addiction_percentage = 45
    if integrity_object.adictions <= 44 : addiction_percentage = 40
    if integrity_object.adictions <= 42 : addiction_percentage = 35
    if integrity_object.adictions <= 41 : addiction_percentage = 30
    if integrity_object.adictions <= 39 : addiction_percentage = 25
    if integrity_object.adictions <= 36 : addiction_percentage = 20
    if integrity_object.adictions <= 32 : addiction_percentage = 15
    if integrity_object.adictions <= 29 : addiction_percentage = 10
    if integrity_object.adictions <= 23 : addiction_percentage = 5
    if integrity_object.adictions <= 7 : addiction_percentage = 1

    if addiction_percentage >= 61:
        adictions_desc_result = adictions_desc['passed']
        adictions_score = "Aprobado"
    elif addiction_percentage <= 50:
        adictions_desc_result = adictions_desc['failed']
        adictions_score = "Reprobado"
    else:
        adictions_desc_result = adictions_desc['passed_cond']
        adictions_score = "Aprobado con Reservas"

    # Judgement percentage
    if integrity_object.judgement <= 71 : judgement_percentage = 99
    if integrity_object.judgement <= 69 : judgement_percentage = 95
    if integrity_object.judgement <= 66 : judgement_percentage = 90
    if integrity_object.judgement <= 63 : judgement_percentage = 85
    if integrity_object.judgement <= 62 : judgement_percentage = 80
    if integrity_object.judgement <= 60 : judgement_percentage = 75
    if integrity_object.judgement <= 59 : judgement_percentage = 70
    if integrity_object.judgement <= 58 : judgement_percentage = 65
    if integrity_object.judgement <= 56 : judgement_percentage = 60
    if integrity_object.judgement <= 55 : judgement_percentage = 55
    if integrity_object.judgement <= 54 : judgement_percentage = 50
    if integrity_object.judgement <= 52 : judgement_percentage = 45
    if integrity_object.judgement <= 50 : judgement_percentage = 40
    if integrity_object.judgement <= 48 : judgement_percentage = 35
    if integrity_object.judgement <= 46 : judgement_percentage = 30
    if integrity_object.judgement <= 44 : judgement_percentage = 25
    if integrity_object.judgement <= 42 : judgement_percentage = 20
    if integrity_object.judgement <= 39 : judgement_percentage = 15
    if integrity_object.judgement <= 34 : judgement_percentage = 10
    if integrity_object.judgement <= 29 : judgement_percentage = 5
    if integrity_object.judgement <= 6 : judgement_percentage = 1
        
    if judgement_percentage >= 61:
        judgement_desc_result = judgement_desc['passed']
        judgement_score = "Aprobado"
    elif judgement_percentage <= 50:
        judgement_desc_result = judgement_desc['failed']
        judgement_score = "Reprobado"
    else:
        judgement_desc_result = judgement_desc['passed_cond']
        judgement_score = "Aprobado con Reservas"

    # Discipline percentage
    if integrity_object.discipline <= 55 : discipline_percentage = 99
    if integrity_object.discipline <= 52 : discipline_percentage = 95
    if integrity_object.discipline <= 49 : discipline_percentage = 90
    if integrity_object.discipline <= 47 : discipline_percentage = 85
    if integrity_object.discipline <= 45 : discipline_percentage = 80
    if integrity_object.discipline <= 42 : discipline_percentage = 75
    if integrity_object.discipline <= 40 : discipline_percentage = 70
    if integrity_object.discipline <= 39 : discipline_percentage = 65
    if integrity_object.discipline <= 37 : discipline_percentage = 60
    if integrity_object.discipline <= 35 : discipline_percentage = 55
    if integrity_object.discipline <= 34 : discipline_percentage = 50
    if integrity_object.discipline <= 33 : discipline_percentage = 45
    if integrity_object.discipline <= 31 : discipline_percentage = 40
    if integrity_object.discipline <= 29 : discipline_percentage = 35
    if integrity_object.discipline <= 27 : discipline_percentage = 30
    if integrity_object.discipline <= 24 : discipline_percentage = 25
    if integrity_object.discipline <= 22 : discipline_percentage = 20
    if integrity_object.discipline <= 20 : discipline_percentage = 15
    if integrity_object.discipline <= 15 : discipline_percentage = 10
    if integrity_object.discipline <= 11 : discipline_percentage = 5
    if integrity_object.discipline <= 5 : discipline_percentage = 1

    if discipline_percentage >= 61:
        discipline_desc_result = discipline_desc['passed']
        discipline_score = "Aprobado"
    elif discipline_percentage <= 50:
        discipline_desc_result = discipline_desc['failed']
        discipline_score = "Reprobado"
    else:
        discipline_desc_result = discipline_desc['passed_cond']
        discipline_score = "Aprobado con Reservas"

    # Veracity percentage
    if integrity_object.veracity <= 108 : veracity_percentage = 99
    if integrity_object.veracity <= 93 : veracity_percentage = 95
    if integrity_object.veracity <= 89 : veracity_percentage = 90
    if integrity_object.veracity <= 87 : veracity_percentage = 85
    if integrity_object.veracity <= 84 : veracity_percentage = 80
    if integrity_object.veracity <= 82 : veracity_percentage = 75
    if integrity_object.veracity <= 80 : veracity_percentage = 70
    if integrity_object.veracity <= 79 : veracity_percentage = 65
    if integrity_object.veracity <= 77 : veracity_percentage = 60
    if integrity_object.veracity <= 76 : veracity_percentage = 55
    if integrity_object.veracity <= 75 : veracity_percentage = 50
    if integrity_object.veracity <= 73 : veracity_percentage = 45
    if integrity_object.veracity <= 72 : veracity_percentage = 40
    if integrity_object.veracity <= 70 : veracity_percentage = 35
    if integrity_object.veracity <= 68 : veracity_percentage = 30
    if integrity_object.veracity <= 65 : veracity_percentage = 25
    if integrity_object.veracity <= 62 : veracity_percentage = 20
    if integrity_object.veracity <= 57 : veracity_percentage = 15
    if integrity_object.veracity <= 52 : veracity_percentage = 10
    if integrity_object.veracity <= 42 : veracity_percentage = 5
    if integrity_object.veracity <= 10 : veracity_percentage = 1

    if veracity_percentage >= 61:
        veracity_desc_result = veracity_desc['passed']
        veracity_score = "Aprobado"
    elif veracity_percentage <= 50:
        veracity_desc_result = veracity_desc['failed']
        veracity_score = "Reprobado"
    else:
        veracity_desc_result = veracity_desc['passed_cond']
        veracity_score = "Aprobado con Reservas"

    # Loyalty percentage
    if integrity_object.loyalty <= 33 : loyalty_percentage = 99
    if integrity_object.loyalty <= 32 : loyalty_percentage = 95
    if integrity_object.loyalty <= 31 : loyalty_percentage = 90
    if integrity_object.loyalty <= 30 : loyalty_percentage = 85
    if integrity_object.loyalty <= 29 : loyalty_percentage = 75
    if integrity_object.loyalty <= 28 : loyalty_percentage = 70
    if integrity_object.loyalty <= 27 : loyalty_percentage = 60
    if integrity_object.loyalty <= 26 : loyalty_percentage = 55
    if integrity_object.loyalty <= 25 : loyalty_percentage = 45
    if integrity_object.loyalty <= 24 : loyalty_percentage = 35
    if integrity_object.loyalty <= 23 : loyalty_percentage = 30
    if integrity_object.loyalty <= 22 : loyalty_percentage = 25
    if integrity_object.loyalty <= 21 : loyalty_percentage = 20
    if integrity_object.loyalty <= 19 : loyalty_percentage = 15
    if integrity_object.loyalty <= 17 : loyalty_percentage = 10
    if integrity_object.loyalty <= 13 : loyalty_percentage = 5
    if integrity_object.loyalty <= 2 : loyalty_percentage = 1

    if loyalty_percentage > 61:
        loyalty_desc_result = loyalty_desc['passed']
        loyalty_score = "Aprobado"
    elif loyalty_percentage < 50:
        loyalty_desc_result = loyalty_desc['failed']
        loyalty_score = "Reprobado"
    else:
        loyalty_desc_result = loyalty_desc['passed_cond']
        loyalty_score = "Aprobado con Reservas"

    # Intentionality percentage
    if integrity_object.intentionality <= 201 : intentionality_percentage = 99
    if integrity_object.intentionality <= 190 : intentionality_percentage = 95
    if integrity_object.intentionality <= 185 : intentionality_percentage = 90
    if integrity_object.intentionality <= 180 : intentionality_percentage = 85
    if integrity_object.intentionality <= 176 : intentionality_percentage = 80
    if integrity_object.intentionality <= 172 : intentionality_percentage = 75
    if integrity_object.intentionality <= 168 : intentionality_percentage = 70
    if integrity_object.intentionality <= 166 : intentionality_percentage = 65
    if integrity_object.intentionality <= 163 : intentionality_percentage = 60
    if integrity_object.intentionality <= 160 : intentionality_percentage = 55
    if integrity_object.intentionality <= 156 : intentionality_percentage = 50
    if integrity_object.intentionality <= 152 : intentionality_percentage = 45
    if integrity_object.intentionality <= 149 : intentionality_percentage = 40
    if integrity_object.intentionality <= 146 : intentionality_percentage = 35
    if integrity_object.intentionality <= 143 : intentionality_percentage = 30
    if integrity_object.intentionality <= 139 : intentionality_percentage = 25
    if integrity_object.intentionality <= 132 : intentionality_percentage = 20
    if integrity_object.intentionality <= 124 : intentionality_percentage = 15
    if integrity_object.intentionality <= 108 : intentionality_percentage = 10
    if integrity_object.intentionality <= 68 : intentionality_percentage = 5
    if integrity_object.intentionality <= 21 : intentionality_percentage = 1

    if intentionality_percentage >= 61:
        intentionality_desc_result = intentionality_desc['passed']
        intentionality_score = "Aprobado"
    elif intentionality_percentage <= 50:
        intentionality_desc_result = intentionality_desc['failed']
        intentionality_score = "Reprobado"
    else:
        intentionality_desc_result = intentionality_desc['passed_cond']
        intentionality_score = "Aprobado con Reservas"

    # Ethic percentage
    if integrity_object.ethic <= 146 : ethic_percentage = 99
    if integrity_object.ethic <= 134 : ethic_percentage = 95
    if integrity_object.ethic <= 129 : ethic_percentage = 90
    if integrity_object.ethic <= 126 : ethic_percentage = 85
    if integrity_object.ethic <= 123 : ethic_percentage = 80
    if integrity_object.ethic <= 120 : ethic_percentage = 75
    if integrity_object.ethic <= 118 : ethic_percentage = 70
    if integrity_object.ethic <= 115 : ethic_percentage = 65
    if integrity_object.ethic <= 113 : ethic_percentage = 60
    if integrity_object.ethic <= 111 : ethic_percentage = 55
    if integrity_object.ethic <= 108 : ethic_percentage = 50
    if integrity_object.ethic <= 105 : ethic_percentage = 45
    if integrity_object.ethic <= 102 : ethic_percentage = 40
    if integrity_object.ethic <= 98 : ethic_percentage = 35
    if integrity_object.ethic <= 94 : ethic_percentage = 30
    if integrity_object.ethic <= 89 : ethic_percentage = 25
    if integrity_object.ethic <= 85 : ethic_percentage = 20
    if integrity_object.ethic <= 79 : ethic_percentage = 15
    if integrity_object.ethic <= 68 : ethic_percentage = 10
    if integrity_object.ethic <= 53 : ethic_percentage = 5
    if integrity_object.ethic <= 20 : ethic_percentage = 1

    if ethic_percentage >= 61:
        ethic_desc_result = ethic_desc['passed']
        ethic_score = "Aprobado"
    elif ethic_percentage <= 50:
        ethic_desc_result = ethic_desc['failed']
        ethic_score = "Reprobado"
    else:
        ethic_desc_result = ethic_desc['passed_cond']
        ethic_score = "Aprobado con Reservas"

    # Reliability percentage
    if integrity_object.reliability  <= 41 : reliability_percentage = 99
    if integrity_object.reliability  <= 40 : reliability_percentage = 95
    if integrity_object.reliability  <= 39 : reliability_percentage = 90
    if integrity_object.reliability  <= 37 : reliability_percentage = 85
    if integrity_object.reliability  <= 35 : reliability_percentage = 80
    if integrity_object.reliability  <= 34 : reliability_percentage = 75
    if integrity_object.reliability  <= 33 : reliability_percentage = 70
    if integrity_object.reliability  <= 32 : reliability_percentage = 65
    if integrity_object.reliability  <= 31 : reliability_percentage = 60
    if integrity_object.reliability  <= 29 : reliability_percentage = 55
    if integrity_object.reliability  <= 28 : reliability_percentage = 50
    if integrity_object.reliability  <= 26 : reliability_percentage = 45
    if integrity_object.reliability  <= 25 : reliability_percentage = 40
    if integrity_object.reliability  <= 23 : reliability_percentage = 35
    if integrity_object.reliability  <= 22 : reliability_percentage = 30
    if integrity_object.reliability  <= 21 : reliability_percentage = 25
    if integrity_object.reliability  <= 18 : reliability_percentage = 20
    if integrity_object.reliability  <= 15 : reliability_percentage = 15
    if integrity_object.reliability  <= 12 : reliability_percentage = 10
    if integrity_object.reliability  <= 9 : reliability_percentage = 5
    if integrity_object.reliability  <= 3 : reliability_percentage = 1

    if reliability_percentage >= 61:
        reliability_desc_result = reliability_desc['passed']
        reliability_score = "Aprobado"
    elif reliability_percentage <= 50:
        reliability_desc_result = reliability_desc['failed']
        reliability_score = "Reprobado"
    else:
        reliability_desc_result = reliability_desc['passed_cond']
        reliability_score = "Aprobado con Reservas"


    result_descriptions = {
        "adictions_desc_result" :adictions_desc_result,
        "judgement_desc_result" :judgement_desc_result,
        "discipline_desc_result" :discipline_desc_result,
        "veracity_desc_result" :veracity_desc_result,
        "loyalty_desc_result" :loyalty_desc_result,
        "intentionality_desc_result" :intentionality_desc_result,
        "ethic_desc_result" :ethic_desc_result,
        "reliability_desc_result" :reliability_desc_result,
    }  

    scores = {
        "adictions_score" :adictions_score,
        "judgement_score" :judgement_score,
        "discipline_score" :discipline_score,
        "veracity_score" :veracity_score,
        "loyalty_score" :loyalty_score,
        "intentionality_score" :intentionality_score,
        "ethic_score" :ethic_score,
        "reliability_score" :reliability_score,
    }

    percentages = {
        "adictions_percentage" :addiction_percentage,
        "judgement_percentage" :judgement_percentage,
        "discipline_percentage" :discipline_percentage,
        "veracity_percentage" :veracity_percentage,
        "loyalty_percentage" :loyalty_percentage,
        "intentionality_percentage" :intentionality_percentage,
        "ethic_percentage" :ethic_percentage,
        "reliability_percentage" :reliability_percentage,
    }

    if 'export_button' in request.POST:

        html_template = get_template('integrity/test_result_pdf.html')

        # Render the context into the PDF/HTML template
        context = {"results":integrity_object, "result_descriptions":result_descriptions, "scores": scores, "percentages": percentages}

        html = html_template.render(context)
        pdf_file = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="PruebaIntegridad.pdf"'

        # Return the response to preview the PDF in a new tab
        return response

    return render(request, 'integrity/test_result.html', {"results":integrity_object, "result_descriptions":result_descriptions, "scores": scores, "percentages": percentages})


def max_instructions(request, test_code):
    if request.method == 'GET':
        if TestCode.objects.filter(code=test_code).exists():
            test_code_object = TestCode.objects.get(code=test_code)
            # Check if code is valid
            code_errors = check_code(test_code_object)
            if code_errors == None:
                return render(request,'max/max_instructions.html',{'test_code_object':test_code_object})
        return redirect('login')

    else:
        start_test = request.POST.get('start_test', False)
        if start_test:
            return redirect('max_test',test_code=test_code)
    return redirect('login')

def max_test(request, test_code):

    # Dictionary with all forms
    test_steps = {
        0: 'max_test_0.html',
        1: 'max_test_1.html',
        2: 'max_test_2.html',
        3: 'max_test_3.html',
        4: 'max_test_4.html',
        5: 'max_test_5.html',
        6: 'max_test_6.html',
        7: 'max_test_7.html',
        8: 'max_test_8.html',
        9: 'max_test_9.html',
        10: 'max_test_10.html',
    }

    # Display the candidate's info form
    if request.method == 'GET':
        test_template = 'max/'+str(test_steps.get(0))
        return render(request, test_template, {'form': candidato})

    # Start saving all the forms
    elif request.method == 'POST':
        current_step = int(request.POST.get('step'))
        next_step = int(current_step) + 1
        # Get the next form template to display
        next_test_template = 'max/'+str(test_steps.get(next_step))
        # Get the text_code to obtain the time assigned por each page
        test_code_object = TestCode.objects.get(code=test_code)
        # If current step is 0, save the ObjectIntegrity object with the candidate's info
        if current_step == 0:
            test_form = candidato(request.POST)
            if test_form.is_valid():
                max_object = ObjectMax()
                test_code_object = TestCode.objects.get(code=test_code)
                max_object.code = test_code_object
                max_object.name = test_form.cleaned_data['nombre']
                max_object.age = test_form.cleaned_data['edad']
                max_object.email = test_form.cleaned_data['email']
                max_object.sex = test_form.cleaned_data['sexo']
                max_object.save()
            else:
                # Display errors
                return render(request, 'max/'+str(test_steps.get(current_step)), {'form': candidato})
            # Go to the next template, for this case the next template is integrity_test_1.html
            return render(request, next_test_template, {'max_object_id': max_object.id,})
        else:
            # Get the saved integrity_object to update
            max_object_id = int(request.POST.get('max_object_id'))
            max_object = ObjectMax.objects.get(id=max_object_id)
            # Sum the values from the form to the saved values
            max_object.T = max_object.T + int(request.POST.get('T', 0))
            max_object.V = max_object.V + int(request.POST.get('V', 0))
            max_object.X = max_object.X + int(request.POST.get('X', 0))
            max_object.S = max_object.S + int(request.POST.get('S', 0))
            max_object.B = max_object.B + int(request.POST.get('B', 0))
            max_object.O = max_object.O + int(request.POST.get('O', 0))
            max_object.R = max_object.R + int(request.POST.get('R', 0))
            max_object.D = max_object.D + int(request.POST.get('D', 0))
            max_object.C = max_object.C + int(request.POST.get('C', 0))
            max_object.Z = max_object.Z + int(request.POST.get('Z', 0))
            max_object.E = max_object.E + int(request.POST.get('E', 0))
            max_object.K = max_object.K + int(request.POST.get('K', 0))
            max_object.F = max_object.F + int(request.POST.get('F', 0))
            max_object.W = max_object.W + int(request.POST.get('W', 0))
            max_object.N = max_object.N + int(request.POST.get('N', 0))
            max_object.G = max_object.G + int(request.POST.get('G', 0))
            max_object.A = max_object.A + int(request.POST.get('A', 0))
            max_object.L = max_object.L + int(request.POST.get('L', 0))
            max_object.P = max_object.P + int(request.POST.get('P', 0))
            max_object.I = max_object.I + int(request.POST.get('I', 0))
            # Update the form with the new sum of values
            max_object.save()
            # if final step return the finish template
            if current_step == 9:
                return render(
                                request, 
                                'max/finish.html', 
                                dict(title = 'Max',name = max_object.name))            
            
            # Go to the next template
            return render(request, next_test_template, {'step': current_step, 'max_object_id': max_object.id,})
    return redirect('login')

def max_test_result(request, test_type, test_id):
    max_object = get_object_or_404(ObjectMax, pk=test_id)

    # calculate descriptions
    result_descriptions = get_result_descriptions(max_object)

    if 'select_position' in request.POST:

        # TODO: Get the position id from the front input and get the proper position from the db
        # Using the first element just for testing
        selected_position_object = MaxPositions.objects.get(id=1)

        return render(request, 'max/test_result.html', {"results":max_object, "result_descriptions":result_descriptions,"selected_position_object":selected_position_object,})

    if 'export_button' in request.POST:

        html_template = get_template('max/test_result_pdf.html')

        # Render the context into the PDF/HTML template
        context = {"results":max_object, "result_descriptions":result_descriptions,}

        html = html_template.render(context)
        pdf_file = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="PruebaIntegridad.pdf"'

        # Return the response to preview the PDF in a new tab
        return response

    
    print(result_descriptions["T"])
    selected_position_object = MaxPositions.objects.get(id=1)
    return render(request, 'max/test_result.html', {"results":max_object, "result_descriptions":result_descriptions,"selected_position_object":selected_position_object})
