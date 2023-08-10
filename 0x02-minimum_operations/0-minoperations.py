#!/usr/bin/python3
""" module calculates minumum number of operation needed """


def minOperations(n):
    """ Calculate the minimum number of operations
        needed to achieve n H characters in the file.
    """

    if n <= 1:
        return 0

    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        operations[i] = i  # Initialize with the maximum possible value

        for j in range(i - 1, 1, -1):
            if i % j == 0:
                operations[i] = operations[j] + (i // j)
                break
    return operations[n]
