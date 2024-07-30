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
        selected_color: color of the selected option.
        options (:obj:`List` of :obj:`str`): list of all options.
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


def draw_list(location: list[int],
              color,
              selected_color,
              padding: int,
              options: list[str],
              selected_item: int | None,
              width: int,
              height: int) -> str:
    """
    Draws a list menu.

    Args:
        location (:obj:`List` of [:obj:`int, :obj:`int`])
        color: main colors.
        selected_color: color of the selected option.
        padding (int): amount of padding to add before and after an option
        options (:obj:`List` of :obj:`str`): list of all options.
        selected_item (int | None): index of the selected item.
        width (int): minimum width of this menu.
        height (int): height of this menu.

    Returns:
        str
    """
    component = ""

    required_width = len(max(options, key=len))
    if required_width > width:
        width = required_width

    option_count = len(options)
    if option_count < height:
        height = option_count

    for index in range(0, height):
        unused_width_space = (width - len(remove_ascii(options[index])))
        component += ansi_codes.move_cursor(*location)
        location[0] += 1
        option_with_padding = (
            ' ' * padding +
            options[index] + ' ' * unused_width_space
            + ' ' * padding
        )
        if index == selected_item:
            component += selected_color(option_with_padding)
        else:
            component += option_with_padding

    return color(component)
