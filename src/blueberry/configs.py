"""
Here you will find the cofiguration options of blueberry editor.

We use the yachalk module for colors.
"""
from yachalk import chalk
from .terminal import keys
from .action import Action

# You can change colors of the UI components here:
colors = {
    "menu": chalk.bg_gray.white,
    "menu.selected": chalk.bg_blue.white,
    "menu.open": chalk.bg_gray.white,
    "menu.open.selected": chalk.bg_blue.white
}

# You can change the overall style of UI components here:
stylings = {
    "menu.width_padding": 1
}

# You can choose the keybinds you prefer here:
keybinds = {
    keys.CTRL_Q: Action("exit")
}

CSI2J_CLEARING = False
