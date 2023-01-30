#!/usr/bin/python3
""" A module that defines a Rectangle class.
"""


class Rectangle:
    """Represents a four sided quadrilateral with Perpendicular sides
    """
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a square with given width and height
        """
        self.width = width
        self.height = height
        try:
            self.__width
        except NameError:
            pass
        else:
            w = 1
        try:
            self.__height
        except NameError:
            pass
        else:
            h = 1
        if h == 1 and w == 1:
            Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Returns informal string relresentation of object
        """
        if self.__width == 0 or self.__height == 0:
            string = ""
        else:
            string = ""
            s = str(self.print_symbol)
            w = self.width
            h = self.height
            for i in range(h):
                for j in range(w):
                    string += s
                if i != h - 1:
                    string += "\n"
        return string

    def __repr__(self):
        """Returns official string representation of object
        """
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        """Destructor method
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
