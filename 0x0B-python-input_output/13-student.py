#!/usr/bin/python3
"""Module that writes a class Student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Method public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary"""
        fick = self.__dict__
        if type(attrs) == list:
            if all(type(i) == str for i in attrs):
                return {n: fick[n] for n in fick if n in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Method that replaces all attributes"""
        for i in json.keys():
            self.__dict__[i] = json[i]
