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
        