#!/usr/bin/python3
"""The Rectangel class"""
from .base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle constructor
            Args:
                width (int): the width of the rectangle
                height (int): the heigth of the rectangle
                x (int): x value
                y (int): y value
        """

        self.check_values(width=width, height=height, x=x, y=y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @staticmethod
    def check_values(**kwargs):
        """Exception raiser for

            Args:
            kwargs (double-value): Key value pair object
        """
        for name, value in kwargs.items():
            if name == "x" or name == "y":
                if type(value) != int:
                    raise TypeError("{} must be an integer".format(name))

                elif value < 0:
                    raise ValueError("{} must be >= 0".format(name))
            else:
                if type(value) != int:
                    raise TypeError("{} must be and integer".format(name))
                if value <= 0:
                    raise ValueError("{} must be >  0".format(name))

    @property
    def width(self):
        """Get the private width arribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """modifying the value of the width
            Args:
                value (int): the new width value
        """
        self.check_values(width=value)
        self.__width = value

    @property
    def height(self):
        """Get the private height arribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Modifying the value of the height
            Args:
                value (int): the new height value
        """
        self.check_values(height=value)
        self.__height = value

    @property
    def x(self):
        """Get the value of x
            Return:
                x (int): x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Modify the value of x"""
        self.check_values(x=value)
        self.__x = value

    @property
    def y(self):
        """Get the value of y
             Return:
                int: y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Modify the value of y
            Args:
                value (int): the new integer value
        """
        self.check_values(y=value)
        self.__y = value

    def area(self):
        """Compute the area of rectangle
            Return:
                int: area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Display number of width and height"""
        [print() for i in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for i in range(self.__x)]
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """String Rep of Rectangle object"""

        return f"[{self.__class__.__name__}] \
 ({self.id}) {self.__x}/{self.__y} \
 - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):

        """No keyword argument
            Args:
                *args: pointer to an object
                **kwargs: a pointer to objects
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) > 0:
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Create dic of rectangle obj"""

        dictionary = {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }

        return dictionary
