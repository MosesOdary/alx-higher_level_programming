#!/usr/bin/python3

"""Textfile reading function"""


def read_file(filename=""):

    """Print UTF8 text file to stdout."""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
