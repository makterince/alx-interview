#!/usr/bin/python3
""" module computes a class and prints its metrics """


import sys
import datetime


class LogStats:
    """
        A class to compute and print metrics from log data.
    """

    def __init__(self):
        """
            Initialize the LogStats instance with initial metrics.
        """

        self.total_size = 0
        self.status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                             404: 0, 405: 0, 500: 0}
        self.line_count = 0

    def process_line(self, line):
        """
            Process a single log line and update the metrics.
            Args:
                line (str): The log line to process.
        """

        parts = line.split()
        if len(parts) < 7:
            return
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        self.total_size += file_size
        if status_code in self.status_codes:
            self.status_codes[status_code] += 1

        self.line_count += 1
        if self.line_count % 10 == 0:
            self.print_stats()

    def print_stats(self):
        """
            Print the current metrics.
        """

        print(f"File size: {self.total_size}")
        for code, count in sorted(self.status_codes.items()):
            if count > 0:
                print(f"{code}: {count}")
                print()


if __name__ == "__main__":
    stats = LogStats()
    try:
        for line in sys.stdin:
            stats.process_line(line.strip())
    except KeyboardInterrupt:
        stats.print_stats()
        sys.exit(0)
