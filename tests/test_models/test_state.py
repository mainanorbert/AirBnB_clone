import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    def test_state_instance(self):
        state = State()
        self.assertIsInstance(state, State)

    def test_state_inherits_base_model(self):
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_state_name(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_state_to_dict(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        # self.assertIn('name', state_dict)

    def test_state_str_representation(self):
        state = State()
        state.name = "New York"
        string_representation = str(state)
        self.assertIn("[State]", string_representation)
        self.assertIn("New York", string_representation)

    def test_dict_output(self):
        d = datetime.today()
        s = State()
        s.id = "123456"
        s.created_at = s.updated_at = d
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': d.isoformat(),
            'updated_at': d.isoformat(),
        }
        self.assertDictEqual(s.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        st = State()
        self.assertNotEqual(st.to_dict(), st.__dict__)

    def test_new_instance_stored_in_objects(self):
        from models import storage
        self.assertIn(State(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

if __name__ == "__main__":
    unittest.main()
