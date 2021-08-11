#!/usr/bin/python3
""" Module Class tests """
import unittest
import inspect
import time
from datetime import datetime
from unittest import mock
import models
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
        """
        test place id
        """
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        if models.storage_type == "db":
            self.assertEqual(review.place_id, None)
        else:
            pass

    def test_user_id(self):
        """
        test user id
        """
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        if models.storage_type == "db":
            self.assertEqual(review.user_id, None)
        else:
            pass

    def test_text(self):
        """
        test class attr
        """
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        if models.storage_type == "db":
            self.assertEqual(review.text, None)
        else:
            pass
