#!/usr/bin/python3

"""Class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class Rectangle
    """
    def __init__(self, width, height):
        """Constructor"""
        self.integer_validation("width", width)
        self.__width = width
        self.integer_validation("height", height)
        self.__height = height
