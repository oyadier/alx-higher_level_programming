"""Test cases for `rectangle` module""" 


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    """All available Test Case for each function"""

    def test_Id(self):
        ob = Base()
        re = Rectangle(2, 3)
        self.assertEqual(re.id, 2)

