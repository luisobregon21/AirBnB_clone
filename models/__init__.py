#!/usr/bin/python3
''' Module creates a unique FileStorage instance '''
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review

hbnb_classes = {'BaseModel': BaseModel, 'City': City,
                'User': User, 'Place': Place, 'State': State,
                'Amenity': Amenity, 'Review': Review
                }

storage = FileStorage()
storage.reload()
