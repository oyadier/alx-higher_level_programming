#!/usr/bin/python3

"""Define a new Square class"""


class Square:

    """Placing methods here"""
    def __init__(self, size=0):
        '''Creating an object
            Args:
            size (int): A positive or 0
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
