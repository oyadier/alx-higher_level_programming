#!/usr/bin/python3
def no_c(my_string):
    """ no_c - a function that removes all
        characters c and C from a string.
        @my_string: the string parameter through which c will be removed
    """
    new_string = ""
    for i in my_string:
        if ord(i) == 67 or ord(i) == 99:
            new_string += ""
        else:
            new_string+= i
    return new_string
