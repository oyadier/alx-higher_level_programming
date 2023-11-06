#!/usr/bin/python3
"""Compare objects."""


def is_king_of_class(obj, a_class):
    """
    Check identical object.
    obj (object): first object.
    a_class: the second object.

    Return: True if same orderwise False.
    """
    return isinstance(obj, a_class)
