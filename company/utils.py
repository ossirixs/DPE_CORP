

def get_integrity_export_data(test_result):
	""" 
	Get structured data from the Integrity test for the xlsx export report.
	"""

	# Addictions percentage
	if test_result.adictions > 67 : addiction_percentage = 99
	if test_result.adictions <= 67 : addiction_percentage = 99
	if test_result.adictions <= 61 : addiction_percentage = 95
	if test_result.adictions <= 58 : addiction_percentage = 90
	if test_result.adictions <= 56 : addiction_percentage = 85
	if test_result.adictions <= 54 : addiction_percentage = 80
	if test_result.adictions <= 53 : addiction_percentage = 75
	if test_result.adictions <= 51 : addiction_percentage = 70
	if test_result.adictions <= 50 : addiction_percentage = 65
	if test_result.adictions <= 49 : addiction_percentage = 60
	if test_result.adictions <= 47 : addiction_percentage = 55
	if test_result.adictions <= 46 : addiction_percentage = 50
	if test_result.adictions <= 45 : addiction_percentage = 45
	if test_result.adictions <= 44 : addiction_percentage = 40
	if test_result.adictions <= 42 : addiction_percentage = 35
	if test_result.adictions <= 41 : addiction_percentage = 30
	if test_result.adictions <= 39 : addiction_percentage = 25
	if test_result.adictions <= 36 : addiction_percentage = 20
	if test_result.adictions <= 32 : addiction_percentage = 15
	if test_result.adictions <= 29 : addiction_percentage = 10
	if test_result.adictions <= 23 : addiction_percentage = 5
	if test_result.adictions <= 7 : addiction_percentage = 1

	if addiction_percentage >= 51:
		adictions_score = "Aprobado"
	elif addiction_percentage <= 30:
		adictions_score = "Reprobado"
	else:
		adictions_score = "Aprobado con Reservas"

	# Judgement percentage
	if test_result.judgement > 71 : judgement_percentage = 99
	if test_result.judgement <= 71 : judgement_percentage = 99
	if test_result.judgement <= 69 : judgement_percentage = 95
	if test_result.judgement <= 66 : judgement_percentage = 90
	if test_result.judgement <= 63 : judgement_percentage = 85
	if test_result.judgement <= 62 : judgement_percentage = 80
	if test_result.judgement <= 60 : judgement_percentage = 75
	if test_result.judgement <= 59 : judgement_percentage = 70
	if test_result.judgement <= 58 : judgement_percentage = 65
	if test_result.judgement <= 56 : judgement_percentage = 60
	if test_result.judgement <= 55 : judgement_percentage = 55
	if test_result.judgement <= 54 : judgement_percentage = 50
	if test_result.judgement <= 52 : judgement_percentage = 45
	if test_result.judgement <= 50 : judgement_percentage = 40
	if test_result.judgement <= 48 : judgement_percentage = 35
	if test_result.judgement <= 46 : judgement_percentage = 30
	if test_result.judgement <= 44 : judgement_percentage = 25
	if test_result.judgement <= 42 : judgement_percentage = 20
	if test_result.judgement <= 39 : judgement_percentage = 15
	if test_result.judgement <= 34 : judgement_percentage = 10
	if test_result.judgement <= 29 : judgement_percentage = 5
	if test_result.judgement <= 6 : judgement_percentage = 1
		
	if judgement_percentage >= 51:
		judgement_score = "Aprobado"
	elif judgement_percentage <= 30:
		judgement_score = "Reprobado"
	else:
		judgement_score = "Aprobado con Reservas"

	# Discipline percentage
	if test_result.discipline > 55 : discipline_percentage = 99
	if test_result.discipline <= 55 : discipline_percentage = 99
	if test_result.discipline <= 52 : discipline_percentage = 95
	if test_result.discipline <= 49 : discipline_percentage = 90
	if test_result.discipline <= 47 : discipline_percentage = 85
	if test_result.discipline <= 45 : discipline_percentage = 80
	if test_result.discipline <= 42 : discipline_percentage = 75
	if test_result.discipline <= 40 : discipline_percentage = 70
	if test_result.discipline <= 39 : discipline_percentage = 65
	if test_result.discipline <= 37 : discipline_percentage = 60
	if test_result.discipline <= 35 : discipline_percentage = 55
	if test_result.discipline <= 34 : discipline_percentage = 50
	if test_result.discipline <= 33 : discipline_percentage = 45
	if test_result.discipline <= 31 : discipline_percentage = 40
	if test_result.discipline <= 29 : discipline_percentage = 35
	if test_result.discipline <= 27 : discipline_percentage = 30
	if test_result.discipline <= 24 : discipline_percentage = 25
	if test_result.discipline <= 22 : discipline_percentage = 20
	if test_result.discipline <= 20 : discipline_percentage = 15
	if test_result.discipline <= 15 : discipline_percentage = 10
	if test_result.discipline <= 11 : discipline_percentage = 5
	if test_result.discipline <= 5 : discipline_percentage = 1

	if discipline_percentage >= 61:
		discipline_score = "Aprobado"
	elif discipline_percentage <= 50:
		discipline_score = "Reprobado"
	else:
		discipline_score = "Aprobado con Reservas"

	# Veracity percentage
	if test_result.veracity > 108 : veracity_percentage = 99
	if test_result.veracity <= 108 : veracity_percentage = 99
	if test_result.veracity <= 93 : veracity_percentage = 95
	if test_result.veracity <= 89 : veracity_percentage = 90
	if test_result.veracity <= 87 : veracity_percentage = 85
	if test_result.veracity <= 84 : veracity_percentage = 80
	if test_result.veracity <= 82 : veracity_percentage = 75
	if test_result.veracity <= 80 : veracity_percentage = 70
	if test_result.veracity <= 79 : veracity_percentage = 65
	if test_result.veracity <= 77 : veracity_percentage = 60
	if test_result.veracity <= 76 : veracity_percentage = 55
	if test_result.veracity <= 75 : veracity_percentage = 50
	if test_result.veracity <= 73 : veracity_percentage = 45
	if test_result.veracity <= 72 : veracity_percentage = 40
	if test_result.veracity <= 70 : veracity_percentage = 35
	if test_result.veracity <= 68 : veracity_percentage = 30
	if test_result.veracity <= 65 : veracity_percentage = 25
	if test_result.veracity <= 62 : veracity_percentage = 20
	if test_result.veracity <= 57 : veracity_percentage = 15
	if test_result.veracity <= 52 : veracity_percentage = 10
	if test_result.veracity <= 42 : veracity_percentage = 5
	if test_result.veracity <= 10 : veracity_percentage = 1

	if veracity_percentage >= 61:
		veracity_score = "Aprobado"
	elif veracity_percentage <= 50:
		veracity_score = "Reprobado"
	else:
		veracity_score = "Aprobado con Reservas"

	# Loyalty percentage
	if test_result.loyalty > 33 : loyalty_percentage = 99
	if test_result.loyalty <= 33 : loyalty_percentage = 99
	if test_result.loyalty <= 32 : loyalty_percentage = 95
	if test_result.loyalty <= 31 : loyalty_percentage = 90
	if test_result.loyalty <= 30 : loyalty_percentage = 85
	if test_result.loyalty <= 29 : loyalty_percentage = 75
	if test_result.loyalty <= 28 : loyalty_percentage = 70
	if test_result.loyalty <= 27 : loyalty_percentage = 60
	if test_result.loyalty <= 26 : loyalty_percentage = 55
	if test_result.loyalty <= 25 : loyalty_percentage = 45
	if test_result.loyalty <= 24 : loyalty_percentage = 35
	if test_result.loyalty <= 23 : loyalty_percentage = 30
	if test_result.loyalty <= 22 : loyalty_percentage = 25
	if test_result.loyalty <= 21 : loyalty_percentage = 20
	if test_result.loyalty <= 19 : loyalty_percentage = 15
	if test_result.loyalty <= 17 : loyalty_percentage = 10
	if test_result.loyalty <= 13 : loyalty_percentage = 5
	if test_result.loyalty <= 2 : loyalty_percentage = 1

	if loyalty_percentage > 61:
		loyalty_score = "Aprobado"
	elif loyalty_percentage < 50:
		loyalty_score = "Reprobado"
	else:
		loyalty_score = "Aprobado con Reservas"

	# Intentionality percentage
	if test_result.intentionality > 201 : intentionality_percentage = 99
	if test_result.intentionality <= 201 : intentionality_percentage = 99
	if test_result.intentionality <= 190 : intentionality_percentage = 95
	if test_result.intentionality <= 185 : intentionality_percentage = 90
	if test_result.intentionality <= 180 : intentionality_percentage = 85
	if test_result.intentionality <= 176 : intentionality_percentage = 80
	if test_result.intentionality <= 172 : intentionality_percentage = 75
	if test_result.intentionality <= 168 : intentionality_percentage = 70
	if test_result.intentionality <= 166 : intentionality_percentage = 65
	if test_result.intentionality <= 163 : intentionality_percentage = 60
	if test_result.intentionality <= 160 : intentionality_percentage = 55
	if test_result.intentionality <= 156 : intentionality_percentage = 50
	if test_result.intentionality <= 152 : intentionality_percentage = 45
	if test_result.intentionality <= 149 : intentionality_percentage = 40
	if test_result.intentionality <= 146 : intentionality_percentage = 35
	if test_result.intentionality <= 143 : intentionality_percentage = 30
	if test_result.intentionality <= 139 : intentionality_percentage = 25
	if test_result.intentionality <= 132 : intentionality_percentage = 20
	if test_result.intentionality <= 124 : intentionality_percentage = 15
	if test_result.intentionality <= 108 : intentionality_percentage = 10
	if test_result.intentionality <= 68 : intentionality_percentage = 5
	if test_result.intentionality <= 21 : intentionality_percentage = 1

	if intentionality_percentage >= 61:
		intentionality_score = "Aprobado"
	elif intentionality_percentage <= 50:
		intentionality_score = "Reprobado"
	else:
		intentionality_score = "Aprobado con Reservas"

	# Ethic percentage
	if test_result.ethic > 146 : ethic_percentage = 99
	if test_result.ethic <= 146 : ethic_percentage = 99
	if test_result.ethic <= 134 : ethic_percentage = 95
	if test_result.ethic <= 129 : ethic_percentage = 90
	if test_result.ethic <= 126 : ethic_percentage = 85
	if test_result.ethic <= 123 : ethic_percentage = 80
	if test_result.ethic <= 120 : ethic_percentage = 75
	if test_result.ethic <= 118 : ethic_percentage = 70
	if test_result.ethic <= 115 : ethic_percentage = 65
	if test_result.ethic <= 113 : ethic_percentage = 60
	if test_result.ethic <= 111 : ethic_percentage = 55
	if test_result.ethic <= 108 : ethic_percentage = 50
	if test_result.ethic <= 105 : ethic_percentage = 45
	if test_result.ethic <= 102 : ethic_percentage = 40
	if test_result.ethic <= 98 : ethic_percentage = 35
	if test_result.ethic <= 94 : ethic_percentage = 30
	if test_result.ethic <= 89 : ethic_percentage = 25
	if test_result.ethic <= 85 : ethic_percentage = 20
	if test_result.ethic <= 79 : ethic_percentage = 15
	if test_result.ethic <= 68 : ethic_percentage = 10
	if test_result.ethic <= 53 : ethic_percentage = 5
	if test_result.ethic <= 20 : ethic_percentage = 1

	if ethic_percentage >= 61:
		ethic_score = "Aprobado"
	elif ethic_percentage <= 50:
		ethic_score = "Reprobado"
	else:
		ethic_score = "Aprobado con Reservas"

	# Reliability percentage
	if test_result.reliability  > 41 : reliability_percentage = 99
	if test_result.reliability  <= 41 : reliability_percentage = 99
	if test_result.reliability  <= 40 : reliability_percentage = 95
	if test_result.reliability  <= 39 : reliability_percentage = 90
	if test_result.reliability  <= 37 : reliability_percentage = 85
	if test_result.reliability  <= 35 : reliability_percentage = 80
	if test_result.reliability  <= 34 : reliability_percentage = 75
	if test_result.reliability  <= 33 : reliability_percentage = 70
	if test_result.reliability  <= 32 : reliability_percentage = 65
	if test_result.reliability  <= 31 : reliability_percentage = 60
	if test_result.reliability  <= 29 : reliability_percentage = 55
	if test_result.reliability  <= 28 : reliability_percentage = 50
	if test_result.reliability  <= 26 : reliability_percentage = 45
	if test_result.reliability  <= 25 : reliability_percentage = 40
	if test_result.reliability  <= 23 : reliability_percentage = 35
	if test_result.reliability  <= 22 : reliability_percentage = 30
	if test_result.reliability  <= 21 : reliability_percentage = 25
	if test_result.reliability  <= 18 : reliability_percentage = 20
	if test_result.reliability  <= 15 : reliability_percentage = 15
	if test_result.reliability  <= 12 : reliability_percentage = 10
	if test_result.reliability  <= 9 : reliability_percentage = 5
	if test_result.reliability  <= 3 : reliability_percentage = 1

	if reliability_percentage >= 51:
		reliability_score = "Aprobado"
	elif reliability_percentage <= 30:
		reliability_score = "Reprobado"
	else:
		reliability_score = "Aprobado con Reservas"

	scores = {
		"addictions_score" :adictions_score,
		"judgement_score" :judgement_score,
		"discipline_score" :discipline_score,
		"veracity_score" :veracity_score,
		"loyalty_score" :loyalty_score,
		"intentionality_score" :intentionality_score,
		"ethic_score" :ethic_score,
		"reliability_score" :reliability_score,
	}

	percentages = {
		"addictions_percentage" :addiction_percentage,
		"judgement_percentage" :judgement_percentage,
		"discipline_percentage" :discipline_percentage,
		"veracity_percentage" :veracity_percentage,
		"loyalty_percentage" :loyalty_percentage,
		"intentionality_percentage" :intentionality_percentage,
		"ethic_percentage" :ethic_percentage,
		"reliability_percentage" :reliability_percentage,
	}

	integrity_export_data = {'scores':scores,'percentages':percentages}

	return integrity_export_data