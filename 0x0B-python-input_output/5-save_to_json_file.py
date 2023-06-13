#!/usr/bin/python3
"""A model that contains a function that convertes json object into string
and writes it into a file"""

import json


def save_to_json_file(my_obj, filename):
    """converts ''my_obj'' into json string and write it into ''filename'' file
    Args:
        my_obj (object): object to convert
        filename (str): the filename to write the json string into
    """
    written = 0
    with open(filename, 'w') as f:
        json_str = json.dumps(my_obj)
        written = f.write(json_str)
    return written
