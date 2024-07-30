"""
Here you will find the functions used to draw diffrent parts of the screen.
"""

from . import focus

from .terminal import ansi_codes
from .terminal import drawings


def draw_menus(self):
    """
    Draws the menu part of the screen.
    """
    menu_texts = [menu_.name for menu_ in self.menus]
    self.write(ansi_codes.move_cursor(0, 0))
    self.write(drawings.draw_bar(
        start="",
        color=self.colors['menu'],
        selected_color=self.colors['menu.selected'],
        options=menu_texts,
        selected_item=self.menu_state.selected,
        width=self.columns
    ))

    if self.currently_focused == focus.MENU:
        self.write(drawings.draw_list(
            (1, 0),
            self.colors['menu.open'],
            self.colors['menu.open.selected'],
            self.stylings['menu.width_padding'],
            [
                i.name for i in self.menus[self.menu_state.selected]
                .submenus
            ],
            self.menu_state.submenu_selected,
            10,  # minimum is 1
            height=self.lines
        ))
