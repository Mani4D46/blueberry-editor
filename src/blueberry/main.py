"""
This file is the main app, it combines all the required parts, it does all the
drawings, updates, input stuff and etc.
"""
import os
import sys
import threading

from . import menu
from . import terminal
from . import configs
from . import draw_ui
from . import action
from . import focus
from . import movement

from .terminal import keys
from .terminal import ansi_codes

UNBINDABLE_KEYS = [keys.ENTER, keys.LEFT, keys.RIGHT, keys.UP, keys.DOWN]


class App():
    """
    The blueberry editor app.
    """
    def __init__(self) -> None:
        # tabs
        self.tabs = []

        # states
        self.menu_state = terminal.State(selected=0, submenu_selected=0)
        self.app_state = terminal.State(
            is_running=True,
            size=os.get_terminal_size()
        )
        # the value for `self.currently_focused` should be included in
        # `blueberry.focus.VALID_OPTIONS`
        self.currently_focused = focus.MENU

        # threading
        self.input_thread = threading.Thread(target=self.keyboard_input)
        self.update_thread = threading.Thread(target=self.update)

        # actions
        self.actions = {
            'exit': self.exit,
        }

    def __enter__(self) -> None:
        sys.stdout.write(ansi_codes.enable_alternative_screen_buffer())
        self.input_thread.start()
        self.update_thread.start()
        sys.stdout.write(ansi_codes.hide_cursor())

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.exit()

    def exit(self) -> None:
        """
        Exits from the app completely.
        """
        self.app_state.is_running = False
        sys.stdout.write(ansi_codes.disable_alternative_screen_buffer())
        sys.stdout.write(ansi_codes.show_cursor())

    def keyboard_input(self) -> None:
        """
        Thread to get keyboard input from the user.
        """
        while self.app_state.is_running:
            keypress = terminal.getkey()
            if keypress in UNBINDABLE_KEYS:
                self.move(keypress)
            elif keypress in configs.keybinds:
                action.run_actions(self, configs.keybinds[keypress])

    def move(self, key) -> None:
        """
        Movement control
        """
        if self.currently_focused == focus.MENU:
            if key == keys.LEFT:
                self.menu_state.selected = movement.move_left(
                    self.menu_state.selected,
                    min_value=0
                )
            if key == keys.RIGHT:
                self.menu_state.selected = movement.move_right(
                    self.menu_state.selected,
                    max_value=len(menu.menu_list) - 1
                )

    def update(self) -> None:
        """
        Thread to update the screen (stdout).
        """
        while self.app_state.is_running:
            # Do some updates here
            self.draw()
            sys.stdout.flush()

    def draw(self) -> None:
        """
        Writes everything on the screen before the flush.
        """
        draw_ui.draw_menus(self)
        # self.draw_tab()
        # self.draw_current_tab()
        # if self.state_command_palette.visibility is True:
        #     self.draw_command_palette()
