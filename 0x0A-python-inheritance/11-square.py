#!/usr/bin/python3
"""
Module for Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Method init for size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
