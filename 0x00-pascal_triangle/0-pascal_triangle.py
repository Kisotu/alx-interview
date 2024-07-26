#!/usr/bin/python3

"""This module contains a function that defines
the structure of a pascal triangle. """


def pascal_triangle(n):
    """
    Returns list of lists of integers representing the Pascal’s triangle of n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists of integers representing the Pascal’s triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # initialize triangle with 1

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
