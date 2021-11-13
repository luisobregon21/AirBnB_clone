#!/usr/bin/python3
"""
Unittest module for BaseModel Class
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModelClass(unittest.TestCase):
    """Class test BaseModel class"""

    def setUp(self):
        ''' define instructions that will be executed
            before and after each test method '''
        self.L_base_model = BaseModel()
        self.J_base_model = BaseModel()

    def test_Init(self):
        ''' Checks if Init works.
        checks if Instance works '''
        self.assertIsInstance(self.L_base_model, BaseModel)
        self.assertIsInstance(self.J_base_model, BaseModel)

    def test_Id(self):
        ''' Test that 2 instances don't have the same ID '''
        self.assertNotEqual(self.L_base_model.id,
                            self.J_base_model.id)

if __name__ == "__main__":
    unittest.main()
