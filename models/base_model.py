#!/usr/bin/python3
'''Module contains BaseModel class'''
import json
import uuid
import datetime


class BaseModel:
    '''
    Class contains common methods/attributes for other classes
    '''

    def __init__(self, id=None, name=None, my_number=None):
        '''Class instantiator'''
        self.id = str(uuid.uuid4())
        self.name = name
        self.my_number = my_number
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    '''Magic Methods'''

    def __str__(self):
        '''Class string representation'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    '''Public instance methods'''

    def save(self):
        '''Method updates instance attribute updated_at'''
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        '''Method returns a dict containing all k's/v's of __dict__'''
        return {
            'my_number': self.my_number,
            'name': self.name,
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.isoformat(),
            'id': self.id,
            'created_at': self.created_at.isoformat()
        }
