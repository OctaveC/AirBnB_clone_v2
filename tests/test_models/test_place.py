#!/usr/bin/python3
""" Mopdule for Place tests """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import unittest
import inspect
import time
from datetime import datetime
from unittest import mock
import models

class test_Place(test_basemodel):
    """ Class for tests Place """

    def __init__(self, *args, **kwargs):
        """ Init Place tests """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ various tests """
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        if models.storage_type == "db":
            self.assertEqual(place.city_id, None)

    def test_user_id(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        if models.storage_type == "db":
            self.assertEqual(place.user_id, None)
        else:
            pass

    def test_name(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        if models.storage_type == "db":
            self.assertEqual(place.name, None)
        else:
            pass

    def test_description(self):
        """ various tests """
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        if models.storage_type == "db":
            self.assertEqual(place.description, None)
        else:
            pass


    def test_number_bathrooms(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        if models.storage_type == "db":
            self.assertEqual(place.number_bathrooms, None)
        else:
            pass
    def test_number_rooms(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        if models.storage_type == "db":
            self.assertEqual(place.number_rooms, None)
    def test_max_guest(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        if models.storage_type == "db":
            self.assertEqual(place.max_guest, None)
        else:
            pass

    def test_price_by_night(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        if models.storage_type == "db":
            self.assertEqual(place.price_by_night, None)
        else:
            pass

    def test_latitude(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        if models.storage_type == "db":
            self.assertEqual(place.latitude, None)
        else:
            pass

    def test_longitude(self):
        """
            Test Class attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        if models.storage_type == "db":
            self.assertEqual(place.longitude, None)
        else:
            pass
    def test_amenity_ids(self):
        """ various tests """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
