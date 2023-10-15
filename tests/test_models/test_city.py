import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime

class TestCity(unittest.TestCase):

   
    def test_city_instance(self):
        city = City()
        self.assertIsInstance(city, City)

    def test_city_inherits_base_model(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_state_id(self):
        city = City()
        city.state_id = "CA"
        self.assertEqual(city.state_id, "CA")

    def test_city_name(self):
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")

    def test_city_to_dict(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        # self.assertIn('City', city_dict)
        # self.assertIn('name', city_dict)

    def test_city_str_representation(self):
        city = City()
        city.state_id = "CA"
        city.name = "Los Angeles"
        string_representation = str(city)
        self.assertIn("[City]", string_representation)
        self.assertIn("CA", string_representation)
        self.assertIn("Los Angeles", string_representation)

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        cy = City()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())

    def test_to_dict_contains_added_attributes(self):
        cy = City()
        cy.middle_name = "Holberton"
        cy.my_number = 98
        self.assertEqual("Holberton", cy.middle_name)
        self.assertIn("my_number", cy.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        cy = City()
        cy_dict = cy.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cy.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        cy = City()
        self.assertNotEqual(cy.to_dict(), cy.__dict__)


if __name__ == "__main__":
    unittest.main()
