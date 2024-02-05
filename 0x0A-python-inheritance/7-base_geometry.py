#!/usr/bin/python3

"""Class BaseGeometry"""


class BaseGeometry:
    """Implements Area"""

    def area(self):
        """Unimplemented function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
