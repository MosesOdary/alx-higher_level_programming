#!/usr/bin/python3

"""Class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class Rectangle
    """
    def __init__(self, width, height):
        """Constructor"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """String method"""
        return "[Rectangle] " + str(self.__width) + '/' + str(self.__height)
