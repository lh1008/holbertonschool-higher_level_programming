#!/usr/bin/python3
"""Module that returns the number of lines"""


def number_of_lines(filename=""):
    """Function that returns the number of line in a text file"""
    with open('my_file_0.txt', 'r') as file_name:
        return len(file_name.read().split('\n')) - 1
