#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ new_in_list - unction that replaces an element in \n a list at a specific position without modifying the original list.
    @idx: the index of the element to be replaced
    @element: the element to replace with
    Return: new list
    """
    new = my_list[:]
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return new
    new[idx] = element
    return new
