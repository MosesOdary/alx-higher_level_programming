#!/usr/bin/python3

"""Class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area of the rectangle"""
        return (self.__width ** 2)

    def __str__(self):
        """String method"""
        return "[Rectangle] " + str(self.__width) + '/' + str(self.__height)
