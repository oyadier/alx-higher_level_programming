"""Test moddule for `base` module"""
from models.base import Base
from models.rectangle import Rectangle
import unittest
import json

class TestBase(unittest.TestCase):
    """Test if id is None"""
    def test_id_none(self):
        """Increate id value if id is None"""
        Base._Base__nb__objects = 0
        bas = Base()
        self.assertEqual(bas.id, 2)

    def test_id_value(self):
        """Assert equal the value of id"""
        obj = Base(23)
        self.assertEqual(obj.id, 23)

    def test_nb_obj_value(self):
        """Check if id value not equal"""
        obj1 = Base(24)
        self.assertNotEqual(obj1.id, 58)

    def test_isinstance(self):
        """Test for it instance"""
        base_obj = Base()
        self.assertIsInstance(base_obj, Base)

    def test_typeError(self):
        """Test with String"""
        obj = Base("typeError")
        self.assertRaises(TypeError, "Not valid value")

    def test_list_typeError(self):
        """Passing List"""
        Base._Base__nb__objects = 0
        _list = [1 ,3, 8]
        obj = Base(_list)
        self.assertRaises(TypeError, "Not valid value")

    def test_same_obj(self):
        obj = Base()
        obj1 = Base(34)
        rec = Rectangle(2, 5)
        self.assertEqual(rec.id, 4)

    def test_id_float(self):
        """Test floating number"""
        obj = Base(2.3)
        self.assertEqual(obj.id, 2.3)

    def test_id_list(self):
        """Testing with a list elements"""
        ids = [2, 34, 4, 55]
        for i in range(len(ids)):
            ele = ids[i]
            bas = Base(ele)
            self.assertEqual(bas.id, ele)

    def test_with_nb(self):
        """Init __nb__obj"""
        Base._Base__nb_objects = 0
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_multiple_obj(self):
        """Test with multi obj"""
        Base._Base__nb_objects = 0
        ob = Base()
        ob1 = Base()
        ob2 = Base(45)
        self.assertEqual(ob1.id, 2)

    def test_multiple1_obj(self):
        """Test with multiple object"""
        Base._Base__nb_objects = 0
        ob = Base()
        ob1 = Base()
        ob2 = Base(45)
        self.assertNotEqual(ob2.id, 2)

    def test_multiple2_obj(self):
        """Create more than 3 objects"""
        Base._Base__nb_objects = 0
        ob = Base()
        ob1 = Base()
        ob2 = Base(45)
        ob3 = Base()
        self.assertEqual(ob3.id, 3)

    def test_id_by_rectangle(self):
        """Use Rectangle to set id"""
        ob = Base()
        rec = Rectangle(2, 4, 0, 2, 290)
        self.assertEqual(rec.id, 290)

    def test_increase_id(self):
        ob = Base()
        ob.id = 90
        self.assertEqual(ob.id, 90)

    """Json Test"""
    def test_none_dic(self):
        ob = Base(1)
        self.assertEqual(ob.to_json_string(None), "[]")

    def test_with_list(self):
        ob = Base()
        _lis = {'name': "Oyadier", 'age': 13}
        json_ob =  ob.to_json_string(_lis)
        self.assertEqual(json_ob, '{"name": "Oyadier", "age": 13}')

    def test_with_list(self):
        ob = Base()
        _lis = {'name': "Oyadier", 'age': 13}
        json_ob =  ob.to_json_string(_lis)
        self.assertEqual(json.loads(json_ob)['name'], "Oyadier")
