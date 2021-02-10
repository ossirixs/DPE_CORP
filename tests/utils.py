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
