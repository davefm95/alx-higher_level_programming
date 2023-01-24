#!/usr/bin/python3
"""This module creates a square object with a private size attribute
"""


class Square:
    """Defines a square class
    """
    def __init__(self, size):
        """Args:
               self (Square): The first parameter
               size (int): The second parameter

        Returns:
               Nothing
        """
        self.__size = size
