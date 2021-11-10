#!/usr/bin/python3
'''Module contains FileStorage class'''
import json
import uuid
from datetime import datetime


class FileStorage:
    '''
    Class contains methods that serialize instances to a JSON file
    and deserializes a JSON file to instances
    '''

    __file__path = "file.json"
    __objects = {}

    def all(self):
        '''Method returns dict __objects'''
        return self.__objects
    
    def new(self, obj):
        '''Method sets in the obj with key'''
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        '''Method'''
        new_dict = {}
        with open (self.__file__path , "w") as f:
            for k, v in self.__objects.items():
                new_dict[k] = v.to_dict()
            json.dump(new_dict, f)
        
    def reload(self):
        
