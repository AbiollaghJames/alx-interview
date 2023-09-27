#!/usr/bin/python3
"""Rep of pascals triangle"""


def pascal_triangle(n):
    """pascals triangle"""

    if n <= 0:
        return []

    lista = []
    for i in range(n):
        listb = []
        for j in range(i+1):
            if j == 0 or j == i:
                listb.append(1)
            else:
                value = lista[i-1][j] + lista[i-1][j-1]
                listb.append(value)

        lista.append(listb)

    return lista
