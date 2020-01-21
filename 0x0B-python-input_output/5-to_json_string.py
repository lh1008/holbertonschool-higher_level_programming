#!/usr/bin/python3
"""Module that returns the JSON representation"""
import json


def to_json_string(my_obj):
    """"Method that returns the object(string)"""
    return json.dumps(my_obj)
