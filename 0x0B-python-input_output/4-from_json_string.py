#!/usr/bin/python3

"""JSON-to-object"""

import json


def from_json_string(my_str):

    """    Return Pyobject representation of JSON string    """

    return json.loads(my_str)
