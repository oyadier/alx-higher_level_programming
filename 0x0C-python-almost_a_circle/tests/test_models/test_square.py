"""Test cases for `Square` module"""

import unittest

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """Defining all the possible cases"""

    def test_size(self):
        """Size is pass"""
        Base._Base__nb_objects = 0
        sq = Square(1)
        self.assertEqual(sq.size, 1)

    def test_diff_size(self):
        """Diff size values"""
        Base._Base__nb_objects = 0
        sq = Square(1, 2)
        self.assertEqual(sq.x, 2)

    def test_string(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq = Square("3")

    def test_type(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq = Square(2, "2")

    def test_y_string(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq = Square(3, 1, "3")
    
    def test_list(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq = Square([2, 4], 3)

    def test_turple(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq = Square(2, (4, 3))

    def test_all_int(self):
        Base._Base__nb_objects = 0
        sq = Square(3, 2, 4, 5)
        self.assertEqual(sq.size, 3)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 4)
        self.assertEqual(sq.id, 5)

    def test_size_typeError(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            sq = Square(-1)

    def test_x_tyepError(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            sq = Square(2, -3)

    def test_y_typeError(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            sq = Square(4, 5, -4)

    def test_size_typeError(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            sq = Square(0)

    """Testing for float"""
    def test_size_valueError(self):
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq = Square(1.2)

    def test__str__(self):
        Base._Base__nb_objects = 0
        sq = Square(3, 4, 5, 2)
        self.assertEqual(sq.__str__(), "[Square] (2) 4/5 - 3")

    def test_to_dictionary(self):
        Base._Base__nb_objects = 0
        sq = Square(3, 2, 4, 5)
        dic = sq.to_dictionary()
        self.assertDictEqual(dic, {'id':  5, 'size': 3, 'x': 2, 'y':4})
        self.assertEqual(type(dic), dict)

