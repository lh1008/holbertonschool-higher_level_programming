#!/usr/bin/python3
"""Module of a square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor method for square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method overloading a square"""
        return '[Square] ({self.id}) {self.x}/{self.y} - {self.width}'.format(self=self)
