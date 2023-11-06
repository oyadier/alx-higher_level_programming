#!/usr/bin/python3
"""This function Compares objects whether they are the same."""


def is_kind_of_class(obj, a_class):
    """Checks identical object.

        Args:
            obj (object): first object.
            a_class (object): the second object.

        Return:
            True: if same
            False: if not
    """
    return isinstance(obj, a_class)
