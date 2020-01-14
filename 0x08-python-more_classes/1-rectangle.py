#!/usr/bin/python3
"""Rectangle module that defines a square"""
class Rectangle:
    """Class rectangle"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        print(whatever)
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")

    @property
    def height(self):
        print(other-word)
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
