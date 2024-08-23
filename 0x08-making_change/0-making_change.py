#!/usr/bin/python3
"""A module that defines a function that solves the making change problem."""


def makeChange(coins, total):
    """Finding the minimum number of coins used to make the total.
    Args:
        coins (list): A list of coins denomination.
        total (int): The total amount of coins to make change for it.
    Returns:
        The number of coins to be used.
    """
    if total <= 0:
        return 0

    current_total = 0
    used_coins = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total - current_total) // coin
        current_total += r * coin
        used_coins += r
        if current_total == total:
            return used_coins
    return -1
