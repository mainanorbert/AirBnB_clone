#!/usr/bin/python3
"""module that with code on the city where with ABNB"""
from models.base_model import BaseModel


class City(BaseModel):
    """class defining the city and state id for ABNB
    Args:
        state_id (str): id of the state
        name (str): name of the city
    """
    state_id = ""
    name = ""
