#!/usr/bin/python3
"""
N Queens module
"""

import sys


def is_safe(board, row, col, n):
    """
    Checks if it's safe to place a queen in a
    particular position
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

        for j in range(col):
            if board[i][j] == 1:
                if i + j == row + col or i - j == row - col:
                    return False

    return True


def n_queens(n):
    """
    Ensures n >= 4
    """
    if n < 4:
        return []

    def backtrack(row):
        """
        Backtracking algorithm
        """
        if row == n:
            solution = [list(row) for row in board]
            sols.append(solution)
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    sols = []
    board = [[0 for r in range(n)] for c in range(n)]
    backtrack(0)
    return sols


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    sols = n_queens(N)

    for sol in sols:
        for row in sol:
            print(row)
        print()
