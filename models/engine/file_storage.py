#!/usr/bin/python3
'''Module contains FileStorage class'''

class FileStorage:
    '''
    Class contains methods that serialize instances to a JSON file
    and deserializes a JSON file to instances
    '''

    def all(self):
        '''Method returns dict __objects'''
        return self.__objects
    
    def new(self, obj):
        '''Method sets in the obj with key'''
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        '''Method Serealizes'''
        
'''def reload(self):
        Method Deserializes
                '''
