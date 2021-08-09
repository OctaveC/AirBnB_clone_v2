#!/usr/bin/python3
""" Module state tests """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Class state tests """

    def __init__(self, *args, **kwargs):
        """ Init state tests """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ various tests """
        new = self.value()
        self.assertEqual(type(new.name), str)
