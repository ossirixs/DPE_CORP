# Django
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
# Models
from tests.models import ObjectCIE
from company.models import TestCode
# Libraries
from formtools.wizard.views import SessionWizardView
from django.shortcuts import get_object_or_404
from tests.utils import clean_data, score_tag_CIE
from weasyprint import HTML
from django.template.loader import get_template
from django.http import HttpResponse
# Utils
from tests.utils import clean_data
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
