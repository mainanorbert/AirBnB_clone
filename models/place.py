#!/usr/bin/python3
"""This module defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """The class represents a place model.

    Args:
        city_id (str): id of the cty
        user_id (str): User.id
        name (str): The name of the place.
        description (str): The description of the place for ABNB.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): No of bathrooms the specific place has
        max_guest (int): Max. no of guests a place has.
        price_by_night (int): The cost per night of the place.
        latitude (float): Latitude of the place.
        longitude (float): Longitude of the place.
        amenity_ids (list): Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
