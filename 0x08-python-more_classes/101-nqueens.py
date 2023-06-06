#!/usr/bin/python3

"""NQueens problem solution"""

from sys import stderr, argv


class BoardSolution:
    """The board sorted solution"""

    queen_symbol = "x"
    empty_symbol = "-"
    space_symbol = " "

    def __init__(self, board, solution_index):
        """Initialize a new board solution

        Args:
            board (board): the board object
            solution_index (int): the solution index"""
        if not isinstance(board, Board):
            raise TypeError("board must be Board instance")
        if type(solution_index) is not int:
            raise TypeError("n must be an integer")
        if solution_index >= board.number_of_solutions:
            raise IndexError(f"n is out of range: {board.number_of_solutions}")
        self.__board = board
        self.__index = solution_index
        self.__N = board.N

    def __get_sutables(self, q) -> list[int]:
        """Returns the sutable next or prev row queen indexes for queen q

        Args:
            q (int): the queen index

        Examples:
            # create board with 4 rows x 4 cols
            >>> board = Board(4)

            # loads solution of index 0
            # to get the number of solutions
            # check ``board.number_of_solutions``
            >>> sol = BoardSolution(board, 0)

            # the queen(q) at col 0 expects queen at col 2 or 3
            # for the next or prev row at board that has 4 cols
            >>> sol._BoardSolution__get_sutables(0)
            [2, 3]

            >>> sol._BoardSolution__get_sutables(2)
            [0]

            >>> sol._BoardSolution__get_sutables(3)
            [0, 1]

            >>> sol._BoardSolution__get_sutables(4)
            Traceback (most recent call last):
            ValueError: q value out of range: 4: 3

        Returns: List of integers (the sutable indexes)
        """
        if type(q) is not int:
            raise ValueError("q must be an integer")
        n = self.__N
        if 0 < q >= n or q < 0:
            raise ValueError(
                f"q value out of range: {q}: {self.__N - 1}")

        qs = self.__board.queens
        if q == 0:
            return qs[2:]
        elif q == n - 1:
            return qs[0:-2]
        else:
            return qs[0:q - 1] + qs[q + 2:]

    def __pick_next(self, sutables, queens) -> int | None:
        """Returns the next suitable queen

        Args:
            sutables (int[]): list of sutable queens
            queens (int[]): the current avalible queens list

        Examples:
            >>> board = Board(4)
            >>> sol = board.get_solution(0)

            >>> sol._BoardSolution__pick_next([0, 1], [2, 1, 3])
            1

            >>> sol._BoardSolution__pick_next([0, 1], [2, 1, 3, 0])
            0

            >>> sol._BoardSolution__pick_next("a", [2, 1, 3, 0])
            Traceback (most recent call last):
            TypeError: sutables must be a list

            >>> sol._BoardSolution__pick_next([0, 1], "queens")
            Traceback (most recent call last):
            TypeError: queens must be a list
            """
        if type(sutables) is not list:
            raise TypeError("sutables must be a list")
        if type(queens) is not list:
            raise TypeError("queens must be a list")
        for x in sutables:
            if x in queens:
                return x

    def solve(self):
        """Start solving the board

        Examples:
            >>> board = Board(4)
            >>> board.get_solution(0)"""
        current = self.__index + 1
        queens = self.__board.queens
        solution = []

        while current is not None:
            # push current to solution
            solution.append(current)
            queens.remove(current)

            # find next of current and set as current for next iteration
            suts = self.__get_sutables(current)
            pick = self.__pick_next(suts, queens)
            current = pick

        if len(queens) > 0:
            suts = self.__get_sutables(queens[0])
            if solution[0] in suts:
                solution.insert(0, queens[0])

        self.__queens = solution

    def print(self):
        """Print solution board using ``BoardSolution.queen_symbol`` and
        ``BoardSolution.empty_symbol``"""
        for q in self:
            print(self.space_symbol.join(
                [(self.queen_symbol if i == q else self.empty_symbol)
                    for i in range(self.__N)]))

    def __iter__(self):
        if not hasattr(self, "_BoardSolution__queens"):
            return [].__iter__()
        else:
            return self.__queens.__iter__()

    def __len__(self):
        if not hasattr(self, "_BoardSolution__queens"):
            return 0
        return len(self.__queens)

    def __getitem__(self, index) -> int:
        if not hasattr(self, "_BoardSolution__queens"):
            raise IndexError("index out of range")
        return self.__queens[index]

    def __str__(self):
        if len(self) == 0:
            return "BoardSolution(Not Solved)"
        return ", ".join([f"{n}" for n in self.__queens])


class Board:
    """Board that contains queens sorted as required"""
    def __init__(self, N):
        """Initialize a new Board instance and generate queens

        Args:
            N (int): The board dimensions and the queens count (N >= 4)"""
        if N < 4:
            raise ValueError("N must be at least 4")
        self.__N = N
        self.__queens = [i for i in range(N)]

    @property
    def N(self):
        """The board dimensions and the queens count"""
        return self.__N

    @property
    def queens(self):
        """A copy list of the generated queens list with the default sort"""
        return self.__queens[:]

    @property
    def number_of_solutions(self):
        """The number of avalible solutions for current board

        Examples:
            >>> Board(4).number_of_solutions
            2

            >>> Board(6).number_of_solutions
            4"""
        return self.__N - 2

    def get_solution(self, n) -> BoardSolution:
        """Return solution by its index
        Check Board.number_of_solutions to get the number of the avalible
        solutions

        Args:
            n (int): the index of the solution

        Examples:
            >>> isinstance(Board(4).get_solution(0), BoardSolution)
            True

            >>> Board(4).get_solution(4)
            Traceback (most recent call last):
            IndexError: n is out of range: 2
            """
        sol = BoardSolution(self, n)
        sol.solve()
        return sol

    def __iter__(self):
        return BoardIterator(self)


class BoardIterator:
    """A class to iterate through the board solutions"""
    def __init__(self, board):
        """Initialize board iterator class

        Args:
            board (Board): the board object to iterate through its solutions"""
        if not isinstance(board, Board):
            raise TypeError("board must be an instance of Board")
        self.__board = board
        self.__solutions = board.number_of_solutions
        self.__current_solution = -1

    def __next__(self) -> BoardSolution:
        if self.__current_solution < self.__solutions - 1:
            self.__current_solution += 1
            return self.__board.get_solution(self.__current_solution)
        raise StopIteration


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

    board = Board(N)
    for solution in board:
        print(list(map(lambda e: list(e), enumerate(solution))))
