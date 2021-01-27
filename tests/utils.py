""" Tools for processing data and prevent errors """


def clean_data(data, invert):
    """
    Function that clean data from None values, return casted data in number
    will invert the output if invert is set True, returns 0 for None values
    """
    # Clean the data for None values
    print("data and invert", data, invert)
    if data is not None:
        data = int(data)
        # Invert the cleaned data if needed
        if invert:
            data = not data
    else:
        data = 0
    print(data)
    return data
