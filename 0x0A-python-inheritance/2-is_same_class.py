#!/usr/bin/python3

"""Check two objects"""
def is_same_class(obj, a_class):
    """
    Check identical object
    Args:
        obj (object): first object
        a_class: the second object

    Return: True if same orderwise False
    """
    return isinstance(obj, a_class)
