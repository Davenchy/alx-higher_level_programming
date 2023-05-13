#!/usr/bin/python3
def multiple_returns(sentence):
    strlen = len(sentence) if isinstance(sentence, str) else 0
    c = sentence[0] if strlen > 0 else None
    return strlen, c
