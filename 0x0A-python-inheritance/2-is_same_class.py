#!/usr/bin/python3

"""Instance checker class"""


def is_same_class(obj, a_class):
    """
    Return True if object is exact instance of specified class otherwise False
    """
    if type(obj) == a_class:
        return True

    return False
