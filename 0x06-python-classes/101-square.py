#!/usr/bin/python3

"""Define a new Square class"""


class Square:

    """Placing methods here"""
    def __init__(self, size=0, position=(0, 0)):
        '''Creating an object
            Args:
            size (int): A positive or 0
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value"""
        if isinstance(value, tuple) and len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        self.__position = value
                        return
        raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        '''prints in stdout the square with the character # or a new line
            is size is zero.
        '''
        if self.__size == 0:
            print()
            return

        for line in range(self.__position[1]):
            print()
        for col in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
        return "{}{}".format(" " * self.__position[0], "#" * self.__size)

    def __str__(self):
        return self.my_print()
