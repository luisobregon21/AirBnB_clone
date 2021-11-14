#!/usr/bin/python3
"""
Unittest module for BaseModel Class
"""
from datetime import datetime
import unittest
from unittest.case import _AssertRaisesContext
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from test_base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    """Class test BaseModel class"""

    def setUp(self):
        ''' create two base models'''
        self.A_base_model = BaseModel()
        self.B_base_model = BaseModel()

    def test_str_is_str(self):
        ''' Test __str__ method '''
        self.assertIsInstance(self.A_base_model.__str__(), str)

    def test_str_content(self):
        """checks content of __str__"""
        self.assertIn("[BaseModel]", self.B_base_model.__str__())

    def test_Init(self):
        ''' Checks if Init works'''
        self.assertIsInstance(self.A_base_model, BaseModel)
        self.assertIsInstance(self.B_base_model, BaseModel)

    def test_Id(self):
        ''' Test if each instance have an unique id '''
        self.assertNotEqual(self.A_base_model.id,
                            self.B_base_model.id)

    def test_id_str(self):
        '''test if id is str'''
        self.assertIsInstance(self.A_base_model.id, str)

    def test_date_is_date(self):
        '''test if dates are datetime type'''
        self.assertIsInstance(self.A_base_model.created_at, datetime)
        self.assertIsInstance(self.A_base_model.updated_at, datetime)

    def test_date_update(self):
        '''test if datetimes updates correctly'''
        self.A_base_model.save()
        self.assertNotEqual(self.A_base_model.created_at,
                            self.A_base_model.updated_at)

    def test_to_dict(self):
        """test if to_dict returns a dictionary"""
        self.assertIsInstance(self.A_base_model.to_dict(), dict)

    def test_to_dict_has_key(self):
        """test if to_dict works"""
        self.assertIn("created_at", self.A_base_model.to_dict())

    def test_add_attribute(self):
        """test adding attribute"""
        self.A_base_model.name = "pepe"
        self.assertEqual(self.A_base_model.name, "pepe")

    def test_kwarg(self):
        objdict = self.A_base_model.to_dict()
        self.kwarginstance = BaseModel(**objdict)
        self.assertIsInstance(self.kwarginstance, BaseModel)


if __name__ == "__main__":
    unittest.main()
