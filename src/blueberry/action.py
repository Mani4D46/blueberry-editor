"""
Here you will find the :obj:`Action` class.
"""
import attr


@attr.define()
class Action:
    """
    class for all actions.

    Attributes:
        name (str)
    """
    name: str
