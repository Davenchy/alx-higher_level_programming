#!/usr/bin/python3
"""Module of 2x matrix multiplication"""


def matrix_mul(m_a, m_b):
    """multiply to matrices together
    Args:
        m_a (list[list[int|float]]): the first matrix
        m_b (list[list[int|float]]): the second matrix
    Returns a new matrix with the result"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not all(type(m) is list for m in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(m) is list for m in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    if not all(all(isinstance(y, (int, float)) for y in x) for x in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(y, (int, float)) for y in x) for x in m_b):
        raise TypeError("m_b should contain only integers or floats")
    na = len(m_a[0])
    for r in m_a:
        if len(r) != na:
            raise TypeError("each row of m_a must be of the same size")
    nb = len(m_b[0])
    for r in m_b:
        if len(r) != nb:
            raise TypeError("each row of m_b must be of the same size")
    if len(m_b) != na:
        raise ValueError("m_a and m_b can't be multiplied")
    m = []
    for row in m_a:
        r = []
        for col in zip(*m_b):
            r.append(sum(x * y for x, y in zip(row, col)))
        m.append(r)
    return m
