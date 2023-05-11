#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

ops = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def main():
    count = len(argv) - 1
    if count != 3:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2].strip()
    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    r = ops[op](a, b)
    print(f"{a} {op} {b} = {r}")


if __name__ == "__main__":
    main()
