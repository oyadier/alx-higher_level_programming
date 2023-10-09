#!/usr/bin/python3
def max_integer(my_list=[]):
    """ max_integer - a function that finds
        the biggest integer of a list.

        @my_list: the list of integer elements

        Return: biggest number
    """
    if len(my_list) == 0:
        return None
    big = 0
    big = my_list[0]
    for i in range(1, len(my_list)):
        small = my_list[i]
        if big < small:
            big = small
    return big
