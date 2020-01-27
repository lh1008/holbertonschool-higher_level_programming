#!/usr/bin/python3
"""Module of a square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor method for square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Method overloading a square"""
        size = self.size
        x = self.x
        y = self.y
        i = self.id
        return '[Square] ({}) {}/{} - {}'.format(i, x, y, size)


    @property
    def size(self):
        """Sets the value of width"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value width"""
        self.width = value
        self.height = value
        self.__size = value

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
