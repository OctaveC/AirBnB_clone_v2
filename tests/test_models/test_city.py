#!/usr/bin/python3
""" Modules for tests city """
from models.city import City
from models.base_model import BaseModel
import os
import unittest


class test_City(unittest.TestCase):
    """ Tests for city """

    @classmethod
    def setUpClass(cls):
        """ set up for test """
        cls.city = City()
        cls.city.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """ at the end of the test this will tear it down """
        del cls.city

    def test_checking_for_docstring_City(self):
        """ checking for docstrings """
        self.assertIsNot(City.__doc__, None)

    def test_is_subclass_City(self):
        """ test if City is subclass of Basemodel """
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """ test attribute type for City """
        self.assertEqual(type(self.city.name), str)

    def test_attributes_City(self):
        """ chekcing if City have attributes """
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        " This test only work in Filestorage ")
    def test_save_City(self):
        """ test if the save works """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """ test if dictionary works """
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
