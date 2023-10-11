#!/usr/bin/python3
import json
import os

"""module that stores stores file objects"""


class FileStorage:
    """Defining a class that serializes and deserializes

    Args:
        file_path (str): string path to json file
        objects (dict): stores objects format <class_name>.id
    """
    __file_path = "model_json"
    __objects = {}

    def all(self):
        """returns the class attribute i.e., dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """saves obj to objects dict"""
        my_key = obj.__class__.__name___
        key = f"{my_key}.{pbj.id}"
        self.__objects[key] = obj
    
    def save(self):
        """serializes objects to json file"""
        obj_serialization = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_serializaion, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                my_json_dict = json.load(f)

