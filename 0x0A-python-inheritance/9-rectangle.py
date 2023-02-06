#!/usr/bin/python3
"""This module contains the rectangle class"""


class BaseGeometry:
    """This class defines a base geometry object"""
    def area(self):
        """This function raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function validates the variable value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This class inherits from baae geometry"""
    def __init__(self, width, height):
        """init method fro rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """implements the area"""
        return self.__height * self.__width
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
