# -*- coding: utf-8 -*-
import sys
import select
import os
import time
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import src.Utils.random_generator as randgen

from platform import system
if system() == 'Windows':
    from msvcrt import getwch as getch
    from msvcrt import kbhit
else:
    def getch():
        ch = sys.stdin.read(1)
        return ch

    def kbhit():
        results = select.select([sys.stdin], [], [], 0)
        return results[0] != []

class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    ORANGE = "\033[38;2;255;165;0m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def ctxt(text:str, color:Colors):
    """
    Wraps the text in the specified color.
    """
    return f"{color}"+text+f"{Colors.RESET}"

def dprint(text:str):
    """
    Prints the text for debug in orange
    """
    print(ctxt(text, Colors.YELLOW))

def color_text_from_rarity(name:str, rarity:randgen.Rarity):
    """
    Returns a colored name based on the rarity.
    """
    color = {
        randgen.Rarity.S: "\033[1;35m",  # Magenta
        randgen.Rarity.B: "\033[1;34m",  # Blue
        randgen.Rarity.C: "\033[1;32m",  # Green
        randgen.Rarity.A: "\033[1;33m",  # Yellow
        randgen.Rarity.D: "\033[1;31m",  # Red
    }
    return f"{color[rarity]}{name}\033[0m"

def color_from_rarity(rarity:randgen.Rarity):
    """
    Returns a color based on the rarity.
    """
    color = {
        randgen.Rarity.S: Colors.MAGENTA,
        randgen.Rarity.B: Colors.BLUE,
        randgen.Rarity.C: Colors.GREEN,
        randgen.Rarity.A: Colors.YELLOW,
        randgen.Rarity.D: Colors.RED,
    }
    return color[rarity]    

def timed_input(prompt, timeout=1):
    print(prompt, end='', flush=True)
    start_time = time.time()
    input_str = ''
    while True:
        if kbhit():
            # char = msvcrt.getwch()
            char = getch()
            if char == '\r':  # Enter key
                # print()
                return input_str
            elif char == '\b':  # Backspace
                input_str = input_str[:-1]
            else:
                input_str += char
            return input_str
        if time.time() - start_time > timeout:
            # print()  # Move to next line
            return None

def strip_ansi(s: str) -> str:
    """Return the string with ANSI escape sequences removed (for width calculation)."""
    return re.sub(r'\x1b\[[0-9;]*m', '', s)

def center_ansi(s: str, width: int) -> str:
    """
    Center a possibly-colored string according to its visible length.
    Preserves ANSI escapes.
    """
    visible = strip_ansi(s)
    if len(visible) >= width:
        if len(visible) > width:
            parts = re.split(visible, s)
            s = parts[0] + visible[:width] + parts[1]
        return s

    pad_total = width - len(visible)
    left = pad_total // 2
    right = pad_total - left
    return ' ' * left + s + ' ' * right
    
def fside(text, side:str='right', width:int=80):
    """
    format a string of 'width' character push the visible text to the 'side'
    """
    visible = strip_ansi(text)

    if side == 'right':
        ftext = "{0:>{1}}".format(text, width+len(text)-len(visible))
    elif side == 'left':
        ftext = "{0:<{1}}".format(text, width)
    else :
        ftext = "{0:^{1}}".format(text, width+len(text)-len(visible))

    return ftext