#!/usr/bin/python3
"""Module of a rectangle that inherits from base"""


class Base:
    """First Class-Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """Class Rectangle that inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Method class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """Gets the value width"""
            return self.width

        @width.setter
        def width(self, value):
            """Sets the value width"""
            self.width = value
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise TypeError("width must be >= 0")

        @property
        def height(self):
            """Gets the value height"""
            return self.height

        @height.setter
        def height(self, value):
            """Sets the value height"""
            self.height = value
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise TypeError("width must be >= 0")

        @property
        def x(self):
            """Gets the value x"""
            return self.x

        @x.setter
        def x(self, value):
            """Sets the value x"""
            self.x = value
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise TypeError("width must be >= 0")

        @property
        def y(self):
            """Gets the value y"""
            return self.y

        @y.setter
        def y(self, value):
            """Sets the value y"""
            self.y = value
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise TypeError("width must be >= 0")
