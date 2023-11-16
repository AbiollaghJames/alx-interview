#!/usr/bin/python3
'''
Rotate a 2D matrix module
'''


def rotate_2d_matrix(matrix):
    '''
    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty
    '''
    matrix[:] = list(map(list, zip(*matrix)))
    for row in matrix:
        row.reverse()
