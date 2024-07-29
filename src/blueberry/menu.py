"""
Here you will find the menus.
"""
import attr


@attr.define()
class Menu():
    """
    Baseclass for all menus.

    Attributes:
        text (str)
        submenus (List[Menu] | None): sub-menus that will open when the menu
            is selected.
        action (str | None): action to execute when menu is selected.
        icon: (str | None)
    """
    text: str
    submenus: list | None
    action: str | None
    icon: str | None
