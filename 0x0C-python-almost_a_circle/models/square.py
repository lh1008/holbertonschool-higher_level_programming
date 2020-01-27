#!/usr/bin/python3
"""Module of a square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor method for square"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Method overloading a square"""
        w = self.width
        x = self.x
        y = self.y
        i = self.id
        return '[Square] ({}) {}/{} - {}'.format(i, x, y, w)

    @property
    def size(self):
        """Sets the value of width"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method for args and kwargs"""
        list = ['id', 'size', 'x', 'y']
        if args:
            for arg in range(len(args)):
                setattr(self, list[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method that returns the dic rep of a Square"""
        deec = self.__dict__
        list = ['id', 'size', 'x', 'y']
        res = {res: getattr(self, res) for res in list}
        return res
