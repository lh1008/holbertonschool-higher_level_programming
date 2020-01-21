#!/usr/bin/python3
"""Module that appends a string"""


def append_write(filename="", text=""):
    """
    Method that appends a string at the end of a text
    file and returns the number of characters
    """
    with open(filename, 'a+', encoding='utf-8') as file_name:
        return file_name.write(text)
