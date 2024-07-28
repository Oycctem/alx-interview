#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Fewest number of coins needed to meet total.
    @coins: List of coin values
    @total: Target amount
    Return: Minimum coins or -1 if not possible
    """
    if not isinstance(total, int) or not isinstance(coins, list):
        return -1
    if total <= 0:
        return 0

    lowest = [float('inf')] * (total + 1)
    lowest[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0 and lowest[i - coin] + 1 < lowest[i]:
                lowest[i] = lowest[i - coin] + 1

    return lowest[total] if lowest[total] != float('inf') else -1
