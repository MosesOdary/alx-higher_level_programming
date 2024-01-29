#!/usr/bin/python3

"""Class rectangle"""


class Rectangle:
    """Class Rectangle"""

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
        elif (value < 0):
            raise ValueError("Width must be a positive value")
        self.__width = value

    @property
    def height(self):
        """Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height is not an integer")
        elif (value < 0):
            raise ValueError("Height must be a positive value")
        self.__height = value
