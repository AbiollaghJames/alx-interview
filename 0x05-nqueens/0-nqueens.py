#!/usr/bin/python3
"""
N Queens module
"""

from sys import argv


def n_queens(cell: list) -> bool:
    """ returns bool if n queens """
    row_num = len(cell) - 1
    diff = 0
    for i in range(0, row_num):
        diff = cell[i] - cell[row_num]
        if diff < 0:
            diff *= -1
        if diff == 0 or diff == row_num - i:
            return False
    return True


def solve_n_queens(d: int, row: int, cell: list, output: list):
    """ gets result of N Queens recursively """
    if row == d:
        print(output)
    else:
        for col in range(0, d):
            cell.append(col)
            output.append([row, col])
            if (n_queens(cell)):
                solve_n_queens(d, row + 1, cell, output)
            cell.pop()
            output.pop()


if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        N = int(argv[1])
    except BaseException:
        print('N must be a number')
        exit(1)
    if N < 4:
        print('N must be at least 4')
        exit(1)
    else:
        output = []
        cell = 0
        solve_n_queens(int(N), cell, [], output)
