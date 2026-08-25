# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import random
from src.Utils.random_generator import Rarity
from src.Object.item import Item
from src.Utils.display import ctxt, Colors, dprint

class Equipement(Item):
    def __init__(self):
        super().__init__()
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
        self.type           = None

    @staticmethod
    def generate_random_equipement(level:int = None, rarity:Rarity = None, type:str = None):
        """
        Generate a random equipement.
        """
        eqpt = Equipement()

        dprint(f"{type=}")
        type = type if type in eqpt.types else None
        type = type if type is not None else random.choice(eqpt.types)
        eqpt.type          = type
        dprint(f"debug type : {type}")
        
        eqpt.generate(level=level, rarity=rarity)

        # debug
        eqpt.name = type
        dprint(f"{eqpt.display_sheet()}")

        return eqpt


    # def create_name(self):


    # # deprecated
    # def equip(self, slot, item):
    #     if slot in self.types:
    #         self.types[slot] = item
    #         return f"Equipped {item} to {slot}."
    #     else:
    #         return "Invalid slot."

    # def unequip(self, slot):
    #     if slot in self.types and self.types[slot] is not None:
    #         item = self.types[slot]
    #         self.types[slot] = None
    #         return f"Unequipped {item} from {slot}."
    #     else:
    #         return "No item to unequip from this slot."

    # def get_equipment(self):
    #     return {slot: item for slot, item in self.types.items() if item is not None}