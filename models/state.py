#!/usr/bin/python3
"""module that defines the state class for my project"""
from models.base_model import BaseModel


class State(BaseModel):
    """defining the state class with name of state for ABNB
    Args:
    name (str): name of the state
    """
    name = ""
