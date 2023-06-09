#!/usr/bin/python3
"""Module to add two integers together"""


def add_integer(a, b=98):
    """Adds two numbers
    a (int|float): the first number
    b (int|float): the second number (default = 98)"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return int(a) + int(b)
