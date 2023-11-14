#!/usr/bin/python3

"""Base Class in the '''base''' module"""


class Base():
    """Calss variable"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The class initializer

            Args:
                id (int): the id of the instances
            """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
