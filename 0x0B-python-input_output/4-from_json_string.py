#!/usr/bin/python3
"""A model that contains a function that converts json string into object"""

import json


def from_json_string(my_str):
    """converts ''my_str'' into a python object
    Args:
        my_str (str): the json string to parse
    """
    return json.loads(my_str)
