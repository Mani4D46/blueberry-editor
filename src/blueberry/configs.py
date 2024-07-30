"""
Here you will find the cofiguration options of blueberry editor.

We use the yachalk module for colors.
"""
from yachalk import chalk
from .terminal import keys
from .action import Action

# You can change colors of the UI elements here:
colors = {
    "menu": chalk.bg_gray.white,
    "menu.selected": chalk.bg_blue.white
}

# You can choose the keybinds you prefer here:
keybinds = {
    keys.CTRL_Q: Action("exit")
}
