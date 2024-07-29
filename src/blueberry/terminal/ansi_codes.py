"""
Here you will find ansi escape sequences which are codes used to talk to the
terminal.

Each function returns the requested escape sequence in form of a string.
"""
import re


ESCAPE_REGEX = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')


def enable_alternative_screen_buffer() -> str:
    """
    Changes the terminal screen buffer to an empty one until the alternative
    screen buffer is disabled.

    Returns:
        str
    """
    return '\033[?1049h'


def disable_alternative_screen_buffer() -> str:
    """
    Restores the previous screen buffer.

    Returns:
        str
    """
    return '\033[?1049l'


def show_cursor() -> str:
    """
    Shows the blinking bar (the cursor).

    Returns:
        str
    """
    return '\033[?25h'


def hide_cursor() -> str:
    """
    Hides the blinking bar (the cursor).

    Returns:
        str
    """
    return '\033[?25l'


def move_cursor(row: int, column: int) -> str:
    """
    Moves cursor to given position.

    Args:
        row (int): row starting from 0
        column (int): column starting from 0

    Returns:
        str
    """
    return f'\033[{row + 1};{column + 1}H'
