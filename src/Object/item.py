# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import random
from src.utils.random_generator import Rarity
from src.Object.Entity import Entity
from src.utils.display import ctxt, Colors

class Item(Entity):
    """
    A class representing an item in the game.
    Inherits from the Entity class.
    """
    def __init__(self):
        self.name = "Item"
        self.rarity         = Rarity.D

        self.constitution   = 0 # for defense
        self.strength       = 0 # for attack
        self.focus          = 0 # for critical hit
        self.speed          = 0
        self.life           = 0
        self.maxlife        = 0

        self.level          = 0
        self.maxlevel       = 20  
        
        self.cr             = 0
        self.gold           = 0 # it's the price for the item, not the gold you get from it
        self.xp             = 0
        
        self.gold_amount    = 0
        self.affect         = []
        self.chose          = []
    
    def display_sheet(self, equipement=False, inventory=False, xp=False):
        """
        Display the item stats in a sheet format.
        format:
        # HEADER #
        # Stat 0 | #
        # Stat 1 | #
        # ...
        # Stat n | #
        """
        sheet = super().display_sheet(equipement=equipement, inventory=inventory, xp=xp)
        return sheet
    
    def use_item(self, character):
        """
        Use the item.
        """
        # Check if it's healing potion
        if self.life > 0:
            character.heal(self.life)
            print(f"\n{self.displayed_name()} has been used! You gained {ctxt(f'{self.life}', Colors.GREEN)} health point!")
        # else it's stat potion
        if "chest" in self.name.lower():
            print(f"\n{self.displayed_name()} has been opened!")
        if self.gold_amount > 0:
            character.gold += self.gold_amount
            print(f"\nYou gained {ctxt(f'{self.gold_amount}', Colors.YELLOW)} gold!")
        if self.xp > 0:
            character.xp += self.xp
            print(f"\nYou gained {ctxt(f'{self.xp}', Colors.BLUE)} experience points!") 
        # Remove the item from the inventory
        character.remove_from_inventory(self)
        character.Check_level()
        print(f"")
    
    @staticmethod
    def generate_random_item(level:int = None, rarity:Rarity = None):
        """
        Generate a random item.
        """
        item = Item()
        name = random.choice(list(item_list.keys()))
        item.name = name
        item.affect = item_list[name]["affect"]
        item.chose  = item_list[name]["chose"]
        item.generate(level=level, rarity=rarity)
        return item
    
    def upgrade_stats(self, credit=0, randomize=False, debug=False):
        """
        Upgrade the stats of the item.
        """
        credit = 0 # unused parameter, can be used for future upgrades
        if len(self.chose) > 0:
            assert len(self.affect) == 0, "You can't have both affect and chose at the same time."
            self.affect = [random.choice(self.chose)]

        for stat in self.affect:
            if stat == "life":
                self.life = random.randint(self.rarity.value + self.level, self.rarity.value * 3 * self.level)
            elif stat == "gold":
                self.gold_amount = random.randint(self.rarity.value + self.level + 10, self.rarity.value * 30 * self.level)
                # print(f"Gold amount set to {self.gold_amount} for item {self.name}")
            elif stat == "xp":
                self.xp = random.randint(self.rarity.value + self.level*4, (3*self.level)**2)
                # print(f"XP set to {self.xp} for item {self.name}")

        # Get the price !
        all_stats_sum = self.life*10 + self.gold_amount + self.xp + self.level + self.rarity.value
        self.gold = random.randint(int(all_stats_sum * 0.4), int(all_stats_sum * 1.4))
        return

item_list = {
    "Healing Potion": {
        "affect": ["life"],
        "chose": [],
    },
    "Gold Chest": {
        "affect": ["gold"],
        "chose": [],
    },
    "XP Chest": {
        "affect": ["xp"],
        "chose": [],
    },
    "Mystery Chest": {
        "affect": [],
        "chose": ["gold", "xp"],
    },
    "Mastery Chest": {
        "affect": ["gold", "xp"],
        "chose": [],
    }

}

if __name__ == "__main__":
    item = Item()
    print(item.display_sheet())
    print(item.displayed_name())
    
    item = Item.generate_random_item()
    print(item.display_sheet())
    print(item.displayed_name())
    item = Item.generate_random_item()
    print(item.display_sheet())
    print(item.displayed_name())
    item = Item.generate_random_item()
    print(item.display_sheet())
    print(item.displayed_name())
    item = Item.generate_random_item()
    print(item.display_sheet())
    print(item.displayed_name())