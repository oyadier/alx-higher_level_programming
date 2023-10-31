#!/usr/bin/python3

"""This is a Rectangle Class module"""



class Rectangle():

    """A rectangle that with width and heig"""

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

    @property
    def height(self):
        """
        Get the value of height

        Returns:
            (int): the height
        """
        return self.__height

    @property
    def width(self):
        """
        Get the value of width

        Returns:
            (int): the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Args:
            value (int): the new width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the new height

        Args:
            value (int): the new height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computing the area of a rectangle

        Returns:
            (int): area of a rectangle
        """
        return self.__width * self.__height
    def perimeter(self):
        """
        Computing the parameter of a rectangle

        Returns:
            (int): the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
