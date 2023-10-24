#!/usr/bin/python3

"""
method that determines if a given data set
represents a valid UTF-8 encoding.
Return: True if data is a valid UTF-8
encoding, else return False
"""


def validUTF8(data):
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    num_bytes = 0

    for byte in data:
        byte_to_binary = format(byte, '08b')

        if num_bytes == 0:
            if byte_to_binary.startswith('110'):
                num_bytes = 1
            elif byte_to_binary.startswith('1110'):
                num_bytes = 2
            elif byte_to_binary.startswith('11110'):
                num_bytes = 3
            elif byte_to_binary.startswith('10'):
                return False
        else:
            if not byte_to_binary.startswith('10'):
                return False
            num_bytes -= 1

    if num_bytes != 0:
        return False
    return True
