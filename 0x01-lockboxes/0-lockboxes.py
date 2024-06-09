#!/usr/bin/python3
"""A module that defines canUnlockAll() function."""

import typing


def canUnlockAll(boxes: typing.Union[typing.List[typing.List], typing.List])\
        -> bool:
    """Returns True or False based on the ability of opening
    all of the lockboxes.

    Args:
        boxes: A list of lists or an internal list.

    Returns:
        True if all boxes can be opened,
        False if otherwise.
    """
    # Adding the keys inside the first box, since it is always unlocked.
    keys = {key for key in boxes[0] if key != 0}  # Available keys.
    locks = {lock for lock in range(1, len(boxes))}  # Locks to be unlocked.
    used_keys = {0}  # Initial key #0 used.

    while keys:
        key = keys.pop()
        if key > len(boxes) or key <= 0:
            continue
        used_keys.add(key)
        keys.update(new_key for new_key in boxes[key]
                    if new_key not in used_keys)
        # print(f"Locks before removing lock[{key}]")
        # print(f"The locks: {locks}")
        locks.remove(key)
        # print(f"Locks after removing lock[{key}]")
        # print(f"The locks: {locks}")

    if (len(locks)):
        return False
    return True
