"""
Here you will find the functions used to draw diffrent parts of the UI.
"""

import sys
from collections.abc import Sequence

from . import focus
from . import menu
from . import configs

from .terminal import ansi_codes
from .terminal import drawings


def draw_menu_list(self) -> None:
    """
    Draws the submenu part of the screen.
    """
    sys.stdout.write(drawings.draw_list(
        location=(1, 0),
        options=[
            i.name for i in menu.menu_list[self.menu_state.selected]
            .submenus
        ],
        selected_item=self.menu_state.submenu_selected,
        color=configs.colors['menu.open'],
        selected_color=configs.colors['menu.open.selected'],
        padding=configs.stylings['menu.width_padding'],
        width=16,
        height=self.app_state.size.lines
    ))


def draw_menus(self) -> None:
    """
    Draws the menu part of the screen.
    """
    menu_texts = [menu_.name for menu_ in menu.menu_list]
    sys.stdout.write(ansi_codes.move_cursor(0, 0))
    sys.stdout.write(drawings.draw_bar(
        start="",
        options=menu_texts,
        selected_item=self.menu_state.selected,
        color=configs.colors['menu'],
        selected_color=configs.colors['menu.selected'],
        width=self.app_state.size.columns
    ))

    current_menu = menu.menu_list[self.menu_state.selected]

    has_submenus = isinstance(current_menu.submenus, Sequence)
    if self.currently_focused == focus.MENU and has_submenus:
        draw_menu_list(self)
