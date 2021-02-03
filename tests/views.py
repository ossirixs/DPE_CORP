from django.shortcuts import render
from tests.models import ObjectCIE
from company.models import TestCode
from tests.forms import *
from formtools.wizard.views import SessionWizardView
from django.shortcuts import get_object_or_404
from tests.utils import clean_data

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


    result = "Est (Estabilidad Emocional) Bajo: Impulsiva, nerviosa e irritable, esta persona se sobreexcita " \
             "ante las circunstancias que no puede controlar. Es susceptible e irritable emocionalmente. " \
             "Se altera fácilmente. Manifiesta cambios de ánimo y mal humor."

    print('ESTs', EST_true, EST_false)

    print('en true EST', EST)
    for pregunta in EST_true:
        EST += clean_data(pregunta, invert=0)
    print('en false EST', EST)
    for pregunta in EST_false:
        EST += clean_data(pregunta, invert=1)

    print('final EST', EST)

    for pregunta in ANS_true:
        ANS += clean_data(pregunta, invert=0)
    for pregunta in ANS_false:
        ANS += clean_data(pregunta, invert=1)

    for pregunta in AUC_true:
        AUC += clean_data(pregunta, invert=0)
    for pregunta in AUC_false:
        AUC += clean_data(pregunta, invert=1)

    for pregunta in EFI_true:
        EFI += clean_data(pregunta, invert=0)
    for pregunta in EFI_false:
        EFI += clean_data(pregunta, invert=1)

    for pregunta in SEG_true:
        SEG += clean_data(pregunta, invert=0)
    for pregunta in SEG_false:
        SEG += clean_data(pregunta, invert=1)

    for pregunta in IND_true:
        IND += clean_data(pregunta, invert=0)
    for pregunta in IND_false:
        IND += clean_data(pregunta, invert=1)

    for pregunta in DOM_true:
        DOM += clean_data(pregunta, invert=0)
    for pregunta in DOM_false:
        DOM += clean_data(pregunta, invert=1)

    for pregunta in COG_true:
        COG += clean_data(pregunta, invert=0)
    for pregunta in COG_false:
        COG += clean_data(pregunta, invert=1)

    for pregunta in SOC_true:
        SOC += clean_data(pregunta, invert=0)
    for pregunta in SOC_false:
        SOC += clean_data(pregunta, invert=1)

    for pregunta in AJS_true:
        AJS += clean_data(pregunta, invert=0)
    for pregunta in AJS_false:
        AJS += clean_data(pregunta, invert=1)

    for pregunta in AGR_true:
        AGR += clean_data(pregunta, invert=0)
    for pregunta in AGR_false:
        AGR += clean_data(pregunta, invert=1)

    for pregunta in TOL_true:
        TOL += clean_data(pregunta, invert=0)
    for pregunta in TOL_false:
        TOL += clean_data(pregunta, invert=1)

    for pregunta in HAB_true:
        HAB += clean_data(pregunta, invert=0)
    for pregunta in HAB_false:
        HAB += clean_data(pregunta, invert=1)

    for pregunta in DISC_true:
        DISC += clean_data(pregunta, invert=0)
    for pregunta in DISC_false:
        DISC += clean_data(pregunta, invert=1)

    for pregunta in LID_true:
        LID += clean_data(pregunta, invert=0)
    for pregunta in LID_false:
        LID += clean_data(pregunta, invert=1)

    for pregunta in VER_true:
        VER += clean_data(pregunta, invert=0)
    for pregunta in VER_false:
        VER += clean_data(pregunta, invert=1)

    for pregunta in IMG_true:
        IMG += clean_data(pregunta, invert=0)
    for pregunta in IMG_false:
        IMG += clean_data(pregunta, invert=1)

    print('escaalas perra', EST, ANS, AUC, EFI, SEG, IND, DOM, COG, SOC, AJS, AGR, TOL, HAB, DISC, LID, VER, IMG, CONG)

    title = 'LEONARDA FLORES HERNANDEZ'

    return render(request, 'test_result.html', dict(title=title,
                                                    result=result,
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
                                                    CONG=CONG))
