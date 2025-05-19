# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import src.utils.random_generator as randgen

class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
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