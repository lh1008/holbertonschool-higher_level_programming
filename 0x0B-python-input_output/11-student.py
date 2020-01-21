#!/usr/bin/python3
"""Module that writes a class Student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Method public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method that retrieves a dictionary"""
        return self.__dict__
