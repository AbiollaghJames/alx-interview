#!/usr/bin/env python3
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
        """convert byte to binary"""
        byte_to_binary = format(byte, '08b')

        if num_bytes == 0:
            """new byte in the sequence"""
            if byte_to_binary.startswith('0'):
                """single byte char"""
                num_bytes = 0
            elif byte_to_binary.startswith('110'):
                """2-bytes char"""
                num_bytes = 1
            elif byte_to_binary.startswith('1110'):
                """3-bytes char"""
                num_bytes = 2
            elif byte_to_binary.startswith('11110'):
                """4-bytes char"""
                num_bytes = 3
            else:
                return False
        else:
            if not byte_to_binary.startswith('10'):
                """continuation byte"""
                return False
            num_bytes -= 1
        """complete bytes"""
    return num_bytes == 0
