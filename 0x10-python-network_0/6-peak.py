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

    if list_of_integers is None:
        return None

    length = len(list_of_integers)
    if length == 0:
        return None

    return max(list_of_integers)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
