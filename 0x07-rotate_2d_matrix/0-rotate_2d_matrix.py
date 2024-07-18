#!/usr/bin/python

"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix 90 degrees clockwise.
    
    The matrix is modified in place.
    
    Args:
        matrix (List[List[int]]): The 2D matrix to rotate.
    """

    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            (matrix[i][j], matrix[j][i]) = (matrix[j][i], matrix[i][j])

    for i in range(n):
        matrix[i].reverse()
