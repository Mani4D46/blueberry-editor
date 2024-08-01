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
             options: list[str],
             selected_item: int | None,
             color,
             selected_color,
             width: int) -> str:
    """
    Draws a bar.

    Args:
        start (str): text at the beginning.
        options (:obj:`List` of :obj:`str`): list of all options.
        selected_item (int | None): index of the selected item.
        color: main color.
        selected_color: color of the selected option.
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
              options: list[str],
              selected_item: int | None,
              color,
              selected_color,
              padding: int,
              width: int,
              height: int) -> str:
    """
    Draws a list menu.

    Args:
        location (:obj:`List` of [:obj:`int, :obj:`int`])
        options (:obj:`List` of :obj:`str`): list of all options.
        selected_item (int | None): index of the selected item.
        color: main color.
        selected_color: color of the selected option.
        padding (int): amount of padding to add before and after an option
        width (int): minimum width of this menu.
        height (int): height of this menu.

    Returns:
        str
    """
    component = ""

    required_width = len(max(options, key=len))
    width = max(width, required_width)

    option_count = len(options)
    height = min(height, option_count)

    location = list(location)

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


def draw_line_numbers(current_line: int,
                      selected_line: int,
                      end: str,
                      color,
                      selected_color,
                      width: int = 6) -> str:
    """
    Draws a line number.

    Args:
        current_line (int): line number for the current line.
        selected_line (int): line number for the selected line.
        end (str): end of line number.
        color: main color.
        selected_color: color of the selected option.
        width (int): max width of this number.

    Returns:
        str
    """
    adjusted_line = (
        str(current_line).rjust(width - len(remove_ascii(end)), ' ')
    )
    if current_line == selected_line:
        component = selected_color(adjusted_line)
    else:
        component = adjusted_line

    component += end

    return color(component)
