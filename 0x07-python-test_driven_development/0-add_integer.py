#!/usr/bin/python3
"""
Module to add two integers
a: integer
b: integer
"""

def add_integer(a, b=98):
    """
    Add_integer function
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
