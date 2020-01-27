#!/usr/bin/python3
"""Module of a rectangle that inherits from base"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Method class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the value width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the value height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the value x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the value y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area value of the Rectangle"""
        return self.__width*self.__height

    def display(self):
        """
        Method that prints in stdout
        with the character #
        """
        if self.__y:
            for i in range(self.__y):
                print()
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """Method str override"""
        ret = '[Rectangle] ({self.id})'.format(self=self)
        ret += '{self.x}/{self.y} - '.format(self=self)
        ret += '{self.width}/{self.height}'.format(self=self)
        return ret

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute"""
        list = ['id', 'width', 'height', 'x', 'y']
        if args:
            for arg in range(len(args)):
                setattr(self, list[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method that returns the dictionary rep of a Rectangle"""
        deec = self.__dict__
        list = ['id', 'width', 'height', 'x', 'y']
        res = {res: getattr(self, res) for res in list}
        return res
