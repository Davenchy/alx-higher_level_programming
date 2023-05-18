#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = filter(lambda item: item[1] == value, a_dictionary.items())
    for key in set(keys):
        del a_dictionary[key[0]]
    return a_dictionary
