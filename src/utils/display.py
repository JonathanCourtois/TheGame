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

class display_sheet:
    """
      UNUSED FOR NOW
    A class to manage a matrix of display cell elements.
    """
    def __init__(self, rows:int=7, cols:int=7, cell_size:int=15):
        self.rows       = rows
        self.cols       = cols
        self.cell_size  = cell_size
        self.sheet      = [["" for _ in range(cols)] for _ in range(rows)]

    def display_cell_map(self):
        """
        Display the cell map of the sheet.
        """
        [[self.set_cell(row, col, f"{row},{col}", prefix="[", suffix="]", color=Colors.RESET) for col in range(self.cols)] for row in range(self.rows)]
        self.display()
        self.clean_sheet()

    def clean_sheet(self):
        """
        Clean the sheet.
        """
        [[self.set_cell(row, col, f" ", prefix="", suffix="", color=Colors.RESET) for col in range(self.cols)] for row in range(self.rows)]

    def set_cell(self, row:int, col:int, value:str, prefix:str="", suffix:str="", color:Colors=Colors.RESET):
       """
       Set a cell in the sheet.
       """
       if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
           raise IndexError("Cell index out of range.")
       if len(value+prefix+suffix) > self.cell_size:
           raise ValueError("Value is too long for the cell.")
       self.sheet[row][col] = f"{prefix}{color}{value:^{self.cell_size-len(prefix)-len(suffix)}}{Colors.RESET}{suffix}"

    def display(self):
        """
        Display the entire sheet.
        """
        string = ""
        for row in range(self.rows):
            for col in range(self.cols):
                string += f"{self.sheet[row][col]}"
            string += "\n"
        print(string)   

if __name__ == "__main__":
    sheet = display_sheet()
    sheet.display_cell_map()
    sheet.display()