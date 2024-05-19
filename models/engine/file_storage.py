#!/usr/bin/python3
"""FileStorage"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
}


class FileStorage:
    """serializes JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns"""
        if cls is not None:
            ndic = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    ndic[key] = value
            return ndic
        return self.__objects

    def new(self, obj):
        """set objects"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(json_obj, f)

    def reload(self):
        """deserialize"""
        try:
            with open(self.__file_path, "r") as f:
                x = json.load(f)
            for key in x:
                self.__objects[key] = classes[x[key]["__class__"]](**x[key])
        except:
            pass

    def delete(self, obj=None):
        """delete"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """reload"""
        self.reload()
