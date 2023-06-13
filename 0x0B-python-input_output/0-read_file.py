#!/usr/bin/python3
"""A model that conntains a function that reads the content of a file and
prints it to stdout"""


def read_file(filename=""):
    """A function that reads the content of a file and prints it into stdout
    Args:
        filename (string): The file name to open and read it content"""
    with open(filename, "r") as file:
        for line in file:
            print(line, end="")
