#!/usr/bin/python3
"""A model with a function that writes text to file"""


def write_file(filename="", text=""):
    """Writes ''text'' to ''filename''
    Args:
        filename (str): the filename to write text to
        text (str): the text to write to the file

    Examples:
    >>> write_file('my_text', "world")
    5"""
    writen = 0
    with open(filename, 'w') as file:
        writen = file.write(text)
    return writen
