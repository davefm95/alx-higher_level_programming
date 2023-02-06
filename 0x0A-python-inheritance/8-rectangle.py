#!/usr/bin/python3
"""This module contains the rectangle class"""


class Rectangle(BaseGeometry):
    """This class inherits from baae geometry"""
    def __init__(self, width, height):
        """init method fro rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = heightn
