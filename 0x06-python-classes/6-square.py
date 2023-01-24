#!/usr/bin/python3
"""This module defins a class square
"""


class Square():
    """Square class definition
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with given size
        """
        self.size = size
        self.position = position

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
                if self.__position[0] > 0:
                    for k in range(self.__position[0]):
                        print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        """returns the position attributes of the square
        """
        return self.__position
    @position.setter
    def position(self, value):
        """Sets the position attributes of the square
        """
        if type(value) != tuple or type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) > 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
