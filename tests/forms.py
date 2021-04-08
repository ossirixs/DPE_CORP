from django import forms


class candidato(forms.Form):
    SEXO = ((0, "Femenino"), (1, "Masculino"))

    nombre = forms.CharField(label='Nombre completo', required=True)
    edad = forms.IntegerField(label='Edad', required=True)
    email = forms.CharField(label='Correo Electrónico', required=True)
    sexo = forms.ChoiceField(label='Sexo', required=True, widget=forms.RadioSelect, choices=SEXO)


class CIE_form_1(forms.Form):
    OPCIONES = ((0, "Falso"), (1, "Verdadero"))

    q_1 = forms.ChoiceField(
        label='1. Hay muchas cosas que me hacen enojar.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_2 = forms.ChoiceField(
        label='2. Actualmente vivo momentos malos, tensos o de inquietud.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_3 = forms.ChoiceField(
        label='3. Hago un gran esfuerzo por demostrar que tengo razón, aún cuando tenga que luchar para lograrlo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_4 = forms.ChoiceField(
        label='4. Tengo mala suerte y a eso se debe que me sucedan muchas de las cosas que me pasan.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_5 = forms.ChoiceField(
        label='5. Me gusta ir a reuniones y fiestas donde hay mucha gente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_6 = forms.ChoiceField(
        label='6. Actúo con diplomacia y tengo tacto al decir lo que pienso.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_7 = forms.ChoiceField(
        label='7. Me gusta buscar el aplauso y la alabanza de los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_8 = forms.ChoiceField(
        label='8. Suelo hablar alto cuando siento enojo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_9 = forms.ChoiceField(
        label='9. Sí soy una persona formal y responsable, sin duda alguna.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_10 = forms.ChoiceField(
        label='10. Mi escala de valores e intereses cambia fácilmente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_11 = forms.ChoiceField(
        label='11. Antes de hacer las cosas por lo general tiendo a dudar bastante como hacerlas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_12 = forms.ChoiceField(
        label='12. Abandono fácilmente mis obligaciones.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_13 = forms.ChoiceField(
        label='13. Comunico con facilidad mis alegrías y tristezas a los demás y me encanta hacerlo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_14 = forms.ChoiceField(
        label='14. Me considero una persona estricta en el seguimiento de las normas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_15 = forms.ChoiceField(
        label='15. La gente puede, sin duda, confiar en mi.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_16 = forms.ChoiceField(
        label='16. Evito las discusiones que llevan a nada.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_17 = forms.ChoiceField(
        label='17. Siempre intento proyectar una buena imagen de mi.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_18 = forms.ChoiceField(
        label='18. Mi estado de ánimo puede cambiar fácilmente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_19 = forms.ChoiceField(
        label='19. Actualmente vivo un poco estresado.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_20 = forms.ChoiceField(
        label='20. Soy una persona muy trabajadora y eficiente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)

class CIE_form_2(forms.Form):
    OPCIONES = ((0, "Falso"), (1, "Verdadero"))

    q_21 = forms.ChoiceField(
        label='21. El éxito es mi meta y estilo de vida.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_22 = forms.ChoiceField(
        label='22. Busco hablar con franqueza y ser abierto con los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_23 = forms.ChoiceField(
        label='23. Me caracterizo por ser una persona reservada o retraída.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_24 = forms.ChoiceField(
        label='24. Considero que mi comportamiento se ajusta a las normas convencionales.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_25 = forms.ChoiceField(
        label='25. Frecuentemente me excedo en destacar mis éxitos.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_26 = forms.ChoiceField(
        label='26. Puedo disgustarme fácilmente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_27 = forms.ChoiceField(
        label='27. Me ruborizo con cierta facilidad.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_28 = forms.ChoiceField(
        label='28. Puedo cambiar de opinión fácilmente si mis amigos me lo piden.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_29 = forms.ChoiceField(
        label='29. Asistir a reuniones sociales o conocer gente nueva, en ocasiones me hace sentir inquieto.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_30 = forms.ChoiceField(
        label='30. Prefiero estar acompañado cuando tengo problemas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_31 = forms.ChoiceField(
        label='31. Me gusta dirigir y hacer que las cosas funcionen.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_32 = forms.ChoiceField(
        label='32. Me gusta organizar bien mi trabajo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_33 = forms.ChoiceField(
        label='33. Me encanta relacionarme con la gente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_34 = forms.ChoiceField(
        label='34. Cuando las personas son informales o incumplidoras suelo criticar su proceder.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_35 = forms.ChoiceField(
        label='35. Observar las costumbres y reglas sociales rige de alguna manera mis valores.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_36 = forms.ChoiceField(
        label='36. Suelo empezar las cosas y no terminarlas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_37 = forms.ChoiceField(
        label='37. Trato de ganar las discusiones en grupo o al menos quedar mejor posicionado que los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_38 = forms.ChoiceField(
        label='38. Cuando tengo que hablar en público, me siento nervioso.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_39 = forms.ChoiceField(
        label='39. Tengo una alta opinión de mi mismo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_40 = forms.ChoiceField(
        label='40. Por lo general, no pido consejo a los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)

class CIE_form_3(forms.Form):
    OPCIONES = ((0, "Falso"), (1, "Verdadero"))

    q_41 = forms.ChoiceField(
        label='41. Mi comportamiento hacia la gente es, en general, distante.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_42 = forms.ChoiceField(
        label='42. En ocasiones cuando tomo una decisión, suele suceder que se me ha pasado la oportunidad.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_43 = forms.ChoiceField(
        label='43. Cuando alguien se incorpora a un grupo de personas, lo aceptoy entablo conversación con él.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_44 = forms.ChoiceField(
        label='44. Si me la hacen, me la pagan.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_45 = forms.ChoiceField(
        label='45. Cumplo con lo que he prometido hacer generalmente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_46 = forms.ChoiceField(
        label='46. Aprovecho las oportunidades que se me presentan para llamar la atención de personas del sexo opuesto.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_47 = forms.ChoiceField(
        label='47. A veces expreso mis emociones en forma explosiva.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_48 = forms.ChoiceField(
        label='48. Me considero una persona un tanto nerviosa.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_49 = forms.ChoiceField(
        label='49. Soy una persona con una gran capacidad para trabajar.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_50 = forms.ChoiceField(
        label='50. Tengo confianza en mi capacidad para hacer las cosas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_51 = forms.ChoiceField(
        label='51. Por lo general, prefiero no tener en cuenta los problemas de los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_52 = forms.ChoiceField(
        label='52. Tiendo a ser autoritario y dominante.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_53 = forms.ChoiceField(
        label='53. Considero que tengo las cualidades para ser líder.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_54 = forms.ChoiceField(
        label='54. Cuando me molestan, puedo responder agresivamente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_55 = forms.ChoiceField(
        label='55. Trato de no decir cosas que puedan ofender a otras personas si creo que pueden perjudicarme.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_56 = forms.ChoiceField(
        label='56. Trato de demostrar que sé y entiendo de cualquier tema que se trate.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_57 = forms.ChoiceField(
        label='57. A menudo suelo manifestar mi mal humor.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_58 = forms.ChoiceField(
        label='58. Los imprevistos o las malas noticias me ponen nervioso.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_59 = forms.ChoiceField(
        label='59. En ocasiones suelo hacer el ridículo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_60 = forms.ChoiceField(
        label='60. Me considero una persona responsable y eficaz al encargarme de algo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)

class CIE_form_4(forms.Form):
    OPCIONES = ((0, "Falso"), (1, "Verdadero"))

    q_61 = forms.ChoiceField(
        label='61. Me encanta mandar.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_62 = forms.ChoiceField(
        label='62. Me es difícil ser yo quien entable conversación con las personas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_63 = forms.ChoiceField(
        label='63. Suelo molestarme y llamar la atención a quienes me impiden oír o ver una película o espectáculo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_64 = forms.ChoiceField(
        label='64. A menudo mis padres no estarían de acuerdo con mi forma de ser y comportarme.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_65 = forms.ChoiceField(
        label='65. Cumplo con mis deberes.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_66 = forms.ChoiceField(
        label='66. Al proponerme alcanzar una meta importante en mi vida (Ej. Un trabajo) hago uso de todos los medios a mi alcance para lograrlo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_67 = forms.ChoiceField(
        label='67. Considero ser una persona con influencia ante los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_68 = forms.ChoiceField(
        label='68. Siento que en algunas situaciones se hieren fácilmente mis sentimientos.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_69 = forms.ChoiceField(
        label='69. Me muestro impaciente cuando debo terminar las tareas o trabajos.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_70 = forms.ChoiceField(
        label='70. Las adversidades me sobrepasan fácilmente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_71 = forms.ChoiceField(
        label='71. Prefiero ser yo solo el responsable cuando tengo que resolver un asunto de trascendencia.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_72 = forms.ChoiceField(
        label='72. Soy capaz de guiar a la gente de acuerdo a mis intereses.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_73 = forms.ChoiceField(
        label='73. Dar mi palabra es tan importante como dejarla escrita.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_74 = forms.ChoiceField(
        label='74. Me siento cómodo participando en conversaciones de grupo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_75 = forms.ChoiceField(
        label='75. Doy una gran importancia a mis obligaciones tanto en el trabajo como con las personas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_76 = forms.ChoiceField(
        label='76. Soy digno de la confianza de mis superiores.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_77 = forms.ChoiceField(
        label='77. Procuro ser el mejor en casi todo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_78 = forms.ChoiceField(
        label='78. Suelo ser puntual y llegar a la hora.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_79 = forms.ChoiceField(
        label='79. Mi estado de ánimo depende de cómo vayan resultando las cosas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_80 = forms.ChoiceField(
        label='80. Suelo tener pensamientos persistentes que perturban mi estado de ánimo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)

class CIE_form_5(forms.Form):
    OPCIONES = ((0, "Falso"), (1, "Verdadero"))

    q_81 = forms.ChoiceField(
        label='81. Puedo demostrar mi capacidad y mi valía cuando me ofrecen la oportunidad de hacerlo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_82 = forms.ChoiceField(
        label='82. Las autoridades y en general mis superiores respetan mis derechos porque yo los hago valer.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_83 = forms.ChoiceField(
        label='83. Soy precavido y me gusta planear todo lo que hago con suficiente anticipación.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_84 = forms.ChoiceField(
        label='84. Puedo controlar lo que digo al encontrarme en una discusión.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_85 = forms.ChoiceField(
        label='85. Me gusta más trabajar en equipo que solo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_86 = forms.ChoiceField(
        label='86. Cuando alguien me ignora o me enfrenta, lo pongo en su lugar.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_87 = forms.ChoiceField(
        label='87. La buena educación y el civismo son para otros.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_88 = forms.ChoiceField(
        label='88. No me gusta convivir con personas creídas o mandonas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_89 = forms.ChoiceField(
        label='89. Prefiero grupos pequeños de amistades.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_90 = forms.ChoiceField(
        label='90. Generalmente busco quedar bien con los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_91 = forms.ChoiceField(
        label='91. A veces me siento menos que los demás y eso turba mi comportamiento.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_92 = forms.ChoiceField(
        label='92. En ocasiones me cuesta trabajo concentrarme en mis tareas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_93 = forms.ChoiceField(
        label='93. Lo que he hecho hasta ahora me demuestra que soy competente en casi todo lo que me propongo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_94 = forms.ChoiceField(
        label='94. Por lo general, suelo hacer las cosas a mi manera.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_95 = forms.ChoiceField(
        label='95. No me gusta que me impongan reglas y normas estrictas en el trabajo o en mi forma de actuar.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_96 = forms.ChoiceField(
        label='96. Generalmente, intento ser quien dice la última palabra.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_97 = forms.ChoiceField(
        label='97. Trato de ser prudente y manejarme con cautela cuando me entrevisto con otras personas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_98 = forms.ChoiceField(
        label='98. Se me dificulta hablar con una persona de otro rango o nivel.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_99 = forms.ChoiceField(
        label='99. Si me cito con una persona y me deja plantado, suelo reclamarle de forma molesta.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_100 = forms.ChoiceField(
        label='100. En ocasiones hago cosas que no debiera yendo en contra de las reglas establecidas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)

class CIE_form_6(forms.Form):
    OPCIONES = ((0, "Falso"), (1, "Verdadero"))

    q_101 = forms.ChoiceField(
        label='101. Me gusta imponer mis opiniones a los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_102 = forms.ChoiceField(
        label='102. Antes de tomar una decisión importante, analizo las alternativas posibles.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_103 = forms.ChoiceField(
        label='103. Cuando espero resultados relativamente importantes me muestro inquieto y preocupado.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_104 = forms.ChoiceField(
        label='104. Fracasar me hace sentir desanimado.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_105 = forms.ChoiceField(
        label='105. Cuando dejo algo sin hacer me siento culpable.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_106 = forms.ChoiceField(
        label='106. En general, se puede decir que hago bien las cosas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_107 = forms.ChoiceField(
        label='107. Mis problemas prefiero solucionarlos yo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_108 = forms.ChoiceField(
        label='108. Hay una persona cerca de mi que influye mucho en mi vida.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_109 = forms.ChoiceField(
        label='109. Suelo ser brusco callando e interrumpiendo a las personas cuando creo que están diciendo tonterías.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_110 = forms.ChoiceField(
        label='110. No suelo juzgar a las personas hasta que conozco los hechos.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_111 = forms.ChoiceField(
        label='111. Cuando creo que alguna persona me ha hecho algo evito encontrarme con ella o no le hablo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_112 = forms.ChoiceField(
        label='112. Cuando juego no me gusta perder y si sucede me enojo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_113 = forms.ChoiceField(
        label='113. No dejo que los demás se metan en mi vida.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_114 = forms.ChoiceField(
        label='114. Tiendo a criticar los errores y en general la manera de actuar de los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_115 = forms.ChoiceField(
        label='115. Si alguien me hace menos reiteradamente, hago lo necesario por demostrarle lo que valgo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_116 = forms.ChoiceField(
        label='116. Exagero mis éxitos o fracasos para lograr la atención de los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_117 = forms.ChoiceField(
        label='117. Me encanta estar solo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_118 = forms.ChoiceField(
        label='118. Mi aspecto físico es algo que me preocupa mucho.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_119 = forms.ChoiceField(
        label='119. Desearía que mi personalidad fuera más estable o bien se ajustara más a los distintos ambientes.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_120 = forms.ChoiceField(
        label='120. Muchas veces dudo si lo que hago lo hago bien.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)

class CIE_form_7(forms.Form):
    OPCIONES = ((0, "Falso"), (1, "Verdadero"))

    q_121 = forms.ChoiceField(
        label='121. Prefiero hacerme cargo de la organización y el desarrollo de las tareas sobre todo cuando trabajo en grupo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_122 = forms.ChoiceField(
        label='122. No tomo en cuenta los intereses de los demás cuando quiero conseguir algo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_123 = forms.ChoiceField(
        label='123. Suelo equivocarme frecuentemente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_124 = forms.ChoiceField(
        label='124. Organizo y participo con gusto en diferentes actividades sociales.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_125 = forms.ChoiceField(
        label='125. Cuando hablo, trabajo, leo, estudio o veo televisión me enoja que me interrumpan.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_126 = forms.ChoiceField(
        label='126. Me siento bien cuando influyo en las decisiones de los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_127 = forms.ChoiceField(
        label='127. Cuando voy a hacer algo importante siempre tengo en cuenta cuales van a ser las consecuencias.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_128 = forms.ChoiceField(
        label='128. Si una persona me humilla en público, le hago lo mismo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_129 = forms.ChoiceField(
        label='129. Puedo ser amable con ciertas personas a las que no aprecio.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_130 = forms.ChoiceField(
        label='130. En ocasiones me dejo llevar por mis impulsos.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_131 = forms.ChoiceField(
        label='131. A veces no me siento bien.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_132 = forms.ChoiceField(
        label='132. Si las opiniones de los demás son diferentes a las mías, eso me desanima.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_133 = forms.ChoiceField(
        label='133. Si los demás tratan de imponerme sus ideas yo no lo permito.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_134 = forms.ChoiceField(
        label='134. Lo que los demás piensen de mi, me importa mucho.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_135 = forms.ChoiceField(
        label='135. Me gusta ser quien lleve la iniciativa en las discusiones de grupo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_136 = forms.ChoiceField(
        label='136. Si enfrento problemas al realizar mis actividades abandono fácilmente lo que tengo que hacer.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_137 = forms.ChoiceField(
        label='137. Asistir a reuniones sociales, tener muchos amigos y salir con ellos son cosas muy importantes para mi.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_138 = forms.ChoiceField(
        label='138. No cambio de opinión y defiendo con todo mis puntos de vista cuando se que tengo la razón.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_139 = forms.ChoiceField(
        label='139. Me disgusta que la gente me de instrucciones de cómo o qué tengo que hacer.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_140 = forms.ChoiceField(
        label='140. Tengo mi propia forma de hacer las cosas y suele ser diferente a la de los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)

class CIE_form_8(forms.Form):
    OPCIONES = ((0, "Falso"), (1, "Verdadero"))

    q_141 = forms.ChoiceField(
        label='141. Por lo general, desconfío de la gente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_142 = forms.ChoiceField(
        label='142. Cuando hago bien las cosas me gusta que los demás lo reconozcan.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_143 = forms.ChoiceField(
        label='143. Sentirme observado es algo que me inquieta.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_144 = forms.ChoiceField(
        label='144. Puede considerarse que soy una persona tranquila y serena.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_145 = forms.ChoiceField(
        label='145. Tiendo a buscar que los demás reconozcan lo que hago.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_146 = forms.ChoiceField(
        label='146. Cuando no conozco a la gente, me cuesta trabajo empezar una conversación.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_147 = forms.ChoiceField(
        label='147. En mis relaciones de pareja, dejo que la otra persona siempre tome la iniciativa.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_148 = forms.ChoiceField(
        label='148. Cuando enfrento muchas dificultades al mismo tiempo, me desconcierto y no se que hacer.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_149 = forms.ChoiceField(
        label='149. Soy una persona de trato fácil y agradable.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_150 = forms.ChoiceField(
        label='150. Si alguien se mete delante de mi en una fila indebidamente, le reclamo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_151 = forms.ChoiceField(
        label='151. Me siento muy unido a mi familia.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_152 = forms.ChoiceField(
        label='152. Casi siempre consigo lo que me propongo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_153 = forms.ChoiceField(
        label='153. Cuando me encuentro en fiestas y reuniones me gusta ser el centro de atención.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_154 = forms.ChoiceField(
        label='154. Me preocupo por todo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_155 = forms.ChoiceField(
        label='155. Suelo hacer alarde de mis capacidades y de lo que valgo cada vez que tengo oportunidad.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_156 = forms.ChoiceField(
        label='156. En general me falta confianza y seguridad en mi mismo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_157 = forms.ChoiceField(
        label='157. Cuando los demás tienen éxito, yo me siento fracasado.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_158 = forms.ChoiceField(
        label='158. Que nada ni nadie me haga cambiar de opinión en mis decisiones es algo de lo que realmente puedo presumir.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_159 = forms.ChoiceField(
        label='159. Hay normas y reglas de algunos lugares contra las que me rebelo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_160 = forms.ChoiceField(
        label='160. Cuando alguien no me devuelve algo que le he prestado en el plazo acordado busco vengarme de el.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)

class CIE_form_9(forms.Form):
    OPCIONES = ((0, "Falso"), (1, "Verdadero"))

    q_161 = forms.ChoiceField(
        label='161. Me encanta estar con más personas alrededor.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_162 = forms.ChoiceField(
        label='162. Cuando me enojo, me dan ganas de destrozar cosas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_163 = forms.ChoiceField(
        label='163. Si me comprometo a hacer algo que sea importante siempre cumplo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_164 = forms.ChoiceField(
        label='164. Si siento menosprecio por alguna persona, puedo burlarme o criticarla.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_165 = forms.ChoiceField(
        label='165. Soluciono adecuadamente los problemas que se me presentan.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_166 = forms.ChoiceField(
        label='166. No me interesan ni tomo en cuenta las costumbres o tradiciones familiares.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_167 = forms.ChoiceField(
        label='167. Me emociono fácilmente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_168 = forms.ChoiceField(
        label='168. Admiro a quienes saben aprovecharse de los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_169 = forms.ChoiceField(
        label='169. A veces tengo la impresión de que no sirvo para muchas cosas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_170 = forms.ChoiceField(
        label='170. El futuro y lo malo que pueda pasar en él, a veces me preocupa mucho.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_171 = forms.ChoiceField(
        label='171. Tiendo a comportarme mejor en público que frente a mi familia.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_172 = forms.ChoiceField(
        label='172. Cuando estoy en mi casa trato de salirme siempre con la mía.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_173 = forms.ChoiceField(
        label='173. Soy confiable cuando alguien me confía un secreto.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_174 = forms.ChoiceField(
        label='174. Si alguien me ofende puedo buscar venganza.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_175 = forms.ChoiceField(
        label='175. Confío en que me vaya mejor si tengo suerte que si me esfuerzo por lograrlo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_176 = forms.ChoiceField(
        label='176. Hago todo lo que puedo en el momento para no tener que aplazarlo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_177 = forms.ChoiceField(
        label='177. Las personas piensan que sé imponerme.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_178 = forms.ChoiceField(
        label='178. Entre menos personas sepan que me he equivocado, para mi es mejor.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_179 = forms.ChoiceField(
        label='179. La disciplina y la puntualidad no son de mis características sobresalientes.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_180 = forms.ChoiceField(
        label='180. Me inquieta saber que voy a llegar tarde a una cita.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)

class CIE_form_10(forms.Form):
    OPCIONES = ((0, "Falso"), (1, "Verdadero"))

    q_181 = forms.ChoiceField(
        label='181. Soy una persona con grandes iniciativas y proyectos.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_182 = forms.ChoiceField(
        label='182. A veces me siento inferior ante personas de otro sexo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_183 = forms.ChoiceField(
        label='183. Cuando salgo con mis amigos me gusta decidir a dónde ir.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_184 = forms.ChoiceField(
        label='184. Suelo culpar a los demás cuando algo sale mal.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_185 = forms.ChoiceField(
        label='185. Las personas piensan que soy amable.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_186 = forms.ChoiceField(
        label='186. Me enojo con facilidad si las cosas no salen bien.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_187 = forms.ChoiceField(
        label='187. Dejo que lo que mis padres dicen o lo que les hubiera gustado influya en lo que hago.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_188 = forms.ChoiceField(
        label='188. En todas las situaciones sociales controlo mis emociones y mi comportamiento.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_189 = forms.ChoiceField(
        label='189. Me desespera tener que esperar ante las ventanillas de las oficinas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_190 = forms.ChoiceField(
        label='190. A menudo dejo que los sentimientos se impongan en mis acciones.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_191 = forms.ChoiceField(
        label='191. Algunas veces siento una gran tensión interna.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_192 = forms.ChoiceField(
        label='192. Acepto con gusto las críticas de los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_193 = forms.ChoiceField(
        label='193. Reclamo cuando llego a un lugar unos minutos tarde y ya no me atienden.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_194 = forms.ChoiceField(
        label='194. Me importa mucho la opinión de los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_195 = forms.ChoiceField(
        label='195. Cuando alguien está en contra de mis opiniones, lo ignoro.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_196 = forms.ChoiceField(
        label='196. Fácilmente tomo parte en las discusiones o pláticas de grupo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_197 = forms.ChoiceField(
        label='197. Cuando me insultan soy firme y me defiendo con coraje.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_198 = forms.ChoiceField(
        label='198. Suelo estar en desacuerdo y enfrentarme con miembros de mi familia.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_199 = forms.ChoiceField(
        label='199. Cuando alguien me acusa o me insulta, hago lo mismo con él.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_200 = forms.ChoiceField(
        label='200. Sé como tratar y guiar adecuadamente a las personas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)

class CIE_form_11(forms.Form):
    OPCIONES = ((0, "Falso"), (1, "Verdadero"))

    q_201 = forms.ChoiceField(
        label='201. Elijo con mucho cuidado a las personas en las que debo confiar en asuntos delicados.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_202 = forms.ChoiceField(
        label='202. Pierdo fácilmente la paciencia con los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_203 = forms.ChoiceField(
        label='203. Lloro con mucha facilidad.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_204 = forms.ChoiceField(
        label='204. Cuando las cosas me salen mal me doy por vencido fácilmente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_205 = forms.ChoiceField(
        label='205. Tomo en cuenta la opinión de mis amigos antes de hacer algo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_206 = forms.ChoiceField(
        label='206. Si alguien confía en mi, no lo defraudo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_207 = forms.ChoiceField(
        label='207. Actúo con dureza cuando alguien me ha engañado o intenta hacerlo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_208 = forms.ChoiceField(
        label='208. Suelo involucrarme en situaciones que me hacen correr riesgos innecesarios.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_209 = forms.ChoiceField(
        label='209. Soy muy hablador.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_210 = forms.ChoiceField(
        label='210. Si alguien daña algún objeto personal o me lo devuelve en mal estado, me enojo con esa persona.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_211 = forms.ChoiceField(
        label='211. En un trabajo de grupo me cuesta trabajo aceptar los errores o faltas de los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_212 = forms.ChoiceField(
        label='212. Cuando estaba en la escuela faltaba con cualquier pretexto.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_213 = forms.ChoiceField(
        label='213. Cuando me preguntan algo muy personal trato de contestar diplomáticamente.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_214 = forms.ChoiceField(
        label='214. Algunas veces, solo por quedar bien, hago algo por los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_215 = forms.ChoiceField(
        label='215. Los problemas me abruman fácilmente porque no soporto mucha presión.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_216 = forms.ChoiceField(
        label='216. Duermo mal o inquieto.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_217 = forms.ChoiceField(
        label='217. Suelo buscar nuevas formas de hacer las cosas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_218 = forms.ChoiceField(
        label='218. Las normas y las costumbres sociales son muy importantes para mi.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_219 = forms.ChoiceField(
        label='219. Si no me siento bien atendido al acudir a una oficina o banco en horarios laborales, reclamo y me quejo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_220 = forms.ChoiceField(
        label='220. Utilizo cualquier pretexto para dejar lo que estoy haciendo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)

class CIE_form_12(forms.Form):
    OPCIONES = ((0, "Falso"), (1, "Verdadero"))

    q_221 = forms.ChoiceField(
        label='221. Me dejo abatir fácilmente cuando siento que fracaso o cuando tengo una experiencia negativa.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_222 = forms.ChoiceField(
        label='222. A veces experimento períodos de soledad.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_223 = forms.ChoiceField(
        label='223. Siento que los demás deberían aprender de todo lo que se.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_224 = forms.ChoiceField(
        label='224. Cuando alguien intenta imponerme sus gustos, elijo o decido lo contrario.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_225 = forms.ChoiceField(
        label='225. Puedo hacer que los demás cambien de opinión fácilmente cuando así lo decido.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_226 = forms.ChoiceField(
        label='226. Generalmente pienso las cosas dos veces antes de tomar una decisión.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_227 = forms.ChoiceField(
        label='227. Dependiendo de la situación puedo ser sincero y hasta agresivo o bien diplomático cuando debo serlo.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_228 = forms.ChoiceField(
        label='228. Cuando voy a comprarme ropa o me visto para alguna ocasión antepongo los gustos y opinión de los demás a los míos.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_229 = forms.ChoiceField(
        label='229. Me gusta dar instrucciones a los demás.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_230 = forms.ChoiceField(
        label='230. No me gustan las bromas pesadas y cuando me las hacen a mi reacciono de mala manera.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_231 = forms.ChoiceField(
        label='231. Deseo que las demás personas tengan una opinión distinta de mi.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_232 = forms.ChoiceField(
        label='232. Generalmente me es difícil hablar de mi mismo con otras personas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)
    q_233 = forms.ChoiceField(
        label='233. Siempre trato de destacar sobre las demás personas.',
        required=True, widget=forms.RadioSelect, choices=OPCIONES)

