#!/usr/bin/python3
'''Module contains User class that inherits from BaseModel'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Child class User of BaseModel'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
