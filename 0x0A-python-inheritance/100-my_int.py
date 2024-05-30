#!/usr/bin/python3

"""Class MyInt"""


class MyInt(int):
    """Invert == and != operators"""

    def __eq__(self, value):
        """Override == opeartor with != functionality"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == functionality"""
        return self.real == value
