#!/usr/bin/python3
'''Module contains class Review'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''class inherits from BaseModel'''

    place_id = ""
    user_id = ""
    text = ""
