"""
Here you will find the :obj:`States` class.
"""
import attr


@attr.define()
class Menu():
    """
    Baseclass for all menus.

    Attributes:
        text (str)
        submenus (:obj:`List` of :obj:`Menu` | None): sub-menus that will open
            when the menu is selected. defaults to None.
        action (str | None): action to run when menu is selected.
            defaults to None.
        icon: (str | None): defaults to None.
    """
    text: str
    submenus: list | None = None
    action: str | None = None
    icon: str | None = None


default_menus = [
    Menu('File', submenus=[
        Menu(
            'Exit',
            submenus=None,
            action='exit',
            icon='close'
        )
    ], action=None, icon=None),
    Menu('Edit', submenus=None, action=None, icon=None)
]
