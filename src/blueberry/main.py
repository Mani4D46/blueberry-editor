"""
This file is the main app, it combines all the required parts.
"""
import sys
from . import terminal
from .terminal import ansi_codes


class App():
    """
    The blueberry editor app.
    """
    def __init__(self):
        # tabs
        self.tabs = []
        self.current_tab = None

        # states
        self.state_command_palette = terminal.State(visibility=False)

        # stdout
        self.write = sys.stdout.write
        self.flush = sys.stdout.flush

    def __enter__(self):
        self.write(ansi_codes.enable_alternative_screen_buffer())

    def __exit__(self, exc_type, exc_value, traceback):
        self.write(ansi_codes.disable_alternative_screen_buffer())

    def update(self):
        # Do some updates here
        self.draw()
        self.flush()

    def draw(self):
        """
        Writes everything on the screen before the flush.
        """
        # self.draw_menus()
        # self.draw_tab()
        # self.draw_current_tab()
        # if self.state_command_palette.visibility is True:
        #     self.draw_command_palette()
