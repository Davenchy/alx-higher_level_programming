#!/usr/bin/python3
"""Simple program that prints that stats collected from stdin to stdout"""
from sys import stdin, stdout

counter = 0
total_size = 0
codes = {}
allowed_codes = [200, 301, 400, 401, 403, 404, 405, 500]


def print_data():
    """prints all the collected data to stdout"""
    print("File size: {:d}".format(total_size))
    for key in sorted(codes.keys()):
        print("{:d}: {:d}".format(key, codes[key]))
    stdout.flush()


try:
    while True:
        line = stdin.readline()
        data = line.split(" ")

        counter += 1
        total_size += int(data[-1])

        status = int(data[-2])
        if status in allowed_codes:
            codes[status] = codes[status] + 1 if status in codes else 1

        if counter == 10:
            print_data()
            counter = 0
except KeyboardInterrupt:
    print_data()
    exit()
