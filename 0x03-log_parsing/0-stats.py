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

try:
    """
    read stdin line by line and split on space
    if length of line > 8/not the format, skip the line and move
    to the next line
    """
    for line in sys.stdin:
        line_parts = line.split()

        if len(line_parts) < 8:
            continue
        f_size = int(line_parts[-1])
        status_code = int(line_parts[-2])

        """
        compute file size and capture status codes count
        """
        total_size += f_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        """
        print line count after every 10 lines and sorted in
        ascending order
        """
        if line_count % 10 == 0:
            print("File size: ", total_size)

            for s_code in sorted(status_codes.keys()):
                if status_codes[s_code] > 0:
                    print(f"{s_code}: {status_codes[s_code]}")

except KeyboardInterrupt:
    print("File size: ", total_size)
    for s_code in sorted(status_codes.keys()):
        print(f"{s_code}: {status_codes[s_code]}")
