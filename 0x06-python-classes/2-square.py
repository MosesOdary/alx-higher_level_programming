#!/usr/bin/python3
"""Create a square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """
        Initialize square

            Args:
                size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
