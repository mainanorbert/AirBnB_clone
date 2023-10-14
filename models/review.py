#!/usr/bin/python3
"""Module that has the review model for ABNB"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class the defines the review of a place
    Args:
        place_id (str): empty string with place of Place.id
        user_id (str): User.id
        text (str): empty string
    """
    place_id = ""
    user_id = ""
    test = ""
