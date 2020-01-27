#!/usr/bin/python3
"""Module for first class Base"""
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of the JSON string rep"""
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method that returns an instance with all attributes"""
        if cls.__name__ == 'Rectangle':
            new_obj = cls(2, 2)
        elif cls.__name__ == 'Square':
            new_obj = cls(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """Method that returnsa list of instances"""
        name_file = cls.__name__+".json"
        if not os.path.isfile(name_file):
                return []
        with open(name_file, 'r') as file_name:
           mafe =  cls.from_json_string(file_name.read())
           inst = []
           for i in mafe:
               inst.append(cls.create(**i))
        return inst
