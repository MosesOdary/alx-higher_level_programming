#!/usr/bin/python3

"""Rectangle class."""


class Rectangle:
    """Rectangle."""

    def __init__(self, width=0, height=0):
        """
        Constructor -
        Args:
            width (int): Width of the rectangle. Default = 0.
            height (int): Height of the rectangle. Default = 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """integer: Get rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if ((value < 0)):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if ((value < 0)):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
