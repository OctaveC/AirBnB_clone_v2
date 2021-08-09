#!/usr/bin/python3
""" Tests for amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Tests for amenity """

    def __init__(self, *args, **kwargs):
        """ Init for amneity """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ test name2 """
        new = self.value()
        self.assertEqual(type(new.name), str)
