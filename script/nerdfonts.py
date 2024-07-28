"""
This script will generate a dict of all nerdfont icons.
"""
import requests

FILE_NAME = 'icons.py'

FILE_STRUCTURE = '''"""
Here you will find the nerdfonts icons that can be used.
"""

ICONS = {!HERE}
'''

URL = ('https://raw.githubusercontent.com/kovidgoyal/kitty/master/gen/'
       'nerd-fonts-glyphs.txt')


def split_parts(line: str) -> list[str]:
    """
    Split a glyph line to [codepoint, style, name].
    """
    splited_line = line.split(' ')
    if len(splited_line) > 2:
        return splited_line[0], splited_line[1], '_'.join(splited_line[2:])
    else:
        print(splited_line)


def filter_to_style(glyph) -> bool:
    """
    Returns a bool which is true only when the style of the glyph is `cod`.
    """
    if isinstance(glyph, tuple):
        return glyph[1] == 'cod'
    else:
        return False


def make_dict_like(glyph) -> list:
    """
    Makes the glyphs a dict item.
    """
    return f'    "\\u{glyph[0]}": "{glyph[2]}"'


glyphs = requests.get(URL, timeout=6).text.split('\n')
seperated_glyphs = map(split_parts, glyphs)
filtered_glyphs = filter(filter_to_style, tuple(seperated_glyphs))
filtered_glyphs_dict_like = ',\n'.join(map(make_dict_like, filtered_glyphs))


file_content = FILE_STRUCTURE.replace(
    '{!HERE}',
    '{\n' + filtered_glyphs_dict_like + '\n}'
)


with open(FILE_NAME, 'w', encoding='ascii') as file:
    file.write(file_content)
