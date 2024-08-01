# Terminal Tag Assignment Sequence
**T**erminal **T**ag **A**ssi**g**nment or `tTAG` for short is a way of marking certain parts of a text to a sepecific "tag" which then can be used to search for that part of the text or more customize that sepecific part of text on the terminal.

## Syntax
### Terms:
- START: `ESC _ t`
- END: `ESC ?`
- TAG: any name containing only "[a-z]" and "_"

### Syntax:
```
START
TAG ("," TAG)* | "!!" | "/" | "!" TAG
(":")
END
```
- Anything in parenthesis means it's optional.
- The pipe character (|) is the seperator of diffrent options. One of them should be chosen.
- The asterisk (*) means the code could be repeated.
- The qoute ("") means something is a character, and should be exactly the same as written inside the qoutes. The qoute itself should be ignore in code.

### Actions

Action of terms and characters mentioned:
- `START`: marks the beggining.
- `/`: ends the previous tag.
- `!`: ends all tags with the sepecified name.
- `!!`: ends all tags.
- `TAG`: the tag name(s).
- `,`: used to seperate tags.
- `:`: marks tag is going to apply for the entire line.
- `END`: marks the ends.

