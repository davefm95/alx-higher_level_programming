#!/usr/bin/python3
"""This the 6-base_geometry module"""


class BaseGeometry:
    """This class defines a base geometry object"""
    def area(self):
        """This function raises an exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """This function validates the variable value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
