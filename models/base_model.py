#!/usr/bin/python3
'''Module contains BaseModel class'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''
    Class contains common methods/attributes for other classes
    '''

    def __init__(self, *args, **kwargs):
        '''Class instantiator'''
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            dt = "%Y-%m-%dT%H:%M:%S.%f"
            del kwargs['__class__']
            kwargs['created_at'] = datetime.strptime(kwargs["created_at"], dt)
            kwargs['updated_at'] = datetime.strptime(kwargs["updated_at"], dt)
            for key, value in kwargs.items():
                setattr(self, key, value)

    '''Magic Methods'''

    def __str__(self):
        '''Class string representation'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    '''Public instance methods'''

    def save(self):
        '''Method updates instance attribute updated_at'''
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Method returns a dict containing all k's/v's of __dict__'''
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
