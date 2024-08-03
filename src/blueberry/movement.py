"""
Here you will find everything related to movement.
"""


def move_right(value: int, max_value: int) -> int:
    """
    Adds the 1 to given value. The result should never exceed `max_value`.
    """
    if value < max_value:
        value += 1

    return value


def move_left(value: int, min_value: int) -> int:
    """
    Subtracts the given value by 1. The result should never exceed `min_value`.
    """
    if value > min_value:
        value -= 1

    return value
