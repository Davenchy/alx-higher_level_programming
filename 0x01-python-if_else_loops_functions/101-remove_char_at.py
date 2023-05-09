#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        n = len(str) + n
    a = str[:n]
    b = str[n+1:]
    return a + b
