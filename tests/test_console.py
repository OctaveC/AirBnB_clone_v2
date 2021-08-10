#!/usr/bin/python3
""" tests for the console"""
import os
import sys
import models
import unittest
from io import StringIO
from unittest.mock import create_autospec
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import console

HBNBCommand = console.HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """ Testing the HBNB CLI """

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

class test_console(unittest.TestCase):
    """ Module for tests console"""
    def setUp(self):
        """Seting up"""
        self.backup = sys.stdout
        self.outie = StringIO()
        sys.stdout = self.outie

    def tearDown(self):
        """"""
        sys.stdout = self.backup

    def create(self):
        """ creates an instance of a class"""
        return HBNBCommand()

    def test_EOF(self):
        """ Test EOF exists"""
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_quit(self):
        """ Test quit exists"""
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_all(self):
        """ Test all exists"""
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.outie.getvalue(), str))

    def test_show(self):
        """
        Testing that show exists
        """
        console = self.create()
        console.onecmd("create User")
        user_id = self.outie.getvalue()
        sys.stdout = self.backup
        self.outie.close()
        self.outie = StringIO()
        sys.stdout = self.outie
        console.onecmd("show User " + user_id)
        x = (self.outie.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(x))

    def test_show_2(self):
        """
        Testing error messages
        """
        console = self.create()
        console.onecmd("create User")
        user_id = self.outie.getvalue()
        sys.stdout = self.backup
        self.outie.close()
        self.outie = StringIO()
        sys.stdout = self.outie
        console.onecmd("show")
        x = (self.outie.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", x)

    def test_show_2(self):
        """
        Testing error messages
        """
        console = self.create()
        console.onecmd("create User")
        user_id = self.outie.getvalue()
        sys.stdout = self.backup
        self.outie.close()
        self.outie = StringIO()
        sys.stdout = self.outie
        console.onecmd("show User")
        x = (self.outie.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", x)

    def test_show_3(self):
        """
        Testing error messages
        """
        console = self.create()
        console.onecmd("create User")
        user_id = self.outie.getvalue()
        sys.stdout = self.backup
        self.outie.close()
        self.outie = StringIO()
        sys.stdout = self.outie
        console.onecmd("show User " + "124356876")
        x = (self.outie.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", x)

    def test_create(self):
        """
        Test create
        """
        console = self.create()
        console.onecmd("create User")
        self.assertTrue(isinstance(self.outie.getvalue(), str))

    def test_class_name(self):
        """
        Testing the error messages for class name missing.
        """
        console = self.create()
        console.onecmd("create")
        x = (self.outie.getvalue())
        self.assertEqual("** class name missing **\n", x)

    def test_class_name_doest_exist(self):
        """
        Testing error messages missing class name.
        """
        console = self.create()
        console.onecmd("create Binita")
        x = (self.outie.getvalue())
        self.assertEqual("** class doesn't exist **\n", x)
