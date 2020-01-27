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
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes the JSON string rep"""
        name_file = cls.__name__+".json"
        with open(name_file, 'w') as file_name:
            if list_objs is None:
                file_name.write("[]")
            else:
                dic = [i.to_dictionary() for i in list_objs]
                file_name.write(cls.to_json_string(dic))
