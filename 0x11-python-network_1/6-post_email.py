#!/usr/bin/python3
"""Script that sends a POST request with email param"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    res = requests.post(url, data)
    value = res.text
    print(value)
