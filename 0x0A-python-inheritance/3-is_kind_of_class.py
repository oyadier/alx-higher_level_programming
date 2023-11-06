#!/usr/bin/python3
"""This function Compares objects whether they are the same."""


def is_king_of_class(obj, a_class):
    """
    Checks identical object.

    Args:
        obj (object): first object.
        a_class: the second object.

    Return:
        bool: if same orderwise False.
    """
    return isinstance(obj, a_class)
