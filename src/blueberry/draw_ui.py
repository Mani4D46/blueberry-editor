"""
Here you will find the functions used to draw diffrent parts of the UI.
"""

from . import focus

from .terminal import ansi_codes
from .terminal import drawings
from . import configs


def draw_menus(self) -> None:
    """
    Draws the menu part of the screen.
    """
    menu_texts = [menu_.name for menu_ in self.menus]
    self.write(ansi_codes.move_cursor(0, 0))
    self.write(drawings.draw_bar(
        start="",
        options=menu_texts,
        selected_item=self.menu_state.selected,
        color=configs.colors['menu'],
        selected_color=configs.colors['menu.selected'],
        width=self.app_state.size.columns
    ))

    if self.currently_focused == focus.MENU:
        self.write(drawings.draw_list(
            location=(1, 0),
            options=[
                i.name for i in self.menus[self.menu_state.selected]
                .submenus
            ],
            selected_item=self.menu_state.submenu_selected,
            color=configs.colors['menu.open'],
            selected_color=configs.colors['menu.open.selected'],
            padding=configs.stylings['menu.width_padding'],
            width=16,
            height=self.app_state.size.lines
        ))
