#!/usr/bin/python3
"""A rectangle module"""


class Rectangle:
    """An Rectangle with Width and height"""
    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returning the biggest area of a rectangle instance"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        re_1 = rect_1.area()
        re_2 = rect_2.area()

        if re_2 > re_1:
            return re_2
        return re_1

    def __init__(self, width=0, height=0):
        """Initialized Rectangle

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returning the biggest area of a rectangle instance"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        re_1 = rect_1.area()
        re_2 = rect_2.area()

        if re_2 > re_1:
            return re_2
        return re_1

    @classmethod
    def square(cls, size=0):
        """Rectangle instance computing square"""
        return cls(size, size)

    @property
    def width(self):
        """Gets the size of width of the retangle

        Returns:
            width (int)
        """

        return self.__width

    @width.setter
    def width(self, width):
        """Changes the width of the rectangle

        Args:
            width (int): New width
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Gets the size of height of the retangle

        Returns:
            height (int)
        """

        return self.__height

    @height.setter
    def height(self, height):
        """Changes the height of the rectangle
        Args:
            height (int): New height
        """

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle

        Returns:
            area (int)
        """

        return self.__width * self.__height

    def perimeter(self):
        """ Calculate the perimeter of the rectangle

        Returns:
            perimeter (int)
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print rectangle using 'print_symbol'

        Returns:
            rectangle(string)
        """

        str_symbol = ""

        if self.__width == 0 or self.__height == 0:
            return ""
        if not isinstance(self.print_symbol, str):
            self.print_symbol = str(self.print_symbol)

        for i in range(self.__height):
            str_symbol += self.print_symbol * self.__width
            if i < self.height - 1:
                str_symbol += "\n"

        return str_symbol

    def __repr__(self):
        """return rectangle in a string format

        Returns:
            rectangle (string)
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Detecs recatangle deletion"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
