#!/usr/bin/python3
"""
This module contains a function that
inserts a line of text to a file, after
each line containing a specific string
(see example):
"""


import sys
from collections import defaultdict

# Initialize variables
total_file_size = 0
status_code_counts = defaultdict(int)

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        _, _, _, status_code, file_size = line.split('"')[2].split()
        total_file_size += int(file_size)
        status_code_counts[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print("Total file size:", total_file_size)
            for code in sorted(status_code_counts.keys()):
                print(code + ":", status_code_counts[code])

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print("Total file size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        print(code + ":", status_code_counts[code])

