#!/usr/bin/python3
"""A script that appends all arguments as an array to a json file"""

from sys import argv

filename = "add_item.json"
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

data += argv[1:]

save_to_json_file(data, filename)
