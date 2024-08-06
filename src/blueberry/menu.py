"""
Here you will find things related to menus.
"""

from collections.abc import Sequence

import attr

from . import focus
from . import configs

from .terminal import drawings


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
    name: str
    submenus: list | None = None
    action: str | None = None
    icon: str | None = None


menu_list = [
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


def draw_menu_list(self) -> None:
    """
    Draws the submenu part of the screen.
    """
    self.write(drawings.draw_list(
        location=(1, 0),
        options=[
            i.name for i in menu_list[self.menu_state.selected]
            .submenus
        ],
        selected_item=self.menu_state.submenu_selected,
        color=configs.colors['menu.open'],
        selected_color=configs.colors['menu.open.selected'],
        padding=configs.stylings['menu.width_padding'],
        width=16,
        height=self.terminal_lines
    ))


def draw_menus(self) -> None:
    """
    Draws the menu part of the screen.
    """
    menu_texts = [menu_.name for menu_ in menu_list]
    self.move_cursor(0, 0)
    self.write(drawings.draw_bar(
        start="",
        options=menu_texts,
        selected_item=self.menu_state.selected,
        color=configs.colors['menu'],
        selected_color=configs.colors['menu.selected'],
        width=self.terminal_columns
    ))

    current_menu = menu_list[self.menu_state.selected]

    has_submenus = isinstance(current_menu.submenus, Sequence)
    if self.currently_focused == focus.MENU and has_submenus:
        draw_menu_list(self)
