#!/usr/bin/python3
'''Module contains FileStorage class'''
import json
from models.base_model import BaseModel

class FileStorage:
    '''
    Class contains methods that serialize instances to a JSON file
    and deserializes a JSON file to instances
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Method returns dict __objects'''
        return self.__objects
    
    def new(self, obj):
        '''Method sets in the obj with key'''
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        '''Method Serializes'''
        new_dic = {}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            for key, val in self.__objects.items():
                new_dic[key] = val.to_dict()
            json.dump(new_dic, f)

    def reload(self):
        ''' Method Deserializes '''
        temp_dic = {}
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                temp_dic = json.loads(f.read())
                for key, val in temp_dic.items():
                    self.__objects[key] = BaseModel(**val)
        except IOError:
            pass
