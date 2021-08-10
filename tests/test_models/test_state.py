#!/usr/bin/python3
""" Modules for tests state """
from models.state import State
from models.base_model import BaseModel
import os
import unittest


class test_State(unittest.TestCase):
    """ Tests for state """

    @classmethod
    def setUpClass(cls):
        """ set up for test """
        cls.state = State()
        cls.state.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """ at the end of the test this will tear it down """
        del cls.state

    def test_checking_for_docstring_State(self):
        """ checking for docstrings """
        self.assertIsNot(State.__doc__, None)

    def test_is_subclass_State(self):
        """ test if State is subclass of Basemodel """
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_State(self):
        """ test attribute type for State """
        self.assertEqual(type(self.state.name), str)

    def test_attributes_State(self):
        """ chekcing if State have attributes """
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        " This test only work in Filestorage ")
    def test_save_State(self):
        """ test if the save works """
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """ test if dictionary works """
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()