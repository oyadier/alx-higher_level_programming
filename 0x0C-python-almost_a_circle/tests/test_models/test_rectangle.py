"""Rectangle Test Module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class RectangleTestCase(unittest.TestCase):
    """Defining all the possible `test cases` """

    def test_increase_id(self):
        Base._Base__nb_objects = 0
        re = Rectangle(3, 4)
        self.assertEqual(re.id, 1)

    def test_change_id(self):
        Base._Base__nb_objects = 0
        re = Rectangle(3, 4)
        re.id = 2
        self.assertEqual(re.id, 2)

    def test_id_value(self):
        Base._Base__nb_objects = 0
        re = Rectangle(3, 56, 0, 0, 19)
        self.assertEqual(re.id, 19)



