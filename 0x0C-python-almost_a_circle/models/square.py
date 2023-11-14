#!/usr/bin/python3
"""A Subclass of Rectangle module"""
from .rectangle import Rectangle


class Square(Rectangle):
    """This class inherit from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Create instance of the 'Rectangle' class

            Args:
                size (int): width value
                size (int): height value
                x (int): x axis value
                y (int): y axis value
                id (int): the instance id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the value of `size`
        Returns:
            value of size
        """
        return super().width()

    @size.setter
    def size(self, value):
        """sets the dimensions of `Square`"""
        super().width(value)
        super().height(value)

    def update(self, *args, **kwargs):
        """Updates the values of the class"""
        if args and len(args) > 0:
            keys = ["id", "size", "x", "y"]
            for i, v in enumerate(args):
                setattr(self, keys[i], v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Retrieves all the attributes of class to dictionary
        Returns:
            dictionary containing it's attributes
        """
        dictionary = {
                "id": self.id,
                "size": super().width,
                "x": super.x(),
                "y": super.y()
        }
        return dictionary

    """def __str__(self):
        string = "[{}] ({}) {}/{} - {}"
        return string.format(self.__class__.__name__,
      self.id, self.x, self.y, self.size(), self.size())
      """
