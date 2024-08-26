#!/usr/bin/python3
"""
Define solution to the Prime Game problem
"""


def primes(n):
    """
    Returns list of prime numbers
    """
    i = []
    j = [True] * (n + 1)
    for p in range(2, n + 1):
        if (j[p]):
            i.append(p)
            for i in range(p, n + 1, p):
                j[i] = False
    return i


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
