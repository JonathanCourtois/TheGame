# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import random
from src.Utils.random_generator import Rarity
from src.Object.item import Item
from src.Utils.display import ctxt, Colors, dprint

class Equipment(Item):
    def __init__(self):
        super().__init__()
        self.types = list(Slot_table.keys())

        self.equipable      = True
        self.usable         = False
        self.type           = None

    @staticmethod
    def generate_random_equipment(level:int = None, rarity:Rarity = None, type:str = None):
        """
        Generate a random Equipment.
        """
        eqpt = Equipment()

        dprint(f"{type=}")
        type = type if type in eqpt.types else None
        type = type if type is not None else random.choice(eqpt.types)
        eqpt.type          = type
        dprint(f"debug type : {type}")
        
        eqpt.generate(level=level, rarity=rarity)

        # debug
        eqpt.name = f"{type}"
        dprint(f"{eqpt.display_sheet()}")

        return eqpt

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
                        equipment.equip(character) # debug

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