#!/usr/bin/python3
"""Module that creates an Object from a 'JSON file'"""
import json


def load_from_json_file(filename):
    """Method that creates the object"""
    with open(filename, 'r') as file_name:
        return json.loads(file_name.read())
