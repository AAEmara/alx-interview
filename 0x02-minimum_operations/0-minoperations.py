#!/usr/bin/python3
"""A module that defines `minOperations` function."""


def minOperations(n: int) -> int:
    """A function that calculates the min number of operations to return n*'H'.
    Args:
        n: The desired number of character repetition.
    Returns:
        The minimum number of operations to generate n*'H'.
    """
    numbers_list = prime_factorization(n)
    operations_count = calculate_operations(n, numbers_list)
    return (operations_count)


def prime_factorization(n: int):
    """Breaks down a given number into a product of prime numbers.
    Args:
        n: The number to be prime factorized.
    Returns:
        A list of numbers where its product returns the given number n.
    """
    factorizing = True
    nums_list = list()
    leftover = n
    mod_num = 2  # Initialized by 2 since other numbers are usless.

    # Checking on edge cases
    if n <= 0:
        nums_list = [0]
        factorizing = False
    elif n == 1:
        nums_list = [1]
        factorizing = False

    # Factorizing the number given and its leftovers.
    while factorizing:
        # Check if the number is divisible by a certain number.
        if not (leftover % mod_num):
            nums_list.append(mod_num)
            leftover = leftover / mod_num
            continue  # To check if may be divisible again or not.
        mod_num += 1

        # It cannot be prime factorized any more.
        if leftover == 1:
            factorizing = False

    return (nums_list)


def calculate_operations(n: int, nums_list) -> int:
    """Calculate the number of operations required to generate n*'H'.
    Args:
        n: The number of characters to reach.
        nums_list: The numbers list resulted from prime factorization .
    Returns:
        The number of opertaions done to generate n*'H'.
    """
    buffer_count = 0
    text_count = 1
    operations_count = 0
    threshold = 1

    for number in nums_list:
        threshold *= number
        while text_count < threshold:
            if buffer_count == 0:
                buffer_count = text_count  # Copied.
                operations_count += 1  # Copy Operation.
            text_count += buffer_count  # Pasted.
            operations_count += 1  # Paste Operation.
        if text_count == threshold and text_count < n:
            buffer_count = text_count  # Copied.
            operations_count += 1  # Copy Operation.

    # Returning the number of operations done.
    return (operations_count)
