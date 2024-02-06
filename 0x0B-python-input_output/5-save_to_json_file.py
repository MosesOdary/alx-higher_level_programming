#!/usr/bin/python3

"""    Defines a JSON file-writing function    """

import json


def save_to_json_file(my_obj, filename):

    """    Write object to text file with JSON    """

    with open(filename, "w") as f:
        json.dump(my_obj, f)
