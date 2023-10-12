#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
        Using dictionary comprehesion to create dictionary
    """
    double_dic = {c: x * 2 for c, x in a_dictionary.items()}
    return double_dic
