#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
msgs = ["", "greater than 5", "less than 6 and not 0"]
msgi = 0
digit = number % 10
digit = digit - 10 if number < 0 and digit else digit
if digit:
    msgi = 1 if digit > 5 else 2
print(f"Last digit of {number} is {digit}", end="")
print(f" and is {msgs[msgi]}" if msgi else "")
