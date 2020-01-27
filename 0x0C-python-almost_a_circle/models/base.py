#!/usr/bin/python3
"""Module for first class Base"""
import json

class Base:
    """First Class-Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Method that returns the JSON string rep"""
        if list_dictionaries == None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
