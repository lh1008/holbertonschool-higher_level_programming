#!/usr/bin/python3
"""Module that inherits a list"""


class MyList(list):
    """Class MyList"""

    def print_sorted(self):
        """Public instance method that prints a list"""
        print(sorted(self))
