#!/usr/bin/python3
"""A model that contains a function that reads a files
and convertes its content as a json string into an object"""

import json


def load_from_json_file(filename):
    """load json string from ``filename`` file and convert it into an object
    Args:
        filename (str): the file name to read json content from"""
    obj = None
    with open(filename, 'r') as f:
        json_str = f.read()
        obj = json.loads(json_str)
    return obj
