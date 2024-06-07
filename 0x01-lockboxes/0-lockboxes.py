#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    """lockboxes"""
    n = len(boxes)
    unlocked = set([0])
    keys = list(boxes[0])
    while keys:
        key = keys.pop()
        if key < n and key not in unlocked:
            unlocked.add(key)
            keys.extend(boxes[key])
    return len(unlocked) == n
