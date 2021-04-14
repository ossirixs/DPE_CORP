""" Tools for processing data and prevent errors """


def clean_data(data, invert):
    """
    Function that clean data from None values, return casted data in number
    will invert the output if invert is set True, returns 0 for None values
    """
    # Clean the data for None values
    if data is not None:
        data = int(data)
        # Invert the cleaned data if needed
        if invert:
            data = not data
    else:
        data = 0

    data = int(data)
    return data

def score_tag_CIE(score):
    """
    Function that returns the score label for a given score points value
    """
    if score < 31:
        score_tag = 'Bajo'
    elif 30 < score < 71:
        score_tag = 'Medio'
    elif score > 70:
        score_tag = 'Alto'
    else:
        score_tag = 'sin valor'
    return score_tag

def percentage_to_degrees(percentage):
    if percentage <= 5:
        return [108,0]

    if percentage > 95:
        return [90,360]

    if percentage <= 50:
        print('percentage',percentage)
        deg_two = 0
        deg_one = (((percentage)/5)*18)+90
        print(deg_one)
        return [deg_one, deg_two]

    if percentage > 50:
        deg_one = 90
        deg_two = (((percentage - 50 )/5)*18)+90
        return [deg_one, deg_two]
        
def get_result_descriptions(max_object):
    # Get a dict with the results long whit their descriptions
    result_descriptions = {
        "T": { "percentage":max_object.T*11, "description":"", "category":"Modo de Vida"},
        "V": { "percentage":max_object.V*11, "description":"", "category":"Modo de Vida"},
        "X": { "percentage":max_object.X*11, "description":"", "category":"Naturaleza Social"},
        "S": { "percentage":max_object.S*11, "description":"", "category":"Naturaleza Social"},
        "B": { "percentage":max_object.B*11, "description":"", "category":"Naturaleza Social"},
        "O": { "percentage":max_object.O*11, "description":"", "category":"Naturaleza Social"},
        "R": { "percentage":max_object.R*11, "description":"", "category":"Adaptación al Trabajo"},
        "D": { "percentage":max_object.D*11, "description":"", "category":"Adaptación al Trabajo"},
        "C": { "percentage":max_object.C*11, "description":"", "category":"Adaptación al Trabajo"},
        "Z": { "percentage":max_object.Z*11, "description":"", "category":"Naturaleza Emocional"},
        "E": { "percentage":max_object.E*11, "description":"", "category":"Naturaleza Emocional"},
        "K": { "percentage":max_object.K*11, "description":"", "category":"Naturaleza Emocional"},
        "F": { "percentage":max_object.F*11, "description":"", "category":"Subordinación"},
        "W": { "percentage":max_object.W*11, "description":"", "category":"Subordinación"},
        "N": { "percentage":max_object.N*11, "description":"", "category":"Grado de Energia"},
        "G": { "percentage":max_object.G*11, "description":"", "category":"Grado de Energia"},
        "A": { "percentage":max_object.A*11, "description":"", "category":"Grado de Energia"},
        "L": { "percentage":max_object.L*11, "description":"", "category":"Liderazgo"},
        "P": { "percentage":max_object.P*11, "description":"", "category":"Liderazgo"},
        "I": { "percentage":max_object.I*11, "description":"", "category":"Liderazgo"},
    }

    if result_descriptions["A"]["percentage"] ==0: result_descriptions["A"]["description"]=" Tiene dificultad para terminar lo que inicia, no tiene iniciativa, no encuentra recompensa en el trabajo, realizándose en otros planos."
    if result_descriptions["A"]["percentage"] ==11: result_descriptions["A"]["description"]=" Tiene dificultad para terminar lo que inicia, no tiene iniciativa, no encuentra recompensa en el trabajo, realizándose en otros planos."
    if result_descriptions["A"]["percentage"] ==22: result_descriptions["A"]["description"]=" Tiende a tener dificultades en terminar lo que inicia, necesita ser presionado para realizar su trabajo."
    if result_descriptions["A"]["percentage"] ==33: result_descriptions["A"]["description"]=" No siente preocupación de terminar lo que inicia; no es ambicioso, tiende a no realizarse a través de ejecución de tareas."
    if result_descriptions["A"]["percentage"] ==44: result_descriptions["A"]["description"]=" Siente la necesidad de terminar una tarea cuando la inicia; tiene un grado regular de ambición."
    if result_descriptions["A"]["percentage"] ==55: result_descriptions["A"]["description"]=" Tiene iniciativa. Tiene un grado de ambición regular; se realiza a través del trabajo."
    if result_descriptions["A"]["percentage"] ==66: result_descriptions["A"]["description"]=" Es ambicioso, toma la iniciativa; tiene una necesidad intensa de realizar; tiene el deseo de ser el mejor; fija altos padrones de ejecución."
    if result_descriptions["A"]["percentage"] ==77: result_descriptions["A"]["description"]=" Es ambicioso. Tiene una necesidad intensa de realizar, fija padrones de ejecución muy altos para sí y para los otros; siente la necesidad de ser el mejor."
    if result_descriptions["A"]["percentage"] ==88: result_descriptions["A"]["description"]=" Es muy ambicioso; necesita ser el mejor; tiene una necesidad exagerada de realizar. Tiende a fijar padrones de ejecución irrealísticamente altos."
    if result_descriptions["A"]["percentage"] ==99: result_descriptions["A"]["description"]=" Es exageradamente ambicioso; fija padrones de ejecución extremadamente altos para sí y para los otros, se frustra con facilidad al no conseguir alcanzar los padrones que estipula."
    if result_descriptions["B"]["percentage"] ==0: result_descriptions["B"]["description"]=" Independiente, no presta importancia a la participación en grupos. Tiene opiniones y puntos de vista propios, tiende a entrar en dificultad cuando trabaja en equipo."
    if result_descriptions["B"]["percentage"] ==11: result_descriptions["B"]["description"]=" Independiente, no presta importancia a la participación en grupos. Tiene opiniones y puntos de vista propios, tiende a entrar en dificultad cuando trabaja en equipo."
    if result_descriptions["B"]["percentage"] ==22: result_descriptions["B"]["description"]=" Comportamiento independiente, no se preocupa de estar de acuerdo con los miembros del grupo, no siendo influenciable por las opiniones del mismo. Tiene dificultad en mudar de opinión y de trabajar en equipo."
    if result_descriptions["B"]["percentage"] ==33: result_descriptions["B"]["description"]=" Persona no influenciable por las actitudes y puntos de vista del grupo. es independiente pudiendo entrar en conflicto con las opiniones del grupo."
    if result_descriptions["B"]["percentage"] ==44: result_descriptions["B"]["description"]=" Está en igualdad con el grupo, al mismo tiempo que influencia al grupo puede ceder en sus puntos de vista."
    if result_descriptions["B"]["percentage"] ==55: result_descriptions["B"]["description"]=" Participa del grupo recibiendo cierta influencia, pudiendo influenciarse por las opiniones del grupo."
    if result_descriptions["B"]["percentage"] ==66: result_descriptions["B"]["description"]=" Le agrada escuchar y seguir al grupo. Es influenciables por las actitudes y puntos de vista del grupo."
    if result_descriptions["B"]["percentage"] ==77: result_descriptions["B"]["description"]=" Necesita comportarse de acuerdo con las actitudes y puntos de vista del grupo tendiendo a depender del mismo."
    if result_descriptions["B"]["percentage"] ==88: result_descriptions["B"]["description"]=" Fuertemente influenciable por los puntos de vista y actitudes del grupo. es dependiente de la aprobación del grupo."
    if result_descriptions["B"]["percentage"] ==99: result_descriptions["B"]["description"]=" Es dependiente del grupo. Subordina sus opiniones y actitudes comportándose totalmente de acuerdo con el grupo. Motivado por el trabajo apenas cuando es estimulado por el grupo."
    if result_descriptions["C"]["percentage"] ==0: result_descriptions["C"]["description"]=" Extremadamente desorganizado."
    if result_descriptions["C"]["percentage"] ==11: result_descriptions["C"]["description"]=" Extremadamente desorganizado."
    if result_descriptions["C"]["percentage"] ==22: result_descriptions["C"]["description"]=" Mínima preocupación  de orden y organización."
    if result_descriptions["C"]["percentage"] ==33: result_descriptions["C"]["description"]=" Poca preocupación de orden y organización."
    if result_descriptions["C"]["percentage"] ==44: result_descriptions["C"]["description"]=" Poco organizado."
    if result_descriptions["C"]["percentage"] ==55: result_descriptions["C"]["description"]=" Es una persona con agrado regular de organización."
    if result_descriptions["C"]["percentage"] ==66: result_descriptions["C"]["description"]=" Muy organizado, trata de estar con todo su material siempre en orden."
    if result_descriptions["C"]["percentage"] ==77: result_descriptions["C"]["description"]=" Muy organizado, trata de estar con todo su material siempre en orden."
    if result_descriptions["C"]["percentage"] ==88: result_descriptions["C"]["description"]=" Extremadamente organizado, No consigue trabajar en ambiente desorganizado."
    if result_descriptions["C"]["percentage"] ==99: result_descriptions["C"]["description"]=" Exagerada preocupación con el orden y organización, no consigue trabajar en ambiente desorganizado."
    if result_descriptions["D"]["percentage"] ==0: result_descriptions["D"]["description"]=" No valoriza detalles, corre serie riesgo de no prestar atención a detalles importantes para la corrección de los trabajos."
    if result_descriptions["D"]["percentage"] ==11: result_descriptions["D"]["description"]=" No valoriza detalles, corre serie riesgo de no prestar atención a detalles importantes para la corrección de los trabajos."
    if result_descriptions["D"]["percentage"] ==22: result_descriptions["D"]["description"]=" Trabaja sin detenerse en detalles, tendiendo a perder detalles importantes para el éxito de su trabajo."
    if result_descriptions["D"]["percentage"] ==33: result_descriptions["D"]["description"]=" Poco interés por detalles, prefiriendo la visión del conjunto."
    if result_descriptions["D"]["percentage"] ==44: result_descriptions["D"]["description"]=" Interés personal regular por detalles."
    if result_descriptions["D"]["percentage"] ==55: result_descriptions["D"]["description"]=" Buena capacidad de ver detalles y trabajar con ellos."
    if result_descriptions["D"]["percentage"] ==66: result_descriptions["D"]["description"]=" Le agrada realizar trabajos que exijan atención en detalles."
    if result_descriptions["D"]["percentage"] ==77: result_descriptions["D"]["description"]=" Le agrada realizar trabajos que exijan atención en detalles."
    if result_descriptions["D"]["percentage"] ==88: result_descriptions["D"]["description"]=" Se dedica a eliminar pormenores, perdiendo la visión del conjunto."
    if result_descriptions["D"]["percentage"] ==99: result_descriptions["D"]["description"]=" Gran interés en detalles. Tiende a omitir conceptos importantes y perder la visión del conjunto."
    if result_descriptions["E"]["percentage"] ==0: result_descriptions["E"]["description"]=" Deja reflejar sus emociones en el trabajo, necesitando ser dinámico, se torna completamente envuelto emocionalmente con el trabajo que realiza."
    if result_descriptions["E"]["percentage"] ==11: result_descriptions["E"]["description"]=" Deja reflejar sus emociones en el trabajo, necesitando ser dinámico, se torna completamente envuelto emocionalmente con el trabajo que realiza."
    if result_descriptions["E"]["percentage"] ==22: result_descriptions["E"]["description"]=" Deja reflejar sus emociones, tiene expresión dinámica y dramática; gasta mucha energía cuando trabaja, tornándose emocionalmente envuelto con su trabajo."
    if result_descriptions["E"]["percentage"] ==33: result_descriptions["E"]["description"]=" Tiende a envolverse emocionalmente con su trabajo, es dinámico en su expresión,  dejando reflejar sus emociones."
    if result_descriptions["E"]["percentage"] ==44: result_descriptions["E"]["description"]=" Grado regular de envolvimiento emocional con el trabajo, se esfuerza para que sus emociones no interfieran en el trabajo."
    if result_descriptions["E"]["percentage"] ==55: result_descriptions["E"]["description"]=" Poco envolvimiento emocional en el trabajo, equilibra sus emociones."
    if result_descriptions["E"]["percentage"] ==66: result_descriptions["E"]["description"]=" Tiende a ser calmado y formal en el trabajo, controla sus emociones."
    if result_descriptions["E"]["percentage"] ==77: result_descriptions["E"]["description"]=" Es calmado y formal en el trabajo, contiene sus emociones difícilmente demuestra lo que está sintiendo."
    if result_descriptions["E"]["percentage"] ==88: result_descriptions["E"]["description"]=" Es frío y formal en el trabajo; característicamente racional; no demuestra lo que siente, tiende a esconder sus emociones, no dando valor a personas emotivas."
    if result_descriptions["E"]["percentage"] ==99: result_descriptions["E"]["description"]=" Es racional y formal en su trabajo, racionalizando sus emociones, no se permite demostraciones afectivas en el trabajo. No consigue trabajar con personas emotivas."
    if result_descriptions["F"]["percentage"] ==0: result_descriptions["F"]["description"]=" Es rebelde ante la autoridad. Necesita sentirse libre y exento de control de la jefatura; su opinión respecto de su trabajo es el factor que lo motiva y no la opinión de la jefatura."
    if result_descriptions["F"]["percentage"] ==11: result_descriptions["F"]["description"]=" Es rebelde ante la autoridad. Necesita sentirse libre y exento de control de la jefatura; su opinión respecto de su trabajo es el factor que lo motiva y no la opinión de la jefatura."
    if result_descriptions["F"]["percentage"] ==22: result_descriptions["F"]["description"]=" Comportamiento independiente, poca preocupación en estar de acuerdo con la autoridad, eventualmente enfrenta a la autoridad y prefiere no recibir supervisión."
    if result_descriptions["F"]["percentage"] ==33: result_descriptions["F"]["description"]=" Auto-confiado y motivado por el trabajo y no por el reconocimiento del jefe. No necesita del incentivo del jefe. Tiende a ser resistente a la autoridad. Se siente libre para expresar sus puntos de vista."
    if result_descriptions["F"]["percentage"] ==44: result_descriptions["F"]["description"]=" Tiene confianza en sí mismo, no dependiendo del control de la jefatura, eventualmente puede argumentar con la jefatura."
    if result_descriptions["F"]["percentage"] ==55: result_descriptions["F"]["description"]=" Tiene confianza en sí mismo, conviviendo en igualdad con la autoridad."
    if result_descriptions["F"]["percentage"] ==66: result_descriptions["F"]["description"]=" Influenciable por las opiniones y puntos de vista de sus superiores; trata de corresponder a la expectativa  de su superiores."
    if result_descriptions["F"]["percentage"] ==77: result_descriptions["F"]["description"]=" Necesita obedecer al jefe para recibir estímulos que lo motiven."
    if result_descriptions["F"]["percentage"] ==88: result_descriptions["F"]["description"]=" Se preocupa mucho en respetar y obedecer al jefe, tratando de asegurarse del valor de su trabajo."
    if result_descriptions["F"]["percentage"] ==99: result_descriptions["F"]["description"]=" No tiene confianza en sí mismo, depende del apoyo de su jefe para poder trabajar. Necesita ser constantemente motivado por la autoridad."
    if result_descriptions["G"]["percentage"] ==0: result_descriptions["G"]["description"]=" No le agradan trabajos que exijan esfuerzo, puede dejar para el día siguiente lo que podía hacer hoy."
    if result_descriptions["G"]["percentage"] ==11: result_descriptions["G"]["description"]=" No le agradan trabajos que exijan esfuerzo, puede dejar para el día siguiente lo que podía hacer hoy."
    if result_descriptions["G"]["percentage"] ==22: result_descriptions["G"]["description"]=" Dedica poco esfuerzo a la realización de sus trabajos."
    if result_descriptions["G"]["percentage"] ==33: result_descriptions["G"]["description"]=" Le agrada realizar trabajos que no exijan esfuerzo para ser realizados."
    if result_descriptions["G"]["percentage"] ==44: result_descriptions["G"]["description"]=" Identificación regular con trabajos difíciles. "
    if result_descriptions["G"]["percentage"] ==55: result_descriptions["G"]["description"]=" Identificación regular con trabajos difíciles. "
    if result_descriptions["G"]["percentage"] ==66: result_descriptions["G"]["description"]=" Identificación sobre regular con trabajos difíciles."
    if result_descriptions["G"]["percentage"] ==77: result_descriptions["G"]["description"]=" Prefiere trabajos que exijan esfuerzo para ser realizado."
    if result_descriptions["G"]["percentage"] ==88: result_descriptions["G"]["description"]=" Es bastante dedicado al trabajo que exige esfuerzo para ser realizado."
    if result_descriptions["G"]["percentage"] ==99: result_descriptions["G"]["description"]=" Es extremadamente dedicado a trabajos que exigen esfuerzos para ser realizados."
    if result_descriptions["I"]["percentage"] ==0: result_descriptions["I"]["description"]=" Siente dificultad para decidirse, el proceso de decisión le crea angustia y malestar; no le agrada tomar decisiones."
    if result_descriptions["I"]["percentage"] ==11: result_descriptions["I"]["description"]=" Siente dificultad para decidirse, el proceso de decisión le crea angustia y malestar; no le agrada tomar decisiones."
    if result_descriptions["I"]["percentage"] ==22: result_descriptions["I"]["description"]=" Es lento en la toma de decisiones. Se preocupa mucho por la calidad de la decisión ( tiende a dejar de tomar decisiones )."
    if result_descriptions["I"]["percentage"] ==33: result_descriptions["I"]["description"]=" Piensa para decidirse; tiende a ser reflexivo, es lento en el proceso de toma de decisiones."
    if result_descriptions["I"]["percentage"] ==44: result_descriptions["I"]["description"]=" Grado regular de capacidad para decidirse."
    if result_descriptions["I"]["percentage"] ==55: result_descriptions["I"]["description"]=" Buena capacidad para decidirse; trata de imprimir en sus decisiones el mismo grado de calidad y rapidez."
    if result_descriptions["I"]["percentage"] ==66: result_descriptions["I"]["description"]=" Toma decisiones con facilidad sin, entretanto, apresurarse en dejar de medir las consecuencias de sus decisiones."
    if result_descriptions["I"]["percentage"] ==77: result_descriptions["I"]["description"]=" Rápido para decidirse; se preocupa poco de las consecuencias de sus decisiones, dando más énfasis a la velocidad en la toma de las mismas."
    if result_descriptions["I"]["percentage"] ==88: result_descriptions["I"]["description"]=" Impulsivo, da más énfasis a la velocidad que a la seguridad de la decisiones. Puede tomar decisiones apresuradas."
    if result_descriptions["I"]["percentage"] ==99: result_descriptions["I"]["description"]=" Extremadamente rápido para decidirse; corre el riesgo de tomar decisiones no pensadas."
    if result_descriptions["K"]["percentage"] ==0: result_descriptions["K"]["description"]=" No manifiesta sus opiniones francamente, estando a la defensiva casi siempre."
    if result_descriptions["K"]["percentage"] ==11: result_descriptions["K"]["description"]=" No manifiesta sus opiniones francamente, estando a la defensiva casi siempre."
    if result_descriptions["K"]["percentage"] ==22: result_descriptions["K"]["description"]=" Está a la defensiva la mayor parte del tiempo, difícilmente se manifiesta abiertamente."
    if result_descriptions["K"]["percentage"] ==33: result_descriptions["K"]["description"]=" Posee reserva en la manifestación de su s opiniones. Tiende a estar en la defensiva."
    if result_descriptions["K"]["percentage"] ==44: result_descriptions["K"]["description"]=" Tiende a estar a la defensiva con las personas."
    if result_descriptions["K"]["percentage"] ==55: result_descriptions["K"]["description"]=" Grado medio de defensa, tiende a ser reservado."
    if result_descriptions["K"]["percentage"] ==66: result_descriptions["K"]["description"]=" Capacidad para enfrentar y argumentar con las personas."
    if result_descriptions["K"]["percentage"] ==77: result_descriptions["K"]["description"]=" Enfrenta las personas, es abierto y sincero."
    if result_descriptions["K"]["percentage"] ==88: result_descriptions["K"]["description"]=" Persona que se opone y enfrenta franca y abiertamente a los otros."
    if result_descriptions["K"]["percentage"] ==99: result_descriptions["K"]["description"]=" Persona que se opone y enfrenta franca y abiertamente a los otros."
    if result_descriptions["L"]["percentage"] ==0: result_descriptions["L"]["description"]=" No acepta el papel de líder, prefiere ser liderado a liderar, en posición de jefatura, tiende a evitar el liderazgo."
    if result_descriptions["L"]["percentage"] ==11: result_descriptions["L"]["description"]=" No acepta el papel de líder, prefiere ser liderado a liderar, en posición de jefatura, tiende a evitar el liderazgo."
    if result_descriptions["L"]["percentage"] ==22: result_descriptions["L"]["description"]=" Tiene problemas con liderazgo. Prefiere ser orientado por los otros . No obtiene suficiente recompensa interior en el papel de liderazgo."
    if result_descriptions["L"]["percentage"] ==33: result_descriptions["L"]["description"]=" No obtiene suficiente recompensa interior como líder, tiende a transferir los problemas de liderazgo."
    if result_descriptions["L"]["percentage"] ==44: result_descriptions["L"]["description"]=" Grado medio de confianza en sí mismo como líder, pudiendo igualmente ejercer el liderazgo y ser liderado."
    if result_descriptions["L"]["percentage"] ==55: result_descriptions["L"]["description"]=" Confía en sí mismo como líder, tiende a ejercer el liderazgo."
    if result_descriptions["L"]["percentage"] ==66: result_descriptions["L"]["description"]=" Le agrada liderar es una persona que asume el liderazgo del grupo."
    if result_descriptions["L"]["percentage"] ==77: result_descriptions["L"]["description"]=" Tiene confianza en sí como líder; le agrada tomar el liderazgo del grupo."
    if result_descriptions["L"]["percentage"] ==88: result_descriptions["L"]["description"]=" Muy confiado como líder; es considerado como un líder en el grupo."
    if result_descriptions["L"]["percentage"] ==99: result_descriptions["L"]["description"]="  Es impulsado por un fuerte deseo de liderazgo. Es auto-confiante a punto de tomar frecuentemente el liderazgo."
    if result_descriptions["N"]["percentage"] ==0: result_descriptions["N"]["description"]=" Persona que se preocupa principalmente en fijar objetivos y metas, no sintiendo ninguna necesidad en acabar lo que inicia. Necesita realizar muchas tareas simultáneamente, pudiendo dejar trabajos incompletos."
    if result_descriptions["N"]["percentage"] ==11: result_descriptions["N"]["description"]=" Persona que se preocupa principalmente en fijar objetivos y metas, no sintiendo ninguna necesidad en acabar lo que inicia. Necesita realizar muchas tareas simultáneamente, pudiendo dejar trabajos incompletos."
    if result_descriptions["N"]["percentage"] ==22: result_descriptions["N"]["description"]=" Persona que no siente la necesidad de completar tareas personalmente, prefiere descentralizar los trabajos para permanecer en una actividad de  coordinación."
    if result_descriptions["N"]["percentage"] ==33: result_descriptions["N"]["description"]=" Puede delegar sus trabajos. Puede realizar muchas tareas simultáneamente.   "
    if result_descriptions["N"]["percentage"] ==44: result_descriptions["N"]["description"]=" Puede delegar sus trabajos. Puede realizar algunas tareas simultáneamente."
    if result_descriptions["N"]["percentage"] ==55: result_descriptions["N"]["description"]=" Puede delegar parte de sus trabajos, dejando para sí la realización completa de buena parte de ella."
    if result_descriptions["N"]["percentage"] ==66: result_descriptions["N"]["description"]=" Tiene necesidad de  completar sus tareas."
    if result_descriptions["N"]["percentage"] ==77: result_descriptions["N"]["description"]=" Necesita mucho terminar lo que comienza; fija toda su atención en la realización de una tarea hasta terminarla."
    if result_descriptions["N"]["percentage"] ==88: result_descriptions["N"]["description"]=" Persistente. Tiene dificultad en dejar la tarea que está haciendo. Tiene que completar lo que comienza. Siente dificultad en delegar."
    if result_descriptions["N"]["percentage"] ==99: result_descriptions["N"]["description"]=" No consigue dejar lo que está haciendo. Es extremadamente preocupado con la necesidad de completar una tarea. Queda frustrado y ansioso al no terminar lo que inicia. Siente mucha dificultad para delegar."
    if result_descriptions["O"]["percentage"] ==0: result_descriptions["O"]["description"]=" Dificultad en su relacionamiento, es muy formal.  "
    if result_descriptions["O"]["percentage"] ==11: result_descriptions["O"]["description"]=" Tiene un modo racional de abordar las cosas (intelectualizada) cierta dificultad de relacionamiento."
    if result_descriptions["O"]["percentage"] ==23: result_descriptions["O"]["description"]=" Mantiene un relacionamiento formal con las personas."
    if result_descriptions["O"]["percentage"] ==33: result_descriptions["O"]["description"]=" Mantiene un relacionamiento formal con las personas."
    if result_descriptions["O"]["percentage"] ==44: result_descriptions["O"]["description"]=" Le agrada pertenecer al grupo y participar con otras personas."
    if result_descriptions["O"]["percentage"] ==55: result_descriptions["O"]["description"]=" Se relaciona cálidamente con las personas."
    if result_descriptions["O"]["percentage"] ==66: result_descriptions["O"]["description"]=" Persona que le agrada recibir el afecto de los otros."
    if result_descriptions["O"]["percentage"] ==77: result_descriptions["O"]["description"]=" Necesita tener el afecto y apoyo de los otros."
    if result_descriptions["O"]["percentage"] ==88: result_descriptions["O"]["description"]=" Sensible, necesita obtener el afecto y apoyo de los otros en su relacionamiento."
    if result_descriptions["O"]["percentage"] ==99: result_descriptions["O"]["description"]=" Es extremadamente afectivo en su relacionamiento; siente la necesidad de ser querido."
    if result_descriptions["P"]["percentage"] ==0: result_descriptions["P"]["description"]=" No le agrada asumir responsabilidad por terceros, tiene dificultad en controlar a los otros."
    if result_descriptions["P"]["percentage"] ==11: result_descriptions["P"]["description"]=" No le agrada asumir responsabilidad por terceros, tiene dificultad en controlar a los otros."
    if result_descriptions["P"]["percentage"] ==22: result_descriptions["P"]["description"]=" Se inclina por sí mismo, poco interés en controlar personas, tiene dificultad en controlar a los otros."
    if result_descriptions["P"]["percentage"] ==33: result_descriptions["P"]["description"]=" Prefiere no responsabilizarse por los otros. Tiende a no controlar a los otros."
    if result_descriptions["P"]["percentage"] ==44: result_descriptions["P"]["description"]="  Agrado de sí mismo y respeta a los otros. Grado regular de preocupación en controlar a los otros."
    if result_descriptions["P"]["percentage"] ==55: result_descriptions["P"]["description"]=" Se interesa por las personas, pudiendo eventualmente manejarlas, a través de la imagen de protector."
    if result_descriptions["P"]["percentage"] ==66: result_descriptions["P"]["description"]=" Le agrada influenciar a las personas transmitiéndoles sus puntos de vista."
    if result_descriptions["P"]["percentage"] ==77: result_descriptions["P"]["description"]=" Le agrada ser responsable de las personas; necesita influenciar a los otros."
    if result_descriptions["P"]["percentage"] ==88: result_descriptions["P"]["description"]=" Se preocupa de orientar y dirigir a las personas, controlándolas de acuerdo con sus puntos de vista."
    if result_descriptions["P"]["percentage"] ==99: result_descriptions["P"]["description"]="  Persona fuertemente dominante. Se preocupa de dirigir a las personas según su voluntad."
    if result_descriptions["R"]["percentage"] ==0: result_descriptions["R"]["description"]=" Ninguna preocupación en planificación."
    if result_descriptions["R"]["percentage"] ==11: result_descriptions["R"]["description"]=" Ejecuta los trabajos sin planificar."
    if result_descriptions["R"]["percentage"] ==22: result_descriptions["R"]["description"]=" Tiene dificultades en planificar sus trabajos, prefiriendo ejecutar a planificar."
    if result_descriptions["R"]["percentage"] ==33: result_descriptions["R"]["description"]=" Prefiere ejecutar a planificar."
    if result_descriptions["R"]["percentage"] ==44: result_descriptions["R"]["description"]=" Prefiere planificar y formular estrategias 40 a 50% del tiempo."
    if result_descriptions["R"]["percentage"] ==55: result_descriptions["R"]["description"]=" Prefiere planificar y formular estrategias 40 a 50% del tiempo."
    if result_descriptions["R"]["percentage"] ==66: result_descriptions["R"]["description"]=" Prefiere planificar y formular estrategias 70% del tiempo."
    if result_descriptions["R"]["percentage"] ==77: result_descriptions["R"]["description"]=" Prefiere planificar y formular estrategias 70% del tiempo."
    if result_descriptions["R"]["percentage"] ==88: result_descriptions["R"]["description"]=" Gasta la mayor parte del tiempo, 80 a 90%, planificando y formulando estrategias."
    if result_descriptions["R"]["percentage"] ==99: result_descriptions["R"]["description"]="  Gasta la totalidad de su tiempo planificando, tiene dificultades en ejecutar tareas."
    if result_descriptions["S"]["percentage"] ==0: result_descriptions["S"]["description"]=" Persona introvertida, sin preocupación por la comunicación social. Socialmente sin condición."
    if result_descriptions["S"]["percentage"] ==11: result_descriptions["S"]["description"]=" Persona introvertida, sin preocupación por la comunicación social. Socialmente sin condición."
    if result_descriptions["S"]["percentage"] ==22: result_descriptions["S"]["description"]=" Es una persona reservada en su relacionamiento social."
    if result_descriptions["S"]["percentage"] ==33: result_descriptions["S"]["description"]=" Posee cierta reserva en la comunicación social."
    if result_descriptions["S"]["percentage"] ==44: result_descriptions["S"]["description"]=" Preocupación regular (50%) con la comunicación social."
    if result_descriptions["S"]["percentage"] ==55: result_descriptions["S"]["description"]=" Buena capacidad de escuchar y comunicarse socialmente."
    if result_descriptions["S"]["percentage"] ==66: result_descriptions["S"]["description"]=" Posee buen relacionamiento social."
    if result_descriptions["S"]["percentage"] ==77: result_descriptions["S"]["description"]=" Buena disposición social. Persona muy receptiva."
    if result_descriptions["S"]["percentage"] ==88: result_descriptions["S"]["description"]=" Persona extrovertida, con óptima capacidad de comunicación."
    if result_descriptions["S"]["percentage"] ==99: result_descriptions["S"]["description"]=" Persona muy participativa y receptiva a la comunicación."
    if result_descriptions["T"]["percentage"] ==0: result_descriptions["T"]["description"]=" No le agrada trabajar con presión de plazos, tiende a no dar importancia al tiempo establecido."
    if result_descriptions["T"]["percentage"] ==11: result_descriptions["T"]["description"]=" No le agrada trabajar con presión de plazos, tiende a no dar importancia al tiempo establecido."
    if result_descriptions["T"]["percentage"] ==22: result_descriptions["T"]["description"]=" Trabaja calmadamente, poco preocupado en cuanto a límites de tiempo, tiene dificultad en manejar plazos pre - establecidos, no se siente bien con trabajos que exijan plazos pre - establecidos."
    if result_descriptions["T"]["percentage"] ==33: result_descriptions["T"]["description"]=" Se preocupa eventualmente por los límites de tiempo, prefiriendo no trabajar en base a presión de plazos."
    if result_descriptions["T"]["percentage"] ==44: result_descriptions["T"]["description"]=" Es responsable en cuanto a límites de tiempo. Tiende a ejecutar sus deberes dentro de los plazos determinados."
    if result_descriptions["T"]["percentage"] ==55: result_descriptions["T"]["description"]=" Se preocupa por lo límites de tiempo. Trabaja dentro de los límites de tiempo establecidos."
    if result_descriptions["T"]["percentage"] ==66: result_descriptions["T"]["description"]=" Responsabilidad sobre regular en cuanto a límites de tiempo."
    if result_descriptions["T"]["percentage"] ==77: result_descriptions["T"]["description"]=" Es una persona inquieta y muy preocupada con plazos, tiene mucha necesidad de realizar sus trabajos dentro de los límites de tiempo."
    if result_descriptions["T"]["percentage"] ==88: result_descriptions["T"]["description"]=" Posee mucha tensión interna. Fuertemente preocupado con los límites de tiempo.   "
    if result_descriptions["T"]["percentage"] ==99: result_descriptions["T"]["description"]=" Persona que esta permanentemente tensa y fuertemente impulsada a trabajar dentro de los límites de tiempo."
    if result_descriptions["V"]["percentage"] ==0: result_descriptions["V"]["description"]=" No le agradan trabajos que exijan movimiento; necesita actividades que pueden ser realizadas sentadas."
    if result_descriptions["V"]["percentage"] ==11: result_descriptions["V"]["description"]=" No le agradan trabajos que exijan movimiento; necesita actividades que pueden ser realizadas sentadas."
    if result_descriptions["V"]["percentage"] ==22: result_descriptions["V"]["description"]=" Prefiere trabajos que pueden ser realizados sentado."
    if result_descriptions["V"]["percentage"] ==33: result_descriptions["V"]["description"]=" Poco interés en actividades que exijan movimiento. Prefiere trabajar sentado."
    if result_descriptions["V"]["percentage"] ==44: result_descriptions["V"]["description"]=" Grado regular de vigor físico. Tiende a preferir funciones que exijan movimiento limitado."
    if result_descriptions["V"]["percentage"] ==55: result_descriptions["V"]["description"]=" Grado regular de vigor físico. Tiende a preferir funciones que exijan movimiento limitado."
    if result_descriptions["V"]["percentage"] ==66: result_descriptions["V"]["description"]=" Le agrada estar en movimiento."
    if result_descriptions["V"]["percentage"] ==77: result_descriptions["V"]["description"]=" Necesita estar en constante movimiento."
    if result_descriptions["V"]["percentage"] ==88: result_descriptions["V"]["description"]=" Es muy dinámico, tiene dificultad en realizar actividades que lo obliguen a estar parado en un ambiente."
    if result_descriptions["V"]["percentage"] ==99: result_descriptions["V"]["description"]=" Es extremadamente inquieto, necesita realizar actividades que exijan bastante movimiento."
    if result_descriptions["W"]["percentage"] ==0: result_descriptions["W"]["description"]=" No le agrada seguir reglamentos, le agrada ir y venir libremente, es auto-dirigido, no le agrada ser orientado."
    if result_descriptions["W"]["percentage"] ==11: result_descriptions["W"]["description"]=" No le agrada seguir reglamentos, le agrada ir y venir libremente, es auto-dirigido, no le agrada ser orientado."
    if result_descriptions["W"]["percentage"] ==22: result_descriptions["W"]["description"]=" Persona que prefiere no seguir normas. Le agrada ser libre. Prefiere auto-dirigirse a ser orientado."
    if result_descriptions["W"]["percentage"] ==33: result_descriptions["W"]["description"]=" Poca necesidad de reglamentos y normas, prefiere recibir supervisión apenas ocasionalmente."
    if result_descriptions["W"]["percentage"] ==44: result_descriptions["W"]["description"]=" Regular interés por seguir normas y reglamentos."
    if result_descriptions["W"]["percentage"] ==55: result_descriptions["W"]["description"]=" Le agrada seguir reglamentos y obtener 'la palabra oficial'."
    if result_descriptions["W"]["percentage"] ==66: result_descriptions["W"]["description"]=" Le agrada seguir normas y reglamentos."
    if result_descriptions["W"]["percentage"] ==77: result_descriptions["W"]["description"]=" Necesita respetar normas y reglamentos."
    if result_descriptions["W"]["percentage"] ==88: result_descriptions["W"]["description"]=" Se preocupa mucho en respetar normas y reglamentos."
    if result_descriptions["W"]["percentage"] ==99: result_descriptions["W"]["description"]=" Necesita de normas y reglamentos para poder trabajar."
    if result_descriptions["X"]["percentage"] ==0: result_descriptions["X"]["description"]=" Prefiere mantenerse reservado, le agrada pasar desapercibido. No le agrada ser el centro de las atenciones."
    if result_descriptions["X"]["percentage"] ==11: result_descriptions["X"]["description"]=" Prefiere mantenerse reservado, le agrada pasar desapercibido. No le agrada ser el centro de las atenciones."
    if result_descriptions["X"]["percentage"] ==22: result_descriptions["X"]["description"]=" Es reservado en sus contactos sociales, tiende a no sentirse bien cuando es el centro de las atenciones."
    if result_descriptions["X"]["percentage"] ==33: result_descriptions["X"]["description"]=" Es sincero en sus contactos sociales."
    if result_descriptions["X"]["percentage"] ==44: result_descriptions["X"]["description"]=" Grado regular de solicitud , tiende a saber escuchar a las personas."
    if result_descriptions["X"]["percentage"] ==55: result_descriptions["X"]["description"]=" Es solícito buscando amistad en el apoyo de los otros."
    if result_descriptions["X"]["percentage"] ==66: result_descriptions["X"]["description"]=" Persona que le agrada recibir atención de los otros y de ser notado."
    if result_descriptions["X"]["percentage"] ==77: result_descriptions["X"]["description"]=" Le agrada hablar respecto de sus actividades con el fin de sentirse valorizado y aceptado."
    if result_descriptions["X"]["percentage"] ==88: result_descriptions["X"]["description"]=" Necesita sentirse valorizado por las personas, llamando la atención sobre sí mismo."
    if result_descriptions["X"]["percentage"] ==99: result_descriptions["X"]["description"]="  Exageradamente dependiente de las opiniones de los otros, trata de hacerse notar en el grupo en el cual se encuentra."
    if result_descriptions["Z"]["percentage"] ==0: result_descriptions["Z"]["description"]=" Tiene gran dificultad para enfrentar nuevas situaciones y cambios; necesita trabajos rutinarios y repetidos en situaciones estables e inmutables."
    if result_descriptions["Z"]["percentage"] ==11: result_descriptions["Z"]["description"]=" Tiene gran dificultad para enfrentar nuevas situaciones y cambios; necesita trabajos rutinarios y repetidos en situaciones estables e inmutables."
    if result_descriptions["Z"]["percentage"] ==22: result_descriptions["Z"]["description"]=" Resistente a las mudanzas, es más indicado para trabajos de rutina y repetidos."
    if result_descriptions["Z"]["percentage"] ==33: result_descriptions["Z"]["description"]=" Posee cierta reserva a los cambios. Prefiere trabajos de rutina y repetidos."
    if result_descriptions["Z"]["percentage"] ==44: result_descriptions["Z"]["description"]=" Medianamente receptivo a los cambios, dependiendo de las circunstancias que las envuelven, puede ofrecer resistencia a los mismos."
    if result_descriptions["Z"]["percentage"] ==55: result_descriptions["Z"]["description"]=" Receptivo a los cambios. Se ajusta a los mismos."
    if result_descriptions["Z"]["percentage"] ==66: result_descriptions["Z"]["description"]=" Se ajusta fácilmente a los cambios; tiene flexibilidad de pensamiento."
    if result_descriptions["Z"]["percentage"] ==77: result_descriptions["Z"]["description"]=" Necesita variar sus actividades, identificándose con cambios y con lo que es nuevo. Prefiere trabajos que exijan creatividad."
    if result_descriptions["Z"]["percentage"] ==88: result_descriptions["Z"]["description"]=" Es impulsado a mudar frecuentemente sus preferencias, necesita cambios continuamente en el trabajo."
    if result_descriptions["Z"]["percentage"] ==99: result_descriptions["Z"]["description"]=" Es impulsado por una fuerte necesidad de cambiar constantemente sus actividades, siendo inconstante en sus preferencias y actividades."

    return result_descriptions