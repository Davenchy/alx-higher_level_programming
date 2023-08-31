#!/usr/bin/python3
"""find the peak in a list"""


def find_peak(list_of_integers):
    """find the peak in a list of integers

    Args:
        list_of_integers (int[]): list of integers

    Examples:
        >>> find_peak([1, 2, 4, 6, 3])
        6

        >>> find_peak([4, 3, 2, 1])
        4

        >>> find_peak([1, 2, 3, 4, 5])
        5

        >>> find_peak([4, 2, 1, 2, 3, 1])
        3

        >>> find_peak([]) is None
        True

        >>> find_peak([1])
        1

        >>> find_peak([2, 2, 2])
        2

    Returns:
        (int|None) The peak of the list of integers or None"""

    if list_of_integers is None:
        return None

    length = len(list_of_integers)
    if length == 0:
        return None
    if length <= 3:
        return max(list_of_integers)

    data = list_of_integers
    i = length // 2

    while True:
        if i == length - 1 or i == 0:
            return data[i]
        a, x, b = data[i - 1], data[i], data[i + 1]
        if x >= a and x >= b:
            return x
        i = i // 2 if a > b else i + (length - i) // 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
