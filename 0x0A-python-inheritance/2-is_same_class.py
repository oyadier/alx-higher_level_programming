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

    if isinstance(obj.__repr__(), a_class):
        return True
    else:
        return False
