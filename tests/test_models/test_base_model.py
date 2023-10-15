#!/usr/bin/python3
"""Testing for the Base model class
Importing modules
"""
import unittest
from datetime import datetime
import models
import time
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

    def test_str(self):
        obj = BaseModel()
        obj_str = str(obj)
        self.assertIn(obj.__class__.__name__, obj_str)
        self.assertIn(obj.id, obj_str)

    def test_Instance_stored_in_objs(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_str(self):
        obj = BaseModel()
        self.assertEqual(type(obj.id), str)

    def test_documentation(self):
        """ testing for for documentation """
        self.assertTrue(len(BaseModel.__doc__) >= 20,
                        "Short or no documentation")
        self.assertTrue(len(BaseModel.save.__doc__) >= 20, "Short doc")
        self.assertTrue(len(BaseModel.to_dict.__doc__) >= 20, "Short doc")
        self.assertTrue(len(BaseModel.__str__.__doc__) >= 20, "Short doc")
        self.assertTrue(len(BaseModel.__init__.__doc__) >= 20, "Short doc")

    def test_updates_as(self):
        base4 = BaseModel()
        var1 = base4.updated_at
        time.sleep(1)
        base4.save()
        var2 = base4.updated_at
        self.assertNotEqual(var1, var2)


class TestBaseModel_save_method(unittest.TestCase):

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("objects_file.json", "r") as f:
            self.assertIn(bmid, f.read())


if __name__ == '__main__':
    unittest.main()
