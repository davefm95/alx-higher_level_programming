#!/usr/bin/python3
"""This the rectangle module that inheruts from base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """inits Rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets width"""
        return self.__width

    @property
    def height(self):
        """returns height"""
        return self.__height

    @property
    def x(self):
        """gets x"""
        return self.__x

    @property
    def y(self):
        """gets y"""
        return self.__y

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """sets x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """sets y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns AreA"""
        return self.width * self.height

    def display(self):
        """Displays the rect with a character"""
        rectangle = ""
        print_symbol = "#"
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + (print_symbol*self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """returns a string"""
        st = "[Rectangle] ({:d}) {:d}/{:d}".format(self.id, self.x, self.y)
        return "{:s} - {:d}/{:d}".format(st, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates the instance variables"""
        if len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
        else:
            if len(args) == 1:
                self.id, = args
            elif len(args) == 2:
                self.id, self.width = args
            elif len(args) == 3:
                self.id, self.width, self.height = args
            elif len(args) == 4:
                self.id, self.width, self.height, self.x = args
            elif len(args) >= 5:
                self.id, self.width, self.height, self.x, self.y = args

    def to_dictionary(self):
        """returns dictionary object"""
        dct = {}
        dct["id"] = self.id
        dct["width"] = self.width
        dct["height"] = self.height
        dct["x"] = self.x
        dct["y"] = self.y
        return dct
