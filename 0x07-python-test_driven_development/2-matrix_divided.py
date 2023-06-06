#!/usr/bin/python3
"""Module to divide a matrix by a number"""


def __validate_matrix_rows(matrix):
    """valdate all matrix rows to be of the same length and to have nums only
    matrix (list[list[int|float]]): A list of lists of numbers"""
    n = -1
    for row in matrix:
        if not isinstance(row, list):
            return False
        if n == -1:
            n = len(row)
        elif len(row) != n:
            return False
        for x in row:
            if not isinstance(x, (int, float)):
                return False
    return True


def matrix_divided(matrix, div):
    """Divide matrix by a number
    matrix (list[list[int|float]]): A list of lists of numbers
    div: the number to divide by (can not be zero)"""
    if type(matrix) is not list or not __validate_matrix_rows(matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[float("{:.2f}".format(x / div)) for x in row] for row in matrix]
