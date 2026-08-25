# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import random
from src.Utils.random_generator import Rarity
from src.Object.item import Item
from src.Utils.display import ctxt, Colors

class Equipement(Item):
    def __init__(self):
        self.types = [
            "Helmet", 
            "Chest plate",
            "Pant", 
            "Shoes",
            "Gantlet", 
            "Neckless",
            "Belt", 
            "Ring",
            "Sword", 
            "Shield"
            ]
        
        self.equipable      = True
        self.usable         = False

    @staticmethod
    def generate_random_equipement(level:int = None, rarity:Rarity = None, type:str = None):
        """
        Generate a random equipement.
        """
        eqpt = Equipement()

        if type is None:
            print(f"No type")
            type = random.choice(eqpt.types)
        else:
            if type in eqpt.types:
                print(f"valid type")
            else:
                print(f"Invalid type")

        print(f"debug type : {type}")




    
    def generate_random_item(level:int = None, rarity:Rarity = None):
        """
        Generate a random equipement.
        """
        return Equipement.generate_random_equipement(level=level, rarity=rarity, type=None)


    def create_name(self):


    # deprecated
    def equip(self, slot, item):
        if slot in self.types:
            self.types[slot] = item
            return f"Equipped {item} to {slot}."
        else:
            return "Invalid slot."

    def unequip(self, slot):
        if slot in self.types and self.types[slot] is not None:
            item = self.types[slot]
            self.types[slot] = None
            return f"Unequipped {item} from {slot}."
        else:
            return "No item to unequip from this slot."

    def get_equipment(self):
        return {slot: item for slot, item in self.types.items() if item is not None}