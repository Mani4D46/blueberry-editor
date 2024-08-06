#! /usr/bin/env python3

"""
This program provides the ability to convert an image file to ANSI compatible
output for display in terminal sessions that support ANSI code.

#
This is a derivative of the improvements made by Takumi Sueda (puhitaku) on
image-to-ansi.py at https://gist.github.com/puhitaku/7eaf6142fa5a42425f55 which
provided significant (7x) speed improvements in turn is a derivative of the
work of Kevin Lange (klange) which was originally built on from Micah Elliott
(MicahElliott) a huge thank you to all these folks for the great foundational
work that I was able to slightly modify.

This version updates a variable to allow for a string variable (filename) to
be passed at run time from cli to the program. This simplifies execution by
allowing the user to run: python image-to-ansi.py <filename>

# Major Improvement List #
- direct passing of file variable to script
- basic error checking for existance of file
- basic error checking for single variable
- addition of help section explaining syntax
- general cleanup
- slight update and rework of the header format

-torrycrass
"""

__author__    = "Micah Elliott http://MicahElliott.com; Kevin Lange <k@dakko.us>"
__copyright__ = "Copyright (C) 2011 Micah Elliott.  All rights reserved."
__credits__ = ["Micah Elliott", "Kevin Lange", "Takumi Sueda", "Torry Crass"]

__license__   = "WTFPL http://sam.zoy.org/wtfpl/"
__version__   = "0.2"
__maintainer__ = "Torry Crass"
__email__ = "tc.github@outlook.com"
__status__ = "Development"

import sys
import os.path

if __name__ == '__main__':

    #Check that the user passed a single variable to the script
    if len(sys.argv) != 2:
        print("")
        print(30 * ">" , "ERROR" , 30 * "<")
        print("\nError: You must pass a single option to the program.")
        print("use --help or -h for syntax assistance.\n")
        print(67 * "^")
        print("")

    #Handle a help request
    elif str(sys.argv[1]) == "--help" or str(sys.argv[1]) == "-h":
        print("Use it like: python3 generate_ascii_art.py myfile.png")

    #Check that the variable provided is a valid file name on the system
    elif os.path.isfile(sys.argv[1]) is not True:
        print("")
        print(30 * ">" , "ERROR" , 30 * "<")
        print("\nError: This program requires an input file, the value provided\n" \
            "is not a file. Please use a valid file name.\n")
        print(67 * "^")
        print("")

    #If all other criteria are not met, process the file
    else:
        bp = [0, 0 ,0]
        FILE = str(sys.argv[1])

        #Process the image file
        from PIL import Image
        im = Image.open(FILE)
        x = im.size[0]
        im = list(im.getdata())
        s = []
        X_0 = False
        O_0 = False
        for i, p in enumerate(im):
            if len(p) > 3 and p[3] == 0:
                if X_0 is False:
                    s.append(f"\033[0m  ")
                    X_0 = True
                else:
                    s.append(f"  ")
            else:
                if bp != p:
                    s.append(f"\033[48;2;{p[0]};{p[1]};{p[2]}m  ")
                else:
                    s.append(f"  ")
                X_0 = False

            if (i+1) % x == 0:
                X_0 = False
                s.append("\033[0m\n")
            bp = p
        s.append("\n")
        sys.stdout.write(''.join(s) + '! ')
