#!/usr/bin/python3
"""
Module for exact same object
"""


def is_same_class(obj, a_class):
    """
    Method that will return True if the object is exaclty
    as specified
    """
    return type(obj) is a_class
