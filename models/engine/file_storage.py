import json
from os.path import isfile
from models.base_model import BaseModel


class FileStorage:
    """Defines a class that is used to store objects to json file

    Args:
        file_path (string): path to json file
        objects (dict): dictionary with class objects
        """
    __file_path = "objects_file.json"
    __objects = {}

    def all(self):
        """
        returns dictionay of all objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """"
        sets objs to obj to __objects with  key <obj class name>.id

        Args:
            obj (object): the object to add to dictionary
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        saves serialized objects to json file
        """
        obj_dict = {
                key: obj.to_dict()
                for key, obj in FileStorage.__objects.items()
                }
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes an json string to recreate an object"""
        if isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.load(file)
                for obj in obj_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    print(cls_name)
                    self.new(eval(cls_name)(**obj))
