# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import random
from src.Utils.random_generator import Rarity, random_rarity
from src.Object.item import Item
from src.Utils.display import ctxt, Colors, dprint

class Equipment(Item):
    def __init__(self):
        super().__init__()
        self.types = list(Slot_table.keys())

        self.constitution   = 0 # for defense
        self.strength       = 0 # for attack
        self.focus          = 0 # for critical hit
        self.speed          = 0
        self.life           = 0
        self.maxlife        = 0

        self.level          = 0
        self.maxlevel       = 25  
        
        self.equipable      = True
        self.usable         = False
        self.type           = None

    @staticmethod
    def generate_random_equipment(level:int = None, rarity:Rarity = None, type:str = None):
        """
        Generate a random Equipment.
        """
        eqpt = Equipment()
        
        type = type if type in eqpt.types else None
        type = type if type is not None else random.choice(eqpt.types)
        eqpt.type          = type
        
        eqpt.generate(level=level, rarity=rarity)

        return eqpt
    
    def generate(self, level:int = None, rarity:Rarity = None):
        """
        Generates a random equipment with a random rarity and stats.
        """
        if rarity is None: # Set rarity to random value
            self.rarity = random_rarity()
        else:
            self.rarity = rarity
        # Add credits upgrade from rarity
        rarity_credit = (self.rarity.value)*5

        if level is None: # Set level to random value
            self.level = random.randint(1, self.maxlevel)
        else:
            self.level = min(level, self.maxlevel)
        # Add credits upgrade from level

        rarity_credit = (self.rarity.value)*5
        total_credit = rarity_credit + self.level

        self.upgrade_stats(credit=total_credit, debug=False)
        self.name_generator()
        return self

    def equip(self, character):
        print(f"this {self.displayed_name()} must be equipped in {Slot_table[self.type]}\n")

        # check if slots are available
        available_slots = []
        used_slots      = []
        for slot in Slot_table[self.type]:
            if character.equipment[slot] is None:
                available_slots.append(slot)
            else:
                used_slots.append(slot)

        if len(available_slots) < 1 and len(used_slots) > 0:
            print(f"All the available slots are already occupied")
            print(f"Used slots : {used_slots}")

        elif len(available_slots) > 0:
            idx = 0
            if len(available_slots) > 1:
                for i, slot in enumerate(available_slots):
                    print(f"{i} - {slot}")
                idx = int(input(f"\nEnter the index of the slot you want to use: "))
                if idx < 0 or idx >= len(available_slots):
                        print("Invalid index.")
            
            slot = available_slots[idx]
            character.equipment[slot] = self
            self.add_attribute_to(character)
            character.remove_from_inventory(self)

        else:
            raise NotImplementedError

        return

    def unequip(self, character, slot):
        # check space in the inventory
        if character.add_to_inventory(self):
            self.remove_attribute_to(character)
            character.equipment[slot] = None
        return

    def add_attribute_to(self, character):

        character.constitution  += self.constitution
        character.strength      += self.strength
        character.focus         += self.focus
        character.speed         += self.speed
        character.maxlife       += self.maxlife

        print(f"\n{self.displayed_name()} has been equipped.")
        print(f"constitution    {self.constitution:+d} -> now -> {character.constitution}")
        print(f"strength        {self.strength:+d} -> now -> {character.strength}")
        print(f"focus           {self.focus:+d} -> now -> {character.focus}")
        print(f"speed           {self.speed:+d} -> now -> {character.speed}")
        print(f"maxlife         {self.maxlife:+d} -> now -> {character.maxlife}\n")

    def remove_attribute_to(self, character):

        character.constitution  -= self.constitution
        character.strength      -= self.strength
        character.focus         -= self.focus
        character.speed         -= self.speed
        character.maxlife       -= self.maxlife

        print(f"\n{self.name} has been unequipped.")
        print(f"constitution    -{self.constitution} -> now -> {character.constitution}")
        print(f"strength        -{self.strength} -> now -> {character.strength}")
        print(f"focus           -{self.focus} -> now -> {character.focus}")
        print(f"speed           -{self.speed} -> now -> {character.speed}")
        print(f"maxlife         -{self.maxlife} -> now -> {character.maxlife}\n")

    @staticmethod
    def equipment_mode(character):
        print(f"\n{character.displayed_name()} Equipment mode")
        while True:
            print(character.display_sheet())
            print(character.display_inventory())
            action = input("What would you like to do ? (e: equip, u: unequip, q: quit) ")

            if action.lower() == 'e':
                eqpmt_idx = int(input("\nEnter the index of the equipment you want to use: "))
                if eqpmt_idx < 0 or eqpmt_idx >= len(character.inventory):
                    print("Invalid index.")
                    pass
                equipment = character.inventory[eqpmt_idx]
                if equipment.equipable :
                    if equipment.level <= character.level:
                        equipment.equip(character)
                    else:
                        print(f"\nLevel too low for this equipment, you need to be level {equipment.level} to equip it !\n")

                    if len(character.inventory) < 1 :
                        break

                else :
                    print(f"This item can't be equipped")

            elif action.lower() == 'u':
                used_slots      = []
                for slot in character.equipment:
                    if character.equipment[slot] is not None:
                        used_slots.append(slot)

                if used_slots == []:
                    print("No equipment equipped")
                else:
                    for idx, slot in enumerate(used_slots):
                        print(f"{idx} - {slot} : {character.equipment[slot].displayed_name()}")
                    index = int(input("\nEnter the index of the equipment you want to remove: "))
                    if index < 0 or index >= len(used_slots):
                        print("Invalid index.")
                        continue
                    else:
                        character.equipment[used_slots[index]].unequip(character,used_slots[index])


            elif action.lower() == 'q':
                break
        
        return

    def name_generator(self):
        """
        Generate the name of the object depending of the Skills
        """
        name = self.type

        # seek for a max caracteristics : 
        stats = {1: "constitution", 2: "strength", 3: "focus", 4: "speed", 5: "maxlife"}
        max_stat_value = 0
        stats_list = []

        for key in stats.keys():

            value = getattr(self, stats[key])
            if stats[key] == 'maxlife':
                value = value/10

            if value > max_stat_value:
                max_stat_value = getattr(self, stats[key])
                stats_list = [stats[key]]

            elif value == max_stat_value:
                stats_list.append(stats[key])

        if len(stats_list) == 1:
            if stats_list[0] == 'maxlife':
                name += ' of Life'
            else:
                name += f" of {stats_list[0]}"
        elif len(stats_list) > 1:
            name = f"Balanced " + name
        self.name = name
        return


    def upgrade_stats(self, credit=0, randomize=True, debug=False):
        """
        Upgrade the entity's stats.
        Allows the entity to upgrade n stats randomly.
        """
        stats = {1: "constitution", 2: "strength", 3: "focus", 4: "speed", 5: "maxlife"}
        while credit > 0:
            if randomize:
                action = random.randint(1, 5)
                if debug:
                    print(f"{self.displayed_name()} randomly chose to upgrade {stats[action]}!")
            
            if action == 1:
                self.constitution += 1
            elif action == 2:
                self.strength += 1
            elif action == 3:
                self.focus += 1
            elif action == 4:
                self.speed += 1
            elif action == 5:
                self.maxlife    += 10
                self.life       += 10
            credit -= 1
            if debug:
                print(f"{self.displayed_name()} upgraded {stats[action]} to {getattr(self, stats[action])}!")
        self.cr = self.calculate_cr()
        if debug:
            print(f"{self.displayed_name()} CR is now {self.cr}!")
            print(self.display_stats(xp=True))

        # Get the price !
        all_stats_sum = self.maxlife/10 + self.rarity.value*5 + self.constitution + self.speed + self.strength + self.focus + self.level*4
        self.gold = random.randint(int(all_stats_sum * 0.4), int(all_stats_sum * 1.5))

Slot_table={
    "Helmet":       ["head"],
    "Chest plate":  ["body"],
    "Pant":         ["legs"],
    "Shoes":        ["feet"],
    "Gantlet":      ["left hand", "right hand"],
    "Neckless":     ["neck"],
    "Belt":         ["belt"],
    "Ring":         ["ring1", "ring2"],
    "Sword":        ["left hand", "right hand"],
    "Shield":       ["left hand", "right hand"]
    }
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