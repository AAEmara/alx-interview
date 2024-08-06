#!/usr/bin/env python3
"""A module that defines a function that represents the Pascal's triangle."""

from typing import List


def pascal_triangle(n: int) -> List:
    """Represents the Pacal's triangle of certain iterations.
    Args:
        n : The number of rows of the pascal's triangle.
    Returns:
        A list of the numbers in each row of Pascal's Triangle.
    """
    pascals_list = list()
    if n <= 0:
        return (pascals_list)
    for i in range(n):
        if i == 0:
            pascals_list.append([1])
            prev_list = pascals_list[-1]
        elif i == 1:
            pascals_list.append([1, 1])
            prev_list = pascals_list[-1]
        else:
            pascals_list.append(create_new_row(i, prev_list))
            prev_list = pascals_list[-1]
            continue
    return (pascals_list)

def create_new_row(n: int, prev_list: List) -> List:
    """Creates a new row based on the previous row list and its items.
    Args:
        n: The number of new row (starting from 1).
        prev_list: The list that represents the previous row to the newer one.
    Returns:
        The newly created row based on pascal's triangle method.
    """
    new_list = [1]
    for i in range(1, n):
        if (i <= (n - 1)):
            new_list.append(prev_list[i - 1] + prev_list[i])
    new_list.append(1)
    return (new_list)
