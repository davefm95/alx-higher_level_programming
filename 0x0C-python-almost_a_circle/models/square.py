#!/usr/bin/python3
"""The Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """inits square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string of instanve"""
        st = "[Square] ({:d}) {:d}/{:d}".format(self.id, self.x, self.y)
        return "{:s} - {:d}".format(st, self.width)

    @property
    def size(self):
        """returns the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates square onst"""
        if len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
        else:
            if len(args) == 1:
                self.id, = args
            elif len(args) == 2:
                self.id, self.size = args
            elif len(args) == 3:
                self.id, self.size, self.x = args
            elif len(args) >= 4:
                self.id, self.size, self.x, self.y = args

    def to_dictionary(self):
        """Returns dict"""
        dct = {}
        dct["id"] = self.id
        dct["size"] = self.size
        dct["x"] = self.x
        dct["y"] = self.y
        return dct
