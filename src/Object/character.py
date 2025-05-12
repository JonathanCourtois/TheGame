# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.utils.random_generator import random_rarity, Rarity
from src.utils.display import color_from_rarity, ctxt, Colors
from src.Object.Entity import Entity
 
class Character(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Character"
        self.inventory = []
        self.equipment = {'head': None, 'body': None, 'legs': None, 'feet': None, 'left hand': None, 'right hand': None, 'neck': None, 'ring1': None, 'ring2': None, 'belt': None}

    def generate_character(self, level=1, rarity=None):
        self.generate_entity(level=level, rarity=rarity)
        return self
    
    def display_stats(self, cr:bool=True, life:bool=True, cst:bool=True, spd:bool=True, strg:bool=True, fcs:bool=True,
                      gold:bool=True, xp:bool=True, maxlife:bool=False):
        stats = super().display_stats(cr=cr, life=life, cst=cst, spd=spd, strg=strg, fcs=fcs,gold=gold, xp=xp, maxlife=maxlife)
        # ADD Inventory Display
        stats += self.display_equipement(name_only=True)
        stats += self.display_inventory(name_only=True)
        return stats
        
    def display_inventory(self, name_only=False):
        """
        Display the character's inventory.
        """
        inv_str = "Inventory:\n"
        if len(self.inventory) == 0:
            inv_str = "Inventory is empty.\n"
            return inv_str
        if name_only:
            for i, item in enumerate(self.inventory):
                inv_str += f"ID : {i:2d} : {item.displayed_name():30} : lvl {item.level:2d} : {item.name}"
            inv_str += "\n"
        else:   
            for i, item in enumerate(self.inventory):
                 inv_str += f"ID : {i:2d}\n{item.display_stats()}"
        return inv_str
        
    def display_equipement(self, name_only=False):
        """
        Display the character's equipement.
        """
        inv_str = "Equipement:\n"
        if name_only:
            for i, item in enumerate(self.equipment):
                if self.equipment[item] is not None:
                    raise NotImplementedError("Display equipement not implemented yet.")
                else:
                    inv_str += f"{item:^12s} : {'Empty':^16s} | "
                    if item in ['feet', 'right hand', 'belt']:
                        inv_str += "\n"
        else:   
            raise NotImplementedError("Display equipement not implemented yet.")
        return inv_str

    def get_equipement_name(self, slot):
        """
        Get the name of the equipment in the given slot.
        """
        if slot in self.equipment:
            if self.equipment[slot] is not None:
                return self.equipment[slot].displayed_name()
            else:
                return "----"
        else:
            raise ValueError(f"Invalid equipment slot: {slot}, valid slots are {list(self.equipment.keys())}")
    
    def get_inventory_item_name(self, index):
        """
        Get the name of the item in the inventory at the given index.
        """
        if index < len(self.inventory):
            return self.inventory[index].displayed_name()
        else:
            return 'Empty'

    def display_character_sheet(self, equipement=True, inventory=True):
        """
        Display the character stats in a sheet format.
        format:
        # HEDER #
        # Stat 0 | equipment 0 #
        # Stat 1 | equipment 1 #
        # ...
        # Stat n | #
        # Inventory #
        """
        # HEADER
        Header = f"# Name : {color_from_rarity(f'{self.name:^20s}', self.rarity)} :"
        class_slot = f"Class {color_from_rarity(f'{self.rarity.name:1s}', self.rarity)}"
        Header += f"{class_slot:^21s}:{'#'*60}\n"

        sheet = f"{Header}# Level {'-'*21} :{self.level:^10d}:"
        eq_h = ''
        if equipement:
            eq_h = f"{' ':15s}⌈{' Head':^12s}⌉{' ':15s}"
            eq_h += f"⌈{' Neck':^12s}⌉ "

        sheet += f"{eq_h}#\n"
        sheet = f"{sheet}# CR {'-'*24} :{self.cr:^10d}:"
        if equipement:
            eq_h = f"{' ':15s}⌊{self.get_equipement_name('head'):^12s}⌋{' ':15s}"
            eq_h += f"⌊{self.get_equipement_name('neck'):^12s}⌋ "
        sheet += f"{eq_h}#\n"

        sheet = f"{sheet}# Life {'-'*22} :{ctxt(f'{self.life:>5d}',Colors.GREEN)}/{ctxt(f'{self.maxlife:<4d}',Colors.GREEN)}:"
        if equipement:
            eq_h = f" ⌈{'Left  Hand':^12s}⌉"
            eq_h += f"⌈{'Body':^12s}⌉"
            eq_h += f"⌈{'Right Hand':^12s}⌉ "
            eq_h += f"⌈{'Belt':^12s}⌉ "
        sheet += f"{eq_h}#\n"

        sheet += f"# Constitution {'-'*14} :{self.constitution:^10d}:"
        if equipement:
            eq_h = f" ⌊{self.get_equipement_name('left hand'):^12s}⌋"
            eq_h += f"⌊{self.get_equipement_name('body'):^12s}⌋"
            eq_h += f"⌊{self.get_equipement_name('right hand'):^12s}⌋ "
            eq_h += f"⌊{self.get_equipement_name('belt'):^12s}⌋ "
        sheet += f"{eq_h}#\n"

        sheet += f"# Speed {'-'*21} :{self.speed:^10d}:"
        if equipement:
            eq_h = f"{' ':15s}⌈{'Legs':^12s}⌉{' ':15s}"
            eq_h += f"⌈{'Ring 1':^12s}⌉ "
        sheet += f"{eq_h}#\n"

        sheet += f"# Strength {'-'*18} :{self.strength:^10d}:"
        if equipement:
            eq_h = f"{' ':15s}⌊{self.get_equipement_name('legs'):^12s}⌋{' ':15s}"
            eq_h += f"⌊{self.get_equipement_name('ring1'):^12s}⌋ "
        sheet += f"{eq_h}#\n"

        sheet += f"# Focus {'-'*21} :{self.focus:^10d}:"
        if equipement:
            eq_h = f"{' ':15s}⌈{'Feet':^12s}⌉{' ':15s}"
            eq_h += f"⌈{'Ring 2':^12s}⌉ "
        sheet += f"{eq_h}#\n"

        sheet += f"# Gold {'-'*22} :{ctxt(f'{self.gold:^10d}',Colors.YELLOW)}:"
        if equipement:
            eq_h = f"{' ':15s}⌊{self.get_equipement_name('feet'):^12s}⌋{' ':15s}"
            eq_h += f"⌊{self.get_equipement_name('ring2'):^12s}⌋ "
        sheet += f"{eq_h}#\n"

        sheet += f"# XP {'-'*24} :{ctxt(f'{self.xp:^10d}',Colors.CYAN)}:{' '*59}#\n"

        if inventory:
            sheet += f"# Inventory : {'-'*86} #\n"
            # We assume there is only 4 slots for now
            if len(self.inventory) >4:
                raise NotImplementedError("Iventory with more than 4 slots not implemented yet.")
            inventory = "#  "
            for i in range(4):
                inventory += f"[{self.get_inventory_item_name(i):^21s}] "
            inventory += f"{' '*(101-len(inventory))}#\n"
            sheet += f"{inventory}"
        sheet += f"{'#'*102}\n"

        return sheet

## Reworked until Here : Idea : Uniform Information display to only have Sheet style display ##
    def manage_inventory(self):
        """
        Manage the character's inventory.
        Allows droping, using and equipping items.
        """
        print("Inventory Management:\n")
        self.display_inventory_name_only()
        action = input("What would you like to do? (s: show item stats, d: drop, e: equip, u: use, x: unequip, q: quit) ")

        if action.lower() == 's':
            self.display_inventory()

        elif action.lower() == 'd':
            item_index = int(input("\nEnter the index of the item you want to drop: "))
            if item_index < 0 or item_index >= len(self.inventory):
                print("Invalid index.")
                return
            item = self.inventory[item_index]
            self.remove_from_inventory(item)
            print(f"\n{item.displayed_name()} has been dropped from your inventory.")

        elif action.lower() == 'e':
            print("Not implemented yet.")
        
        elif action.lower() == 'u':
            item_index = int(input("\nEnter the index of the item you want to use: "))
            if item_index < 0 or item_index >= len(self.inventory):
                print("Invalid index.")
                return
            item = self.inventory[item_index]
            self.use_item(item)

        elif action.lower() == 'x':
            print("Not implemented yet.")

        elif action.lower() == 'q':
            print("Exiting inventory management.")
            return
        self.manage_inventory()
        
    def add_to_inventory(self, item):
        if len(self.inventory) < 4:
            self.inventory.append(item)
        else:
            print("Inventory is full!\n")

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print("Item not found in inventory!")

    def use_item(self, item):
        """
        Use an item from the inventory.
        """
        if item in self.inventory:
            if isinstance(item, Item) or isinstance(item, Chest):
                if item.level > self.level:
                    print(f"{item.displayed_name()} is too high level for you!\n")
                else:
                    item.use_item(self)
            else:
                print("Item is not usable.\n")
        else:
            print("Item not found in inventory!\n")

    def displayed_name(self):
        """
        Returns the name of the character.
        """
        return color_from_rarity(self.name, self.rarity)
    
    def save(self):
        """
        Save the character's stats to a file.
        """
        save_data = {
            "name": self.name,
            "strength": self.strength,
            "speed": self.speed,
            "life": self.life,
            "maxlife": self.maxlife,
            "rarity": self.name,
            "inventory": [item.save() for item in self.inventory],
            "equipment": [item.save() for item in self.equipment],
            "gold": self.gold,
            "xp": self.xp,
            "level": self.level
        }
        return str(save_data)
    
    @staticmethod
    def load(save_data):
        """
        Load the character's stats from a file.
        """
        save_data = eval(save_data)
        rarity = Rarity[save_data["rarity"]]
        character = Character(save_data["strength"], save_data["speed"], save_data["life"], rarity)
        character.rename(save_data["name"])
        character.maxlife = save_data["maxlife"]
        character.inventory = [Item.load(item) for item in save_data["inventory"]]
        character.equipment = save_data["equipment"]
        character.gold = save_data["gold"]
        character.xp = save_data["xp"]
        character.level = save_data["level"]
        character.cr = character.calculate_cr()
        return character

if __name__ == "__main__":
    print("Basic Character Test")
    character = Character()
    print(character.display_stats())
    print("Random Character Test")
    rcharacter = Character().generate_character()
    print(rcharacter.display_stats())
    print("Character Sheet Test")
    print(character.display_character_sheet())