#!/usr/bin/python3

"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """    Appends a string to end of  file.    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
