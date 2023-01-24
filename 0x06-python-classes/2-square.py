#!/usr/bin/python3
"""This module defins a class square
"""


class Square():
    """Square class definition
    """
    def __init__(self, size=0):
        """Initializes a square with given size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
