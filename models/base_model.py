#!/usr/bin/python3
"""importing modules"""
import uuid
from datetime import datetime
from models import storage


"""This module defines a class called BaseModel"""


class BaseModel:

    """
    The model class contains functions and attributes


    id (str): unique id of the objects created
    """
    def __init__(self, *args, **kwargs):
        """Initiaizing the base class

        args:
            args (): a variable length of arguments args is not used though
            kwargs these are key word argumensts
        attributes
            id (sr): a unique identify for objects
            created_at: time when object was created
            updated_at (datetime): time when object was updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        self.created_at = datetime.strptime(kwargs["created_at"],
                                                            '%Y-%m-%dT%H:%M:%S.%f')
                    elif key == "updated_at":
                        self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            storage.new(self)

    def save(self):
        """This function updates time when object is modified"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Function returning dictionary representation of object
        Returns:
        dict: dictionary representation of the base model object
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """returns the string representation of objects"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
