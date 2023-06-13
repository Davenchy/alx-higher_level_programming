#!/usr/bin/python3
"""A model that contains a function that convertes json object into string"""

import json


def to_json_string(my_obj):
    return json.dumps(my_obj)
