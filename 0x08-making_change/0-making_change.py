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

    # Sorting the coins in descending order.
    sorted_coins = sorted(coins, reverse=True)

    index_max = len(coins) - 1
    made_change = True
    coins_used = list()
    i = 0

    while (total > 0):
        if i > index_max:
            made_change = False  # Failure.
            break
        coin_tested = sorted_coins[i]  # Coin to be compared with total amount.
        if (total >= coin_tested):
            total = total - coin_tested
            coins_used.append(coin_tested)
            continue  # To check if the same coin could be used again.
        i += 1

    if not made_change:
        return (-1)  # Failed to make change for the total amount given.
    return (len(coins_used))  # Success.
