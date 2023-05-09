#!/usr/bin/python3
for c in range(97, 97 + 26):
    if chr(c) not in ['e', 'q']:
        print("{:c}".format(c), end="")
