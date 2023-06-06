#!/usr/bin/python3

def text_indentation(text):
    """Prints text to stdout with a blankline after each ., ? and :
    text (str): the message to print"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(":", ":|")
    text = text.replace("?", "?|")
    text = text.replace(".", ".|")
    print("\n\n".join(map(lambda line: line.strip(), text.split("|"))), end="")
