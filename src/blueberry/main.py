"""
This file is the main app, it combines all the required parts.
"""
import sys
import threading
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
        self.is_running = True

        # stdout
        self.write = sys.stdout.write
        self.flush = sys.stdout.flush

        # threading
        self.input_thread = threading.Thread(target=self.keyboard_input)
        self.update_thread = threading.Thread(target=self.update)

        # actions (for extension support)
        self.actions = {
            'exit': self.exit,
        }

    def __enter__(self):
        self.write(ansi_codes.enable_alternative_screen_buffer())
        self.input_thread.start()
        self.update_thread.start()

    def __exit__(self, exc_type, exc_value, traceback):
        self.exit()

    def exit(self):
        """
        Exits from the app completely.
        """
        self.is_running = False
        self.write(ansi_codes.disable_alternative_screen_buffer())

    def keyboard_input(self):
        """
        Thread to get keyboard input from the user.
        """
        while self.is_running:
            keypress = terminal.getkey()
            if keypress == 'q':
                self.exit()

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
        # self.draw_menus()
        # self.draw_tab()
        # self.draw_current_tab()
        # if self.state_command_palette.visibility is True:
        #     self.draw_command_palette()
