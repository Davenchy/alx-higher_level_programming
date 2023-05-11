#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def task(a, b, simple, fun):
    print("{:d} {} {:d} = {:d}".format(a, simple, b, fun(a, b)))


if __name__ == "__main__":
    a = 10
    b = 5
    task(a, b, "+", add)
    task(a, b, "-", sub)
    task(a, b, "*", mul)
    task(a, b, "/", div)
