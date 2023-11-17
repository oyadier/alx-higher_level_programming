"""Test cases for `Square` module"""

import unittest

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """Defining all the possible cases"""

    def test_size(self):
        """Size is pass"""
        sq = Square(1)
        self.assertEqual(sq.size, 1)

    def test_id(self):
        """Size is pass"""
        sq = Square(1)
        self.assertEqual(sq.id, 1)
