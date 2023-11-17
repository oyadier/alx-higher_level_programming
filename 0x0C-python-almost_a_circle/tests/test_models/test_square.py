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

    def test_id(self):
        """Size is pass"""
        Base._Base__nb_objects = 0
        sq = Square(1)
        re = Rectangle(23, 3)
        sq.id += 2
        self.assertEqual(sq.id, 3)

    def test_diff_size(self):
        """Diff size values"""
        Base._Base__nb_objects = 0
        sq = Square(1, 2)
        self.assertEqual(sq.size, 1)
