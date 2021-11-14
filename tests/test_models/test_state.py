#!/usr/bin/python3
"""
Unittest module for User Class
"""
from datetime import datetime
import unittest
from unittest.case import _AssertRaisesContext
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from test_base_model import BaseModel
from models.base_model import State


class TestBaseModel(unittest.TestCase):
    """Class test BaseModel class"""

    def setUp(self):
        ''' create two base models'''
        self.A_user = State()
        self.B_user = State()

    def test_str_is_str(self):
        ''' Test __str__ method '''
        self.assertIsInstance(self.A_user.__str__(), str)

    def test_str_content(self):
        """checks content of __str__"""
        self.assertIn("[State]", self.A_user.__str__())

    def test_Init(self):
        ''' Checks if Init works'''
        self.assertIsInstance(self.A_user, State)
        self.assertIsInstance(self.B_user, State)

    def test_Id(self):
        ''' Test if each instance have an unique id '''
        self.assertNotEqual(self.A_user.id,
                            self.B_user.id)

    def test_id_str(self):
        '''test if id is str'''
        self.assertIsInstance(self.A_user.id, str)

    def test_date_is_date(self):
        '''test if dates are datetime type'''
        self.assertIsInstance(self.A_user.created_at, datetime)
        self.assertIsInstance(self.B_user.updated_at, datetime)

    def test_date_update(self):
        '''test if datetimes updates correctly'''
        self.A_base_model.save()
        self.assertNotEqual(self.A_user.created_at,
                            self.A_user.updated_at)

    def test_to_dict(self):
        """test if to_dict returns a dictionary"""
        self.assertIsInstance(self.A_user.to_dict(), dict)

    def test_to_dict_has_key(self):
        """test if to_dict works"""
        self.assertIn("created_at", self.A_user.to_dict())


if __name__ == "__main__":
    unittest.main()
