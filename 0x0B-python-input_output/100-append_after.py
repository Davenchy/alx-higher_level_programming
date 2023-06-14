#!/usr/bin/python3
"""A module that contains a function that appends a line of text
after a matching line"""


def append_after(filename="", search_string="", new_string=""):
    """appends ''new_string'' after the line that contains ''search_string''
    in the file ''filename''

    Args:
        filename (str): the file name to append text into
        search_string (str): the string to match to append the ''new_string''
        after
        new_string (str): the string to append after the line that contains
        ''search_string''"""
    lines = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
            line = f.readline()

    with open(filename, 'w') as f:
        f.writelines(lines)
