#!/usr/bin/python3
"""Module that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Method using a JSON represntation that writes an
    object to a text file
    """
    with open(filename, 'w') as file_name:
        return file_name.write(json.dumps(my_obj))
