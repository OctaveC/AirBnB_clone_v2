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


    def test_all(self):
        """ test for all """
        obj = storage.all()
        self.assertEqual(type(obj), dict)

    def testState(self):
        """ testing various objects """
        state = State(name="machin")
        if state.id in storage.all():
            self.assertTrue(state.name, "machin")

    def testCity(self):
        """ testing various objects """
        city = City(name="biduche")
        if city.id in storage.all():
            self.assertTrue(city.name, "biduche")

    def testPlace(self):
        """ testing various objects """
        place = Place(name="truc", number_rooms=5)
        if place.id in storage.all():
            self.assertTrue(place.number_rooms, 5)
            self.assertTrue(place.name, "truc")

    def testUser(self):
        """ testing various objects """
        user = User(name="thing")
        if user.id in storage.all():
            self.assertTrue(user.name, "thing")

    def testAmenity(self):
        """ testing various objects """
        amenity = Amenity(name="Toilet")
        if amenity.id in storage.all():
            self.assertTrue(amenity.name, "Toilet")

    def testReview(self):
        """ testing various objects """
        review = Review(text="rreview")
        if review.id in storage.all():
            self.assertTrue(review.text, "rreview")
