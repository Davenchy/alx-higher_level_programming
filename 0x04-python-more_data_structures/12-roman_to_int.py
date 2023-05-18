#!/usr/bin/python3

symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_string = roman_string.strip()
    last = None
    sum = 0
    for c in roman_string:
        value = symbols[c]
        if last is not None and last < value:
            sum += value - last * 2
        else:
            sum += value
        last = value
    return sum
