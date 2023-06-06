#!/usr/bin/python3
"""Module to print square with side size"""


def print_square(size):
    """prints a square using '#' char to the stdout
    size (int): the size of a square size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    [print("".join(["#" for _ in range(size)])) for _ in range(size)]
