#!/usr/bin/python3

"""NQueens problem solution"""

from sys import stderr, argv


def find_sutables(queen, n):
    """Find sutable next queen values for the current queen
        Args:
            queen (int): the queen index in a row
            n: the row length
        Returns: List with sutable queens indexes in the next row
        Examples:
            >>> find_sutables(0, 4)
            [2, 3]

            >>> find_sutables(1, 4)
            [3]

            >>> find_sutables(2, 6)
            [0, 4, 5]
        """
    if type(queen) is not int:
        raise TypeError("queen must be an integer")
    if queen < 0 or queen >= n:
        raise IndexError("queen is out of range")
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n < 4:
        raise ValueError("n must be >= 4")

    queens = [i for i in range(n)]
    if queen == 0:
        return queens[2:]
    elif queen == n - 1:
        return queens[:-2]
    else:
        return queens[0:queen - 1] + queens[queen+2:]


def generate_steps(queen, step, n):
    """Iterates through (row, column) + step, as row and column in range ]0, n]
    Args:
        queen (tuple(int, int)): the queen coordinate
        step (tuple(int, int)): the step to add to the queen each iteration
        n (int): the board size (n == columns, n == rows)
    Return: Iterable(tuple(int, int))
    Examples:
        >>> [x for x in generate_steps((2, 2), (0, 1), 5)]
        [(2, 3), (2, 4)]

        >>> [x for x in generate_steps((2, 2), (-1, 1), 5)]
        [(1, 3), (0, 4)]"""
    if (type(queen) is not tuple or
            len(queen) != 2 or not all([type(x) is int for x in queen])):
        raise TypeError("queen must be a tuple(int, int)")
    if (type(step) is not tuple or
            len(step) != 2 or not all([type(x) is int for x in step])):
        raise TypeError("queen must be a tuple(int, int)")
    if type(n) is not int:
        raise TypeError("n must be an integer")

    a, b = step
    x, y = queen[0] + a, queen[1] + b
    while x >= 0 and x < n and y >= 0 and y < n:
        yield x, y
        x += a
        y += b


def check_board(n, queens):
    """Checks if the board has (n) queens all in idle state
    Args:
        n (int): the size of the board
        queens (list[int]): list of integers each one represents a queen
            index in a row
    Returns: True or False
    Examples:
        >>> check_board(4, [1, 3, 0, 2])
        True

        >>> check_board(3, [1, 3, 0])
        True

        >>> check_board(5, [1, 3, 0, 4, 2])
        False

        >>> check_board(3, [1, 3, 0, 2])
        Traceback (most recent call last):
        ValueError: length of queens must be equal to n"""
    if type(n) is not int:
        raise TypeError("n must be an intgere")
    if type(queens) is not list or not all(type(x) is int for x in queens):
        raise TypeError("queens must be a list of integers")
    if len(queens) != n:
        raise ValueError("length of queens must be equal to n")

    coordinates = list(enumerate(queens))
    for x in coordinates:
        for c in generate_steps(x, (1, 1), n):
            if c in coordinates:
                return False
        for c in generate_steps(x, (-1, 1), n):
            if c in coordinates:
                return False
        for c in generate_steps(x, (1, -1), n):
            if c in coordinates:
                return False
        for c in generate_steps(x, (-1, -1), n):
            if c in coordinates:
                return False
    return True


def solve(n, queens, hold):
    """Solves nqueens problem by returning list of queen index in each row
    Args:
        n (int): number of queens also the board size
        queens (list(int)): A list of queens that has the first queen index
        hold: (list(int)): A list of the remaining queens
    Examples:
        >>> solve(4, [2], [0, 1, 3])
        [2, 0, 3, 1]

        >>> solve(4, [1], [0, 2, 3])
        [1, 3, 0, 2]"""
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if type(queens) is not list or not all(type(x) is int for x in queens):
        raise TypeError("queens must be a list of intgeres")
    if type(hold) is not list or not all(type(x) is int for x in hold):
        raise TypeError("hold must be a list of intgeres")

    if len(queens) == n and check_board(n, queens):
        return queens
    for x in hold:
        q = queens[-1]
        if x not in find_sutables(q, n):
            continue
        qs = queens[:] + [x]
        h = hold[:]
        h.remove(x)
        s = solve(n, qs, h)
        if s:
            return s


if __name__ == "__main__":
    # check number of arguments
    if len(argv) != 2:
        print("Usage: nqueens N", file=stderr)
        exit(1)

    # try to get N from arguments
    try:
        N = int(argv[1])
    except Exception:
        print("N must be a number", file=stderr)
        exit(1)

    if N < 4:
        print("N must be at least 4", file=stderr)
        exit(1)

    for curr in range(1, N - 1):
        sol = solve(N, [curr], [i for i in range(N) if i != curr])
        print(list(enumerate(sol)))
