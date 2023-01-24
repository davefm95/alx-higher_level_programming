#!/usr/bin/python3
"""This module defins a class square
"""


class Square():
    """Square class definition
    """
    def __init__(self, size=0):
        """Initializes a square with given size
        """
        self.size = size

    @property
    def size(self):
        """Return s the size of fhe square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """ThIs prints the swuare to stdout
        """
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
