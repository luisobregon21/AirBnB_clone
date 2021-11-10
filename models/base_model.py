#!/usr/bin/python3
'''Module contains BaseModel class'''
import json
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    '''
    Class contains common methods/attributes for other classes
    '''

    def __init__(self, *args, **kwargs):
        '''Class instantiator'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if 'my_number' in kwargs:
                self.my_number = kwargs['my_number']
            if 'update_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if 'name' in kwargs:
                self.name = kwargs['name']
     
    '''Magic Methods'''

    def __str__(self):
        '''Class string representation'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    '''Public instance methods'''

    def save(self):
        '''Method updates instance attribute updated_at'''
        self.update_at = datetime.now()
        storage.save()

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
