#!/usr/bin/python3

"""
Script that reads stdin line by line and compute metrics
After every 10mins of keyboard interrupt, print stats from
the beginning
"""

import sys


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0
s_code = 0


def to_print(status_codes, total_size):
    print(f"File size: {total_size}")
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print(f"{k}: {v}")


try:
    for line in sys.stdin:
        line_parts = line.split()
        line_parts = line_parts[::-1]

        if len(line_parts) > 2:
            line_count += 1

        if line_count <= 10:
            total_size += int(line_parts[0])
            s_code = line_parts[1]

            if (s_code in status_codes.keys()):
                status_codes[s_code] += 1

        if (line_count == 10):
            to_print(status_codes, total_size)
            line_count = 0

finally:
    to_print(status_codes, total_size)
