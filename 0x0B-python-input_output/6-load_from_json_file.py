#!/usr/bin/python3

"""    JSON reading function    """
import json


def load_from_json_file(filename):

    """    Create Pyobject from JSON file    """

    with open(filename) as f:
        return json.load(f)
