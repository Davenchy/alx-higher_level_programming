#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    max_item = None
    for item in a_dictionary.items():
        if max_item is None or item[1] > max_item[1]:
            max_item = item
    return max_item[0] if max_item is not None else None
