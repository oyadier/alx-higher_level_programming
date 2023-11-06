#!/usr/bin/python3
"""Checks for inheritance."""


def inherits_from(obj, a_class):
    """Function that checks for inheritance.

        Args:
            obj (Objects): first object.
            a_class(object): seconde object.

        Return:
            True: if it inherited
            False: if not
    """
    return ((issubclass(type(obj), a_class)) and type(obj) != a_class)
