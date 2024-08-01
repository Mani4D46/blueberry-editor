from ascii_magic import AsciiArt

def art():
   art = AsciiArt.from_image('./../assets/blueberry.svg')
   art.to_terminal()

art()
