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

if __name__ == '__main__':
    unittest.main()

