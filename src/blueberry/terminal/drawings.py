"""
Here you will find small components used for drawing stuff. useful
for consistancy.
"""
from . import ansi_codes


def remove_ascii(text: str) -> str:
    """
    Removes all ANSI escape sequences from a string.

    Args:
        text (str)

    Returns:
        str
    """
    return ansi_codes.ESCAPE_REGEX.sub('', text)


def draw_bar(start: str,
             color,
             selected_color,
             options: list[str],
             selected_item: int | None,
             width: int) -> str:
    """
    Draws a bar.

    Args:
        start (str): text at the beginning.
        color: main colors.
        selected_color: color of the selected option
        options (List[str]): list of all options.
        selected_item (int | None): index of the selected item.
        width (int): maximum width of this line.

    Returns:
        str
    """
    component = start
    for index, option in enumerate(options):
        if index == selected_item:
            component += selected_color(f' {option} ')
        else:
            component += f' {option} '
    # the following line adds whitespace to the end
    component += ' ' * (width - len(remove_ascii(component)))
    return color(component)
