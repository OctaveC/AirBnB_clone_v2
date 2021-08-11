#!/usr/bin/python3
""" Module for User tests """
import unittest
import inspect
import time
from datetime import datetime
from unittest import mock
import models
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.base_model import BaseModel

class test_User(test_basemodel):
    """ Class for User tests """

    def __init__(self, *args, **kwargs):
        """ Init tests User """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ various tests """
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        if models.storage_type == "db":
            self.assertEqual(user.first_name, None)
        else:
            pass

    def test_last_name(self):
        """ various tests """
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        if models.storage_type == "db":
            self.assertEqual(user.last_name, None)
        else:
            pass

    def test_email(self):
        """
        test class attribute email
        """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        if models.storage_type == "db":
            self.assertEqual(user.email, None)
        else:
            pass


    def test_password(self):
        """ various tests """
        new = self.value()
        self.assertTrue(hasattr(new, "password"))
        if models.storage_type == "db":
            self.assertEqual(new.password, None)
        else:
            pass
