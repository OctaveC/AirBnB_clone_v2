#!/usr/bin/python3
""" Module testing FileStorage """
import unittest
import models
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class for FileStorageTests """

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def setUp(self):
        """ Seting up """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def tearDown(self):
        """ Removing the garbage """
        try:
            os.remove('file.json')
        except Exception:
            pass

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        temp = ""
        obj = ""
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_all(self):
        """ Checking all """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_saving_instantiation(self):
        """ testing save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_empty(self):
        """ Testing with nothing """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)


    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_reload_from_nothing(self):
        """ testing relopading nothing """
        self.assertEqual(storage.reload(), None)

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_reload_empty(self):
        """ Reload empty """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_base_model_save(self):
        """ BaseModel save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_type_path(self):
        """ test path """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_type_objects(self):
        """ checking objects """
        self.assertEqual(type(storage.all()), dict)

    @unittest.skipIf(models.storage_type == 'db', "testing DB storage instead")
    def test_storage_var_created(self):
        """ FileStorage & storage """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
