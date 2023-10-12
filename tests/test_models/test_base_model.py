#!/usr/bin/python3
"""Testing for the Base model class
Importing modules
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Unittests for BaseModel Class

    Inherits from unittest.TestCase
    """

    def test_Instantatiaon(self):
        """testing for instantiation of the object"""
        my_obj = BaseModel()
        self.assertIsInstance(my_obj, BaseModel)
        self.assertTrue(hasattr(my_obj, "id"))

    def test_uniqu_id(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_date_time(self):
        obj1 = BaseModel()
        self.assertIsInstance(obj1.created_at, datetime)

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj.id, obj_dict["id"])

if __name__ == '__main__':
    unittest.main()

