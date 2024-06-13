#!/usr/bin/python3
""""""

def minOperations(n):
    """
    Returns the fewest number of operations to get n H characters.
    """
    if n < 2:
        return 0

    operations = 0
    min_operations = 2

    while n > 1:
        while n % min_operations == 0:
            operations += min_operations
            n //= min_operations
        min_operations += 1

    return operations