"""Testing a function"""
#to make middle names optional
def get_formatted_name(first, last, middle=''):
    """Get neatly formated full name"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

    