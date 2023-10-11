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
    __file_path = "my_objects.json"
    __objects = {}

    def all(self):
        """returns the class attribute i.e., dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """saves obj to objects dict"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects.update({key: obj})
    
    def save(self):
        """serializes objects to json file"""
        obj_serialization ={}
        obj_serialization = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_serializaion, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    # module = __import__('models.{}'.format(class_name), fromlist=[class_name])
                    # cls = getattr(module, class_name)
                    # instance = cls(**value)
                    # self.__objects[key] = instance
                    cls = eval(class_name)
                    obj = cls(**value)
