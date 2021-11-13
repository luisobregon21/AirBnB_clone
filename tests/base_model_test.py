#!/usr/bin/python3
"""
Unittest module for BaseModel Class
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Class test BaseModel class"""

    def setUp(self):
        ''' define instructions that will be executed
            before and after each test method '''
        self.L_base_model = BaseModel()

    def test_Init(self):
        ''' Checks if Init works.
        checks if Instance works '''
        self.assertIsInstance(self.L_base_model, BaseModel)


if __name__ == "__main__":
    unittest.main()
