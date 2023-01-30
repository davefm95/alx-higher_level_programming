#!/usr/bin/python3
""" A module that defines a Rectangle class.
"""


class Rectangle:
    """Represents a four sided quadrilateral with Perpendicular sides
    """
    def __init__(self, width=0, height=0):
        """Initializes a square with given width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setsbtye width of the rectangle
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns tue height of tue rectangel
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
