#!/usr/bin/python3
"""A model that contains a function that convertes json object into string"""

import json


def to_json_string(my_obj):
    """converts object into json string without handling exceptions
    Args:
        my_obj: object to convert
    Returns:
        json string
    """
    return json.dumps(my_obj)
