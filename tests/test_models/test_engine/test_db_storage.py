#!/usr/bin/python
""" Module test """
import os
import unittest
from models.engine.db_storage import DBStorage
from models import storage
from unittest.case import skipIf
from models.engine.file_storage import FileStorage
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City

@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db',
    "skip if not database"
)
class test_dbstorage(unittest.TestCase):
    """ class for dbstorage stets """

    def setUp(cls):
        """ Seting up """
        cls.user = User()
        cls.user.last_name = "Last"
        cls.user.first_name = "First"
        cls.user.email = "important@mail.com"
        cls.user.password = "pwd"

        cls.storage = FileStorage()

    def tearDown(self):
        """ cleaning up """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_new_db(self):
        """ testing new """
        for obj in storage.all(User).values():
            temp = obj
            self.assertTrue(temp is obj)

    def test_all_db(self):
        """ testing all """
        obj = storage.all()
        self.assertEqual(type(obj), dict)
