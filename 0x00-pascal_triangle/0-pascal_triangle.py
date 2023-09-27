#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    lista = []
    for i in range(n):
        listb = []
        for j in range(i+1):
            if j == 0 or j == i:
                listb.append(1)
            else:
                m_value = lista[i-1][j] + lista[i-1][j-1]
                listb.append(m_value)
        lista.append(listb)
    return lista
