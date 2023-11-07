#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Class attributes Here"""

    def area(self):
        """Raising implemention exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value

            Args:
            name (str): user name.
            value (int): integer value

            Return:
            Nothing.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
