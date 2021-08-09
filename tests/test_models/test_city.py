#!/usr/bin/python3
""" Modules for tests city """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Class for city tests """

    def __init__(self, *args, **kwargs):
        """ Init city tests"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ various tests """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ various tests """
        new = self.value()
        self.assertEqual(type(new.name), str)
