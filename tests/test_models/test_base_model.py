#!/usr/bin/python3
""" Tests for Base Model """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ Class tests for Base Model """

    def __init__(self, *args, **kwargs):
        """ Init Base models """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ Setup. """
        pass

    def test_default(self):
        """ Default tests """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Various tests """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ Various tests """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_str(self):
        """ Various tests """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ Various tests """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ Various tests """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ Various tests """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ Various tests """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)
