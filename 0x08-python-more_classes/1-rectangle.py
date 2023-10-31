#!/usr/bin/python3

"""
This is a Rectangle Class module
It purpose is to compute the area of a rectangle
"""


class Rectangle():

    def __init__(self, width=0, height=0):
        """
        Magic instantiating method of an object

        Args:
            width (int): the width of a rectangle
            height (int): the height of a ractangle

        Return:
            (int): the size area of rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

        # Getters and setters of the rectangle object

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
