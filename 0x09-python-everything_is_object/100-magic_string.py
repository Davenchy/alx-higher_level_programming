#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "_n", getattr(magic_string, "_n", 0) + 1)
    return ", ".join(["BestSchool"] * getattr(magic_string, "_n"))
