#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """ replace_in_lis - search and replace an element at posi
        @idx: the index of the element
        @element: the element to replace with
        Return: list of objects
    """
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
