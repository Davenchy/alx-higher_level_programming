#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = None
    for n in my_list:
        if max is None or n > max:
            max = n
    return max
