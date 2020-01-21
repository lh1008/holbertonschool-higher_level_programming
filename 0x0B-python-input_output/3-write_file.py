#!/usr/bin/python3
"""Module that writes a string to a text file"""


def write_file(filename="", text=""):
    """
    Method that writes a string and returns the number
    of characters
    """
    with open(filename, 'w', encoding='utf-8') as file_name:
        return file_name.write(text)
