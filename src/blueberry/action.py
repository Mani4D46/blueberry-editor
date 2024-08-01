"""
Here you will find the :obj:`Action` class.
"""
from collections.abc import Iterable

import attr


@attr.define()
class Action:
    """
    class for all actions.

    Attributes:
        name (str)
    """
    name: str


def run_actions(self, actions: Iterable[Action] | Action) -> None:
    """
    Runs the given action(s).

    Args:
        actions (Iterable[Action] | Action): the action(s) to run.
    """
    if not isinstance(actions, Iterable):
        # if action is not iterable, make it an iterable.
        actions = (actions,)

    for action in actions:
        if action.name in self.actions:
            self.actions[action.name]()
        else:
            raise ValueError(f"No action found with name '{action}'")
