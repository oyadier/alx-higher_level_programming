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

    def area(self):
        '''The get method for the square
        '''
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''A setter method to set instance private size
            Args:
            value (int): a posive or zero value
        '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print()
