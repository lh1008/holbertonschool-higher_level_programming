#!/usr/bin/python3
"""
Module that returns a dictionary description with simple
data structure
"""


def class_to_json(obj):
    """Method serialization of an object"""
    return obj.__dict__
