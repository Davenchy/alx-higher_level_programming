#!/usr/bin/python3
def weight_average(my_list=[]):
    total = sum(map(lambda t: t[1], my_list))
    prod = sum(map(lambda t: t[0] * t[1], my_list))
    return prod / total
