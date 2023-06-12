#!/usr/bin/python3
"""A model that contains a custom int class called MyInt"""


class MyInt(int):
    """My custom int class"""
    def __eq__(self, value: object) -> bool:
        return super().__ne__(value)

    def __ne__(self, value: object) -> bool:
        return super().__eq__(value)
