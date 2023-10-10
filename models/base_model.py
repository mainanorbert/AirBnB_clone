#!/usr/bin/python3
"""importing modules"""
import uuid
from datetime import datetime


"""This module defines a class called BaseModel"""


class BaseModel:

    """
    The model class contains functions and attributes


    id (str): unique id of the objects created
    """
    def __init__(self, *args, **kwargs):
        """Initiaizing the base class

        args:
            id (str): unique id for each object created
            created_at (datetime): time when object was created
            updated_at (datetime): time when object was updated
        """
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        """This function updates time when object is modified"""
        self.updated_at = datetime.now()

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
