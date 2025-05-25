import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.utils.random_generator import random_rarity, Rarity
from src.utils.display import color_from_rarity, color_text_from_rarity, ctxt, Colors
from src.Object.Entity import Entity
import pickle as pkl

class Monster(Entity):
    """
    A class representing a monster in the game.
    Inherits from the Entity class.
    """
    def __init__(self):
        super().__init__()
        self.name = "Monster"
        self.inventory = []
        self.equipment = {'head': None, 'body': None, 'legs': None, 'feet': None, 'left hand': None, 'right hand': None, 'neck': None, 'ring1': None, 'ring2': None, 'belt': None}

    def display_stats(self, stats=""):
        print(f"Deprecated method display_stats, use display_sheet instead.")
        stats = f"Name:\t\t{self.name}\n"
        stats = super().display_stats(stats)
        return stats

    def display_sheet(self, equipement=False, inventory=False, xp=False):
        """
        Display the character stats in a sheet format.
        format:
        # HEADER #
        # Stat 0 | equipment 0 #
        # Stat 1 | equipment 1 #
        # ...
        # Stat n | #
        # Inventory #
        """
        sheet = super().display_sheet(equipement=equipement, inventory=inventory, xp=xp)

        return sheet
    
    def generate(self, level=None, rarity=None, name="Monster"):
        self.__init__()
        self.name = name
        super().generate(level=level, rarity=rarity)
        return self
    
# rework until here

    def generate_ranged(self, Character, range:int=2):
        charac_cr = Character.calculate_cr()
        self.generate(name=f"{self.name}")
        while self.cr > charac_cr + range:

            self.generate(name=f"{self.name}")
            # print(f"Generated monster {self.name} with CR {self.cr} and Character CR {charac_cr} with range {range}")

        return self

monster_stat_list = {
    "Goblin": {
        "strength": (0, 3),
        "speed": (0, 3),
        "life": (10, 20),
    },
    "Slime": {
        "strength": (0, 2),
        "speed": (0, 2),
        "life": (2, 10),
    },
    "Wolf": {
        "strength": (0, 3),
        "speed": (2, 5),
        "life": (15, 25),
    },
    "Bandit": {
        "strength": (2, 5),
        "speed": (2, 5),
        "life": (25, 40),
    }
}
