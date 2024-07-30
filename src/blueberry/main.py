"""
This file is the main app, it combines all the required parts, it does all the
drawings, updates, input stuff and etc.
"""
import os
import sys
import threading

from collections.abc import Iterable

from . import menu
from . import terminal
from . import configs
from .terminal import ansi_codes
from .terminal import drawings
from .action import Action


class App():
    """
    The blueberry editor app.
    """
    def __init__(self):
        # tabs
        self.tabs = []

        # menus
        self.menus = menu.default_menus

        # states
        self.command_palette_state = terminal.State(visibility=False)
        self.menu_state = terminal.State(selected=0, is_focused=False)
        self.is_running = True

        # stdout
        self.write = sys.stdout.write
        self.flush = sys.stdout.flush

        # general info
        self.columns, self.lines = os.get_terminal_size()

        # threading
        self.input_thread = threading.Thread(target=self.keyboard_input)
        self.update_thread = threading.Thread(target=self.update)

        # actions
        self.actions = {
            'exit': self.exit,
        }

        # keybinds
        self.keybinds = configs.keybinds

        # colors
        self.colors = configs.colors

    def __enter__(self):
        self.write(ansi_codes.enable_alternative_screen_buffer())
        self.input_thread.start()
        self.update_thread.start()
        self.write(ansi_codes.hide_cursor())

    def __exit__(self, exc_type, exc_value, traceback):
        self.exit()

    def exit(self):
        """
        Exits from the app completely.
        """
        self.is_running = False
        self.write(ansi_codes.disable_alternative_screen_buffer())
        self.write(ansi_codes.show_cursor())

    def keyboard_input(self):
        """
        Thread to get keyboard input from the user.
        """
        while self.is_running:
            keypress = terminal.getkey()
            if keypress in self.keybinds:
                self.run_actions(self.keybinds[keypress])

    def update(self):
        """
        Thread to update the screen (stdout).
        """
        while self.is_running:
            # Do some updates here
            self.draw()
            self.flush()

    def draw(self):
        """
        Writes everything on the screen before the flush.
        """
        self.draw_menus()
        # self.draw_tab()
        # self.draw_current_tab()
        # if self.state_command_palette.visibility is True:
        #     self.draw_command_palette()

    def draw_menus(self):
        """
        Draws the menu part of the screen.
        """
        menu_texts = [menu_.text for menu_ in self.menus]
        self.write(ansi_codes.move_cursor(0, 0))
        self.write(drawings.draw_bar(
            start="",
            color=self.colors['menu'],
            selected_color=self.colors['menu.selected'],
            options=menu_texts,
            selected_item=self.menu_state.selected,
            width=self.columns
        ))

    def run_actions(self, actions: Iterable[Action] | Action):
        """
        Runs any action given.
        """
        if not isinstance(actions, Iterable):
            # if action is not iterable, make it an iterable
            actions = (actions,)
        for action in actions:
            if action.name in self.actions:
                self.actions[action.name]()
            else:
                raise ValueError(f"No action found with name '{action}'")
