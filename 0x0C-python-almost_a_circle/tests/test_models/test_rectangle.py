"""Rectangle Test Module"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    """Defining all the possible `test cases` """

    def test_increase_id(self):
        ob = Base()
        re = Rectangle(3, 4)
        self.assertEqual(re.id, 3)

