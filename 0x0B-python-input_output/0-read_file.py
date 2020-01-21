#!/usr/bin/python3
"""Module that reads a text file UTF8"""


def read_file(filename=""):
    """Method that printsit to stdout"""
    with open(filename, 'r') as r:
        for text in r:
            print(text, end='')
