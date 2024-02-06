#!/usr/bin/python3

"""    Class Student    """


class Student:

    """Represent a student."""

    def __init__(self, first_name, last_name, age):

        """    Initialize new Student    """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """     Return dictionary representation of Student    """

        return self.__dict__
