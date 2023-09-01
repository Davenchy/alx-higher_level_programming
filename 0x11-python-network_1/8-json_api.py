#!/usr/bin/python3
"""Script that fetches url and print json data with errors handling"""

import requests
import sys


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    res = requests.post(url, data={'q': letter})
    try:
        json = res.json()

        _id = json.get('id')
        name = json.get('name')

        if name is None or _id is None:
            print("No result")
        else:
            print("[{}] {}".format(_id, name))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
