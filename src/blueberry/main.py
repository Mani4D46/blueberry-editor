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

from .terminal import ansi_codes


class App():
    """
    The blueberry editor app.
    """
    def __init__(self) -> None:
        # tabs
        self.tabs = []

        # menus
        self.menus = menu.default_menus

        # states
        self.menu_state = terminal.State(selected=0, submenu_selected=0)
        self.is_running = True
        # Should be included in `blueberry.focus.VALID_OPTIONS`
        self.currently_focused = 'menu'

        # stdout
        self.write = sys.stdout.write
        self.flush = sys.stdout.flush

        # terminal info
        self.columns, self.lines = os.get_terminal_size()

        # threading
        self.input_thread = threading.Thread(target=self.keyboard_input)
        self.update_thread = threading.Thread(target=self.update)

        # actions
        self.actions = {
            'exit': self.exit,
        }

    def __enter__(self) -> None:
        self.write(ansi_codes.enable_alternative_screen_buffer())
        self.input_thread.start()
        self.update_thread.start()
        self.write(ansi_codes.hide_cursor())

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.exit()

    def exit(self) -> None:
        """
        Exits from the app completely.
        """
        self.is_running = False
        self.write(ansi_codes.disable_alternative_screen_buffer())
        self.write(ansi_codes.show_cursor())

    def keyboard_input(self) -> None:
        """
        Thread to get keyboard input from the user.
        """
        while self.is_running:
            keypress = terminal.getkey()
            if keypress in configs.keybinds:
                action.run_actions(self, configs.keybinds[keypress])

    def update(self) -> None:
        """
        Thread to update the screen (stdout).
        """
        while self.is_running:
            # Do some updates here
            self.draw()
            self.flush()

    def draw(self) -> None:
        """
        Writes everything on the screen before the flush.
        """
        draw_ui.draw_menus(self)
        # self.draw_tab()
        # self.draw_current_tab()
        # if self.state_command_palette.visibility is True:
        #     self.draw_command_palette()
