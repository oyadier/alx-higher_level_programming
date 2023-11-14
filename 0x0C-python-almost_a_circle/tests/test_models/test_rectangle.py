"""Test cases for `rectangle` module""" 


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    """All available Test Case for each function"""

    def test_Id(self):
        """Increase the id with subclass"""
        ob = Base()
        re = Rectangle(2, 3)
        self.assertEqual(re.id, 2)

    def test_width_value(self):
        ob = Base()
        re = Rectangle(2, 3)
        self.assertEqual(re.width, re.id)

    def test_height_value(self):
        Base._Base__nb_objects = 0
        re = Rectangle(33, 9, 34)
        self.assertEqual(re.id, re.__width - re.__x)
