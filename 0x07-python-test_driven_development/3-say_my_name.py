#!/usr/bin/python3
"""Module to print first and last names to stdout"""


def say_my_name(first_name, last_name=""):
    """prints fullname
    first_name (str): the first name
    last_name (str): the last name (default = "")"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
