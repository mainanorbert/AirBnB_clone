#!/usr/bin/python3
"""Module defines class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):

    """defing class for users details
    Args:
    email (str): contains user email
    password (str): stores user password
    first_name (str): first name of user
    last_name (str): last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
