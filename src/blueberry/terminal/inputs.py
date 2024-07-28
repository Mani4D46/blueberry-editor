"""
Inputs from the terminal.
"""
import sys
import platform
if platform.system() in {'Linux', 'Darwin'}:
    import tty
    import termios
    # comment the this 2 following lines for windows
else:
    raise NotImplementedError(
        f"OS '{platform.system()}' not supported."
        "for windows support change the 'inputs.py' as explained in the "
        "comments"
    )

# uncomment the following code for windows
# from msvcrt import getwch

# def getch():
#     """
#     Gets a single character from STDIO.
#     """
#     return getwch().encode('utf-8', 'replace').decode()


# comment the following function for windows
def getch() -> str:
    """
    Gets a single character from STDIO.

    Returns:
        str
    """
    file_no = sys.stdin.fileno()
    old = termios.tcgetattr(file_no)
    try:
        tty.setraw(file_no)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(file_no, termios.TCSADRAIN, old)


def getkey() -> str:
    """
    Gets a key from STDIO

    Returns:
        str
    """
    char1 = getch()
    if char1 not in '\x00\xe0':  # '\x00\xe0\x1b' for windows
        return char1

    char2 = getch()
    if char2 not in '\x5b':  # '\x5b\x4f' for windows
        if char1 == '\xe0':
            return '\x00' + char2
        return char1 + char2

    char3 = getch()
    if char3 not in '\x31\x32\x33\x35\x36':
        return char1 + char2 + char3

    char4 = getch()
    if char4 not in '\x30\x31\x33\x34\x35\x37\x38\x39':
        return char1 + char2 + char3 + char4

    char5 = getch()
    return char1 + char2 + char3 + char4 + char5
