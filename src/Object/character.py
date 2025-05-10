# -*- coding: utf-8 -*-

import src.utils.display as dsp
import src.utils.random_generator as randgen
import src.Object.Entity as Entity
 
class Character(Entity):
    def __init__(self, strength, speed, life, rarity):
        super().__init__(strength, speed, life)
        self.name = "Character"
        self.rarity = rarity
        self.inventory = []
        self.equipment = {}

    def display_stats(self, stats=""):
        name = Rarity.color_name_from_rarity(self.name, self.rarity)
        stats = f"Name:\t\t{name}\n"
        stats += f"Level:\t\t{self.level:3d}\n"
        stats += f"Rarity:\t\t  {self.rarity.name}\n"
        stats = super().display_stats(stats)
        stats += f"Gold:\t{ctxt(f'{self.gold:11d}',Colors.YELLOW)}\n"
        stats += f"XP:\t{ctxt(f'{self.xp:7d}',Colors.BLUE)}/{ctxt(f'{self.level*10:3d}',Colors.BLUE)}\n"
        return stats
        
    def display_inventory(self):
        """
        Display the character's inventory.
        """
        print("Inventory:")
        if len(self.inventory) == 0:
            print("Inventory is empty.\n")
            return
        for i, item in enumerate(self.inventory):
            print(f"ID : {i:2d}\n{item.display_stats()}")

    def display_inventory_name_only(self):
        """
        Display the character's inventory with names only.
        """
        print("Inventory:")
        if len(self.inventory) == 0:
            print("Inventory is empty.\n")
            return
        for i, item in enumerate(self.inventory):
            print(f"ID : {i:2d} : {item.displayed_name():30} : lvl {item.level:2d} : {item.rarity.name}")
        print("")


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
        return Rarity.color_name_from_rarity(self.name, self.rarity)
    
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
            "rarity": self.rarity.name,
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
        rarity = Rarity.Rarity[save_data["rarity"]]
        character = Character(save_data["strength"], save_data["speed"], save_data["life"], rarity)
        character.rename(save_data["name"])
        character.maxlife = save_data["maxlife"]
        character.inventory = [Item.load(item) for item in save_data["inventory"]]
        character.equipment = save_data["equipment"]
        character.gold = save_data["gold"]
        character.xp = save_data["xp"]
        character.level = save_data["level"]
        character.cr = character.calculate_cr()
        character.ca = 10
        return character
