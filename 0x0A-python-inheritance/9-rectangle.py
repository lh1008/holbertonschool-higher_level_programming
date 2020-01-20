#!/usr/bin/python3
"""
Module for empyt class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Method instantiationfor width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area of a Rectangle"""
        return self.__width*self.__height

    def __str__(self):
        """Informal string rectangle representation"""
        string = '['+type(self).__name__+'] '
        return string + "{}/{}".format(self.__width, self.__height)
