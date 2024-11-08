#!/usr/bin/python3
"""N queens puzzle: place N non-attacking queens on an NxN chessboard."""

from sys import argv


def is_NQueen(cell: list) -> bool:
    """Check if the last queen placement does not cause a conflict."""
    row_number = len(cell) - 1
    for index in range(0, row_number):
        # Check for column or diagonal conflicts
        if cell[index] == cell[row_number] or abs(cell[index] - cell[row_number]) == row_number - index:
            return False
    return True


def solve_NQueens(dimension: int, row: int, cell: list):
    """Recursively solve N Queens problem and print all solutions."""
    if row == dimension:
        print([[i, cell[i]] for i in range(dimension)])
    else:
        for column in range(dimension):
            cell.append(column)
            if is_NQueen(cell):
                solve_NQueens(dimension, row + 1, cell)
            cell.pop()


# Input validation
if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)
try:
    N = int(argv[1])
except ValueError:
    print('N must be a number')
    exit(1)
if N < 4:
    print('N must be at least 4')
    exit(1)

# Solve the N-Queens problem
solve_NQueens(N, 0, [])

