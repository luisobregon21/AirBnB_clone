#!/usr/bin/python3
'''Module contains BaseModel class'''


#import json
import uuid
from datetime import datetime

class BaseModel:
    '''
    Class contains common methods/attributes for other classes
    '''

    def __init__(self, *args, **kwargs):
        '''Class instantiator'''
        if kwargs is not None:
            if 'name' in kwargs:
                self.name = kwargs['name']
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'my_number' in kwargs:
                self.my_number = kwargs['my_number']
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if 'update_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    '''Magic Methods'''

    def __str__(self):
        '''Class string representation'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    '''Public instance methods'''

    def save(self):
        '''Method updates instance attribute updated_at'''
        self.update_at = datetime.now()

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
