#!/usr/bin/python3
"""A module that contians a function that returns a list of lists represents
pascals triangle"""


def pascal_triangle(n):
    """Returns a list of lists represents pascals triangle"""
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
                continue
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle
