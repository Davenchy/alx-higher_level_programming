#!/usr/bin/python3
"""find the peak in a list"""


def find_peak(list_of_integers):
    """find the peak in a list of integers

    Args:
        list_of_integers (int[]): list of integers

    Examples:
        >>> find_peak([1, 2, 4, 6, 3])
        6

        >>> find_peak([]) is None
        True

        >>> find_peak([1])
        1

        >>> find_peak([2, 2, 2])
        2

    Returns:
        (int|None) The peak of the list of integers or None"""

    peak = None
    if list_of_integers is not None:
        for n in list_of_integers:
            if peak is None or n > peak:
                peak = n
    return peak


if __name__ == '__main__':
    import doctest
    doctest.testmod()
