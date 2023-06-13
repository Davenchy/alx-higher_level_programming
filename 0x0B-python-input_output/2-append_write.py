#!/usr/bin/python3
"""A model contains function that appends text to a file"""


def append_write(filename="", text=""):
    """Appends text to a file
    Args:
        filename (str): the file to append text to
        text (str): the text to append to the file"""
    written = 0
    with open(filename, "a") as file:
        written = file.write(text)
    return written
