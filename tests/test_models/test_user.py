#!/usr/bin/python3
""" Module for User tests """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Class for User tests """

    def __init__(self, *args, **kwargs):
        """ Init tests User """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ various tests """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ various tests """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ various tests """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ various tests """
        new = self.value()
        self.assertEqual(type(new.password), str)
