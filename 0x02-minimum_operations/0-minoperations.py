#!/usr/bin/python3
"""
Finding minimum number of operations to obtain
`n` H characters using `Copy All` and `Paste` operations
"""


def minOperations(n):
    """
    Takes int n as input and returns int which reps
    number of min operations needed to achieve n H chars
    """
    if n < 2:
        return 0

    ops = 0
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
            ops += factor
        factor += 1

    if n > 1:
        ops += n
    return ops
