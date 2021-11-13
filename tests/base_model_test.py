#!/usr/bin/python3
"""
Unittest for BaseModel Class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    ''' Class tests BaseModel class '''

    def test_init(self):
        ''' Method tests the init method of base_model '''
        self.test_model = BaseModel()
