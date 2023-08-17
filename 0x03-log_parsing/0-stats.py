#!/usr/bin/python3
"""Log parsing"""


import sys
import re
import signal


def print_statistics(total_size, status_counts):
    """Prints the statistics"""
    print("Total file size: {}".format(total_size))
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))


log_pattern = re.compile(
        r"([0-9]+(?:\.[0-9]+){3}) - \[([^\]]+)\] \"GET \/projects\/260 HTTP\/1\.1\" ([0-9]+) ([0-9]+)")

total_size = 0
status_counts = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }
line_counter = 0


def interrupt_handler(signum, frame):
    """Handles KeyboardInterrupt and prints statistics before exiting."""
    print_statistics(total_size, status_counts)
    sys.exit(0)


signal.signal(signal.SIGINT, interrupt_handler)

try:
    for line in sys.stdin:
        match = re.match(log_pattern, line.strip())
        if match:
            _, _, status, size = match.groups()
            total_size += int(size)
            if status in status_counts:
                status_counts[status] += 1
            line_counter += 1
            if line_counter == 10:
                print_statistics(total_size, status_counts)
                line_counter = 0
except KeyboardInterrupt:
    print_statistics(total_size, status_counts)
    sys.exit(0)
