#!/usr/bin/python3
"""Module that returns an JSON rep of an structure"""
import json


def from_json_string(my_str):
    """Method that returns the JSON structure object"""
    return json.loads(my_str)
