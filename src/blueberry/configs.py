"""
Here you will find the cofiguration options of blueberry editor.

We use the yachalk module for colors.
"""

from yachalk import chalk
from .terminal import keys
from .action import Action

# Config for coloring
menu_color = "#808080" # Hex please!
menu_selected = "#dbe9f4" # Hex please! 
menu_opened = "#d3d3d3" # Hex please!
menu_open_selected = "#dbe9f4" # Hex please!

# Config for styling
menu_width_padding = 1

# You can change colors of the UI components here:
colors = {
    "menu": chalk.hex(menu_color),
    "menu.selected": chalk.hex(menu_selected),
    "menu.open": chalk.hex(menu_opened),
    "menu.open.selected": chalk.hex(menu_open_selected)
}

# You can change the overall style of UI components here:
stylings = {
    "menu.width_padding": menu_width_padding
}

# You can choose the keybinds you prefer here:
keybinds = {
    keys.CTRL_Q: Action("exit")
}

CSI2J_CLEARING = False
