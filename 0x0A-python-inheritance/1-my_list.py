#!/usr/bin/python3

"""MyList Class"""


class MyList(list):
    """Class MyList"""

    def print_sorted(self):
        """Print list in ascending order"""
        print(sorted(self))
