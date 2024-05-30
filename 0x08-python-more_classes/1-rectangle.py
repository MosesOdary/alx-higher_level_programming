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
        elif ((value < 0)):
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
        elif ((value < 0)):
            raise ValueError("height must be >= 0")
        self.__height = value
