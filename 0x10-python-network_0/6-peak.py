#!/usr/bin/python3
"""    Find max number in list    """


def find_peak(list_of_integers):
    """    Find max number in list    """
    if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
