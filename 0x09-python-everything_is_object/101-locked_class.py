#!/usr/bin/python3
"""Locked class"""


class LockedClass:
    """
        Prevent the user from instantiating new attributes
        for anything but first_name
    """

    __slots__ = ["first_name"]
