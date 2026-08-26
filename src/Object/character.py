# -*- coding: utf-8 -*-
import sys
import os
import random
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.Utils.random_generator import random_rarity, Rarity
from src.Utils.display import color_from_rarity, color_text_from_rarity, ctxt, Colors, dprint
from src.Object.entity import Entity
from src.Object.item import Item
from src.Object.equipment import Equipment

import pickle as pkl
 
class Character(Entity):
    def __init__(self):
        super().__init__()
        self.name = "Character"
        self.uid  = 0               # between 1 and 10 Only
        self.inventory = []
        self.equipment = {'head': None, 'body': None, 'legs': None, 'feet': None, 'left hand': None, 'right hand': None, 'neck': None, 'ring1': None, 'ring2': None, 'belt': None}

    def generate(self, level=1, rarity=None):
        super().generate(level=level, rarity=rarity)
        return self
    
    def display_stats(self, cr:bool=True, life:bool=True, cst:bool=True, spd:bool=True, strg:bool=True, fcs:bool=True,
                      gold:bool=True, xp:bool=True, maxlife:bool=False):
        print(f"Deprecated method display_stats, use display_sheet instead.")
        stats = super().display_stats(cr=cr, life=life, cst=cst, spd=spd, strg=strg, fcs=fcs,gold=gold, xp=xp)
        # ADD Inventory Display
        stats += self.display_equipment(name_only=True)
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
        
    def display_equipment(self, name_only=False):
        """
        Display the character's equipment.
        """
        inv_str = "equipment:\n"
        if name_only:
            for i, item in enumerate(self.equipment):
                if self.equipment[item] is not None:
                    raise NotImplementedError("Display equipment not implemented yet.")
                else:
                    inv_str += f"{item:^12s} : {'Empty':^16s} | "
                    if item in ['feet', 'right hand', 'belt']:
                        inv_str += "\n"
        else:   
            raise NotImplementedError("Display equipment not implemented yet.")
        return inv_str

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
    
    def get_inventory_item_name(self, index):
        """
        Get the name of the item in the inventory at the given index.
        """
        if index < len(self.inventory):
            return self.inventory[index].displayed_name().strip()
        else:
            return 'Empty'

    def display_sheet(self, equipment=True, inventory=True, xp=True):
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

