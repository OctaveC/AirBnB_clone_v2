#!/usr/bin/python3
""" Module Class tests """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Class review tests """

    def __init__(self, *args, **kwargs):
        """ Init Review tests"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ various tests """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ various tests """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ various tests """
        new = self.value()
        self.assertEqual(type(new.text), str)
