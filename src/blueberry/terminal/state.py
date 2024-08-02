"""
Here you will find the :obj:`States` class.
"""


# TODO: Add a predefined set of valid state names for better auto-suggestion

class State():
    """
    State of everything should be defined in this class.

    Example:
        >>> some_state = State(visibility=True)
        >>> some_state.visibility
        True
    """
    def __init__(self, **state) -> None:
        for key, value in state.items():
            setattr(self, key, value)

print()