## Reworked until Here : Idea : Uniform Information display to only have Sheet style display ##
    def manage_inventory(self):
        """
        Manage the character's inventory.
        Allows droping, using and equipping items.
        """
        print("Inventory Management:\n")
        print(self.display_inventory())
        action = input("What would you like to do? (s: show item stats, d: drop, e: equipment, u: use, q: quit) ")

        if action.lower() == 's':
            print(self.display_inventory())

        elif action.lower() == 'd':
            item_index = int(input("\nEnter the index of the item you want to drop: "))
            if item_index < 0 or item_index >= len(self.inventory):
                print("Invalid index.")
                return
            item = self.inventory[item_index]
            self.remove_from_inventory(item)
            print(f"\n{item.displayed_name()} has been dropped from your inventory.")

        elif action.lower() == 'e':
            Equipment.equipment_mode(self)
        
        elif action.lower() == 'u':
            item_index = int(input("\nEnter the index of the item you want to use: "))
            if item_index < 0 or item_index >= len(self.inventory):
                print("Invalid index.")
                return
            item = self.inventory[item_index]
            if item.isusable() :
                self.use_item(item)
            else :
                print(f"This item can't be used")

        elif action.lower() == 'q':
            print("Exiting inventory management.")
            return
        self.manage_inventory()
        
    def add_to_inventory(self, item):
        if len(self.inventory) < 4:
            self.inventory.append(item)
            print(f"{item.displayed_name()} Added to your inventory")
            return True
        else:
            print("Inventory is full!\n")
            return False

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
            if isinstance(item, Item) : #or isinstance(item, Chest):
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
        return color_text_from_rarity(self.name, self.rarity)
    
    def life_status(self, add_name=True):
        """
        Returns a sentence relating the life status of the entity.
        """
        life_color = self.life_color()
        if add_name:
            name = self.displayed_name()
        else:
            name = ""
        if self.life <= 0:
            return f"{name} is dead!"
        elif self.life < self.maxlife*0.2:
            return f"{name} looks really bad! {ctxt(f'{self.life}', life_color)} hit point left!\n"
        elif self.life < self.maxlife*0.5:
            return f"{name} looks wounded! {ctxt(f'{self.life}', life_color)} hit point left!\n"
        else:
            return f"{name} looks to handle it! {ctxt(f'{self.life}', life_color)} hit point left!\n"
        
    def save(self):
        """
        Save the character's stats to a file.
        """
        action = input(f"Do you want to save the character {self.displayed_name()} {self.rarity.name} lvl:{self.level} ? (y/n): ")
        if action.lower() != 'y':
            print("Character not saved.")
            return
        # check if the save/characters.pkl file exists
        if not os.path.exists("save"):
            os.makedirs("save")
        if not os.path.exists("save/characters.pkl"):
            with open("save/characters.pkl", "wb") as f:
                pkl.dump({}, f)
        # load the existing characters
        with open("save/characters.pkl", "rb") as f:
            characters = pkl.load(f)

        # check if the character already exists by UID
        if self.uid < 1 and len(characters) < 10: # new character not loaded, it's a new one
            dprint(f"debug : {list(characters.keys())} - {1 in characters.keys()=}")
            for i in range(1, 11):
                if i not in characters.keys():
                    self.uid = i
                    dprint(f"choosen UID {i}")
                    break
            # Update local save
            
            print(f"Saving - {self.displayed_name()} {self.rarity.name} lvl: {self.level}\n")
            characters[self.uid] = self

        elif self.uid < 1 and len(characters) >= 10: # new character not loaded and save slot full
            action = input("Save slot are full. Do you want to delete an other character ? (y/n)")
            if action.lower() == 'y': 
                self.manage_save(delete_mode=True)
                self.save()
            else:
                print("Character not saved.")

        else: # character is a previous loaded one
            print(f"Character already exists :")
            print(f"old : {characters[self.uid].displayed_name()} {characters[self.uid].rarity.name} lvl: {characters[self.uid].level}")
            action = input(f"new : {self.displayed_name()} {self.rarity.name} lvl: {self.level}\nDo you want to overwrite it? (y/n): ")
            if action.lower() == 'y':
                # Update local save
                characters[self.uid] = self
                print("Character overwrited.")
            else:
                print("Character not saved.")
        
        with open("save/characters.pkl", "wb") as f:
            pkl.dump(characters, f) # Update save file
        return
                
    def delete_save_file(self, save_file="save/characters.pkl"):
        """
        Delete the character's save file.
        """
        if not os.path.exists("save"):
            print("Save directory does not exist.")
            return None
        if not os.path.exists(save_file):
            print("Characters save file does not exist.")
            return None
        
        # load the existing characters
        with open(save_file, "rb") as f:
            characters = pkl.load(f)
        
        if self.uid in characters:
            character_name = characters[character_uid].displayed_name()
            del characters[self.uid]
            with open(save_file, "wb") as f:
                pkl.dump(characters, f)
            print(f"Character {character_name} deleted.")
        else:
            print(f"Character {self.displayed_name()} not found in save file.")

    @staticmethod
    def manage_save(save_file="save/characters.pkl", delete_mode=False):
        """
        manage_save character's from a file.
        """
        if not os.path.exists("save"):
            print("Save directory does not exist.")
            return None
        if not os.path.exists(save_file):
            print("Characters save file does not exist.")
            return None
        
        # load the existing characters
        with open(save_file, "rb") as f:
            characters = pkl.load(f)

        if len(characters) > 0:
            action = (f"{len(characters)} characters found. Do you want to load or manage the saves (m) OR start with a new character (n): ")
            action = input(action) if not delete_mode else 'm'

            if action.lower() == 'm':
                while True:
                    for i, (uid, character) in enumerate(characters.items()):
                        print(f"{i} - {character.displayed_name()} {character.rarity.name} lvl: {character.level}")
                    
                    action = input("Do you want to load a character (l), delete one (d) or start with a new other one (n)? ") if not delete_mode else 'd'

                    if action.lower() == 'd':
                        index = int(input("Enter the index of the character you want to delete: "))
                        if 0 <= index < len(characters):
                            character_uid = list(characters.keys())[index]
                            character_name = characters[character_uid].displayed_name()
                            del characters[character_uid]
                            with open(save_file, "wb") as f:
                                pkl.dump(characters, f)
                            with open(save_file, "rb") as f:
                                characters = pkl.load(f)
                            print(f"Character {character_name} deleted.")
                        else:
                            print("Invalid index. No character deleted.")
                        if delete_mode:
                            return None

                    elif action.lower() == 'l':
                        action = input("Enter the index of the character you want to load: ")
                        try:
                            index = int(action)
                            if 0 <= index < len(characters):
                                # LOAD Character
                                character_uid = list(characters.keys())[index]
                                character_name = characters[character_uid].displayed_name()
                                print(f"Loading character: {character_name}")

                                print(f"{characters[character_uid]} - {characters[character_uid].uid=}")
                                return characters[character_uid]
                            else:
                                print("Invalid index. No character loaded.")
                        except ValueError:
                            print("Invalid input. No character loaded.")
                        return None
                    
                    else:
                        return None     

                    if len(characters) <= 0:  
                        print("No more characters to load.\n")
                        return None
            else:
                return None
            
        else:
            print("No character save found.")

        return None

if __name__ == "__main__":
    print("Basic Character Test")
    character = Character()
    print(character.display_stats())
    print("Random Character Test")
    rcharacter = Character().generate()
    print(rcharacter.display_stats())
    print("Character Sheet Test")
    print(character.display_sheet())