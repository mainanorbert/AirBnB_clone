#!/usr/bin/python3
"""module that defines the amenities for ABNB"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The amenity class with model for amenities
    Args:
        name (str): name of the amenity"""
    name = ""
