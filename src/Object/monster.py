import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.Utils.random_generator import random_rarity, Rarity, roll_d
import random
from src.Utils.display import color_from_rarity, color_text_from_rarity, ctxt, Colors, dprint, fside
from src.Object.entity import Entity
from src.Object.equipment import Equipment

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

    def display_sheet(self, equipment=False, inventory=False, xp=False):
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
        sheet = super().display_sheet(equipment=equipment, inventory=inventory, xp=xp)

        return sheet
    
    def displayed_name(self):
        """
        Returns the name of the character.
        """
        return color_text_from_rarity(self.name, self.rarity)
            
    # def display_equipment(self, name_only=False):
    #     """
    #     Display the monster's equipment.
    #     """
    #     inv_str = "equipment:\n"
    #     if name_only:
    #         for i, item in enumerate(self.equipment):
    #             if self.equipment[item] is not None:
    #                 raise NotImplementedError("Display equipment not implemented yet.")
    #             else:
    #                 inv_str += f"{item:^12s} : {'Empty':^16s} | "
    #                 if item in ['feet', 'right hand', 'belt']:
    #                     inv_str += "\n"
    #     else:   
    #         raise NotImplementedError("Display equipment not implemented yet.")
    #     return inv_str

    def get_equipment_name(self, slot):
        """
        Get the name of the equipment in the given slot.
        """
        if slot in self.equipment:
            if self.equipment[slot] is not None:
                return self.equipment[slot].displayed_name().strip()
            else:
                return "----"
        else:
            raise ValueError(f"Invalid equipment slot: {slot}, valid slots are {list(self.equipment.keys())}")
        
    def attack(self):
        """
        Roll attack stats.
        Returns a tuple of hit and damage.
        """
        life_bar = f"{'\u0190>'*int((self.life*(80-len(self.name))/self.maxlife)/2)} "
        c_life_bar = ctxt(life_bar, self.life_color())

        combat_log  = f"{fside(c_life_bar+self.displayed_name(), side='right')}\n"

        return super().attack(combat_log=combat_log, log_side='right')

    def defend(self, hit, damage, combat_log="", log_side: str = 'None'):
        """
        Roll the defence against an attack.
        If the hit is greater than the CA, reduce life by damage.
        """
        life_bar = f"{'\u0190>'*int((self.life*(80-len(self.name))/self.maxlife)/2)} "
        c_life_bar = ctxt(life_bar, self.life_color()) 
        
        combat_log += f"{fside(c_life_bar+self.displayed_name(), side='right')}\n"
        
        return  super().defend(hit, damage, combat_log=combat_log, log_side='right')
    
    def generate(self, level=None, rarity=None, name="Monster"):
        self.__init__()
        self.name = name
        super().generate(level=level, rarity=rarity)
        # Loot :
        # gold based on their level and statisctics
        all_stats_sum = (self.constitution + self.speed + self.strength + self.focus + self.maxlife/10 + self.level + self.rarity.value)
        self.gold = random.randint(self.level, int(all_stats_sum * 1.5))


        # Equipe item and or equipment:
        for slot in self.equipment.keys():
            if roll_d(100) <= 3 :
                eqpt = Equipment.generate_random_equipment(level=random.randint(1,self.level), rarity=None, type=slot)
                dprint(eqpt.display_sheet())
                eqpt.equip(self, random_choice=True)


        return self

    def generate_ranged(self, Character, range:int=1):
        charac_cr = Character.calculate_cr()
        self.generate(name=f"{self.name}")
        while self.cr > charac_cr + range or self.cr < charac_cr - 3:

            self.generate(name=f"{self.name}")
            dprint(f"Generated monster {self.name} with CR {self.cr} and Character CR {charac_cr} with range {range}")

        return self

monster_stat_list = {
    "Slime": {
        "strength": (0, 2),
        "speed": (0, 2),
        "life": (2, 10),
    },
    "Goblin": {
        "strength": (0, 3),
        "speed": (0, 3),
        "life": (10, 20),
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
