#!/usr/bin/python3
""" Minimum Operations to get n H characters """

def minOperations(n: int) -> int:
    """ Returns the fewest number of operations needed to result in exactly n H characters """
    if n < 2:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations