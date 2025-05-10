import sys
import os
# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.utils.random_generator import Rarity

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

def color_from_rarity(name:str, rarity:Rarity):
    """
    Returns a colored name based on the rarity.
    """
    color = {
        Rarity.S: "\033[1;35m",  # Magenta
        Rarity.B: "\033[1;34m",  # Blue
        Rarity.C: "\033[1;32m",  # Green
        Rarity.A: "\033[1;33m",  # Yellow
        Rarity.D: "\033[1;31m",  # Red
    }
    return f"{color[rarity]}{name}\033[0m"