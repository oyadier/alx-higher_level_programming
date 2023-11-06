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
    return isinstance(obj, a_class)
