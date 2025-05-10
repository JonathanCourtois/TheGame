import src.characters.rarity as Rarity
import random
from src.utils.display import ctxt, Colors
from src.utils.random_generator import stat_modifier, random_rarity

class Entity:
    def __init__(self, strength, speed, life):
        self.name = "Entity"
        self.strength   = strength
        self.speed      = speed
        self.life       = life
        self.maxlife    = life
        self.ca = 10
        self.cr = self.calculate_cr()
        ## bonus
        self.gold   = 0
        self.xp     = 0
        self.level  = 1

    def display_stats(self, stats=f"Name:\tEntity\n"):
        stats = f"{stats}CR:\t\t{self.cr:3d}\n"
        stats = f"{stats}Life:\t{ctxt(f'{self.life:7d}',Colors.GREEN)}/{ctxt(f'{self.maxlife:3d}',Colors.GREEN)}\n"
        stats = f"{stats}CA:\t\t {self.ca:2d}\n"
        stats = f"{stats}Speed:\t\t {self.speed:2d}\n"
        stats = f"{stats}Strength:\t {self.strength:2d}\n"
        return stats
    
    def calculate_cr(self):
        """
        Calculate the Challenge Rating (CR) of the entity.
        CR is calculated as the average of the strength, speed, and life.
        """
        return (self.strength + self.speed + self.life)
    
    def displayed_name(self):
        """
        Returns the name of the entity.
        """
        return self.name
    
    def attack(self):
        """
        Simulate an attack.
        Returns a tuple of hit and damage.
        """
        dice    = random.randint(1, 20)
        hit     = dice + self.strength
        if dice == 20:
            damage  = random.randint(1, 4) * 2 + self.strength 
            print(f"{self.displayed_name()} attacks with {ctxt('Crit!',Colors.RED)} Hit: {ctxt(f'{hit:2d}',Colors.YELLOW)}, Damage: {ctxt(f'{damage:2d}',Colors.YELLOW)}")
        else:
            damage  = random.randint(1, 4) + self.strength
            print(f"{self.displayed_name()} attacks with Hit: {ctxt(f'{hit:2d}',Colors.RED)}, Damage: {ctxt(f'{damage:2d}',Colors.RED)}")
        return hit, damage
    
    def defend(self, hit, damage):
        """
        Simulate defending against an attack.
        If the hit is greater than the CA, reduce life by damage.
        """
        if hit > self.ca+self.speed:
            self.life -= damage
            if self.life < self.maxlife*0.2:
                life_color = Colors.RED
            elif self.life < self.maxlife*0.5:
                life_color = Colors.YELLOW
            else:
                life_color = Colors.GREEN
            print(f"{self.displayed_name()} takes {ctxt(f'{damage:2d}',Colors.RED)} damage! Life left: {ctxt(f'{self.life:3d}',life_color)}/{ctxt(f'{self.maxlife:3d}',Colors.GREEN)}")
        else:
            print(f"{self.displayed_name()} dodges the attack!\n")

    def heal(self, amount):
        """
        Heal the entity by a certain amount.
        If the healed life exceeds max life, set it to max life.
        """
        self.life += amount
        if self.life > self.maxlife:
            self.life = self.maxlife
        print(f"{self.name} heals for {ctxt(f'{amount:2d}',Colors.GREEN)}! Life left: {ctxt(f'{self.life:3d}',Colors.GREEN)}/{ctxt(f'{self.maxlife:3d}',Colors.GREEN)}")

    def rename(self, name):
        """
        Rename the entity.
        """
        print(f"{self.name} has been renamed to {name}!")
        self.name = name
        
    def get_loot_from_monster(self, monster):
        """
        Simulate getting loot from a monster.
        Adds the monster's gold and XP to the entity.
        """
        self.gold   += monster.gold
        self.xp     += monster.xp
        print(f"{self.name} loots {ctxt(f'{monster.gold}',Colors.YELLOW)} gold and {ctxt(f'{monster.xp}',Colors.BLUE)} XP from {monster.name}!\n")
        if self.xp >= self.level * 10:
            self.xp -= self.level * 10
            self.level += 1
            print(f"{self.name} {ctxt('leveled up',Colors.MAGENTA)} and can upgrade 3 stats! New level: {ctxt(f'{self.level}',Colors.MAGENTA)}")
            self.upgrade_stats()
            self.heal(self.maxlife)
            self.cr = self.calculate_cr()
    
    def upgrade_stats(self, credit=3):
        """
        Upgrade the entity's stats.
        Allows the player to upgrade n stats.
        """
        while credit > 0:
            print(f"\nAvailable credits: {credit}\n")
            print(f"Current stats: Strength: {self.strength}, Speed: {self.speed}, MaxLife: {self.maxlife}\n")
            stat_to_upgrade = input("Which stat would you like to upgrade? (st:strength, sp:speed, l:life) ")
            if stat_to_upgrade == "st" or stat_to_upgrade == "strength":
                self.strength += 1
            elif stat_to_upgrade == "sp" or stat_to_upgrade == "speed":
                self.speed += 1
            elif stat_to_upgrade == "l" or stat_to_upgrade == "life":
                self.maxlife += 1
            else:
                print("Invalid stat. Please choose again.")
                continue
            credit -= 1
        print(f"Stats upgraded! New stats: Strength: {self.strength}, Speed: {self.speed}, Life: {self.life}")
    
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

class Monster(Entity):
    """
    A class representing a monster in the game.
    Inherits from the Entity class.
    """
    def __init__(self, name, strength, speed, life):
        super().__init__(strength, speed, life)
        self.name = name
        self.ca = 10
        self.cr = self.calculate_cr()
        self.xp = random.randint(int(self.cr/3), int(self.cr/2))
        self.gold = random.randint(int(self.cr/3), self.cr)

    def display_stats(self, stats=""):
        stats = f"Name:\t\t{self.name}\n"
        stats = super().display_stats(stats)
        return stats

    @staticmethod
    def generate_random_monster():
        name = random.choice(list(monster_stat_list.keys()))
        stats = monster_stat_list[name]
        strength = random.randint(stats["strength"][0], stats["strength"][1])
        speed = random.randint(stats["speed"][0], stats["speed"][1])
        life = random.randint(stats["life"][0], stats["life"][1])
        return Monster(name, strength, speed, life)
    
    def generate_random_monster_leveled(Character, range:int=2):
        carac_cr = Character.calculate_cr()
        monster = Monster.generate_random_monster()
        while monster.cr < carac_cr - 4*range or monster.cr > carac_cr + range:
            monster = Monster.generate_random_monster()
            monster.cr  = monster.calculate_cr()
            carac_cr    = Character.calculate_cr()

        return monster

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

class Item(Entity):
    """
    A class representing an item in the game.
    Inherits from the Entity class.
    """
    def __init__(self, name, strength, speed, life, maxlife, price, level, xp, rarity):
        super().__init__(strength, speed, life)
        self.name       = name
        self.maxlife    = maxlife
        self.level      = level
        self.gold       = price
        self.xp         = xp
        self.rarity     = rarity
    
    def displayed_name(self):
        """
        Returns the name of the item.
        """
        return Rarity.color_name_from_rarity(self.name, self.rarity)
    
    def display_stats(self, stats=""):
        stats = f"Name:\t\t{self.displayed_name()}\n"
        stats += f"Level:\t\t{self.level:3d}\n"
        stats += f"Rarity:\t\t  {self.rarity.name}\n"
        stats += f"Price:\t\t{self.gold:3d}\n"
        stats += f"XP:\t\t{self.xp:3d}\n"
        stats += f"MaxLife:\t{self.maxlife:3d}\n"
        stats += f"Strength:\t{self.strength:3d}\n"
        stats += f"Speed:\t\t{self.speed:3d}\n"
        stats += f"Life:\t\t{self.life:3d}\n"
        return stats
    
    def use_item(self, character):
        """
        Use the item.
        """
        # Check if it's healing potion
        if self.life > 0:
            character.heal(self.life)
            print(f"\n{self.displayed_name()} has been used! You healed {ctxt(f'{self.life}', Colors.GREEN)} health point!")
        # else it's stat potion
        if self.strength > 0:
            character.strength += self.strength
            print(f"{self.displayed_name()} has been used! You gained {ctxt(f'{self.strength}', Colors.GREEN)} strength point!")
        if self.speed > 0:
            character.speed += self.speed
            print(f"{self.displayed_name()} has been used! You gained {ctxt(f'{self.speed}', Colors.GREEN)} speed point!")
        if self.maxlife > 0:
            character.maxlife += self.maxlife
            print(f"{self.displayed_name()} has been used! You gained {ctxt(f'{self.maxlife}', Colors.GREEN)} max life point!")
            character.heal(character.maxlife)
        # Remove the item from the inventory
        character.remove_from_inventory(self)
        print(f"")
    
    def save(self):
        """
        Save the item to a file.
        """
        save_data = {
            "name": self.name,
            "strength": self.strength,
            "speed": self.speed,
            "life": self.life,
            "maxlife": self.maxlife,
            "price": self.gold,
            "level": self.level,
            "xp": self.xp,
            "rarity": self.rarity.name
        }
        return str(save_data)
    
    @staticmethod
    def load(save_data):
        """
        Load the item from a file.
        """
        save_data = eval(save_data)
        rarity = Rarity.Rarity[save_data["rarity"]]
        # Check if the item is a chest
        if "chest" in save_data["name"]:
            item = Chest(save_data["name"], save_data["strength"], save_data["speed"], save_data["life"], save_data["maxlife"], save_data["price"], save_data["level"], save_data["xp"], rarity)
        else:
            item = Item(save_data["name"], save_data["strength"], save_data["speed"], save_data["life"], save_data["maxlife"], save_data["price"], save_data["level"], save_data["xp"], rarity)
        return item
    
    @staticmethod
    def generate_random_item():
        """
        Generate a random item.
        """
        name = random.choice(list(item_stat_list.keys()))
        stats = item_stat_list[name]
        rarity      = random_rarity()
        level       = random.randint(stats["level"][0],     stats["level"][1])
        stat_bias   = (level+stat_modifier(rarity))

        life        = random.randint(int(stats["life"][0]*stat_bias),
                                     int(stats["life"][1]*stat_bias))

        stat_bias   = (level+stat_modifier(rarity))
        strength    = random.randint(int(stats["strength"][0]*stat_bias),  
                                     int(stats["strength"][1]*stat_bias))
        stat_bias   = (level+stat_modifier(rarity))
        speed       = random.randint(int(stats["speed"][0]*stat_bias),     
                                     int(stats["speed"][1]*stat_bias))
        stat_bias   = (level+stat_modifier(rarity))
        maxlife     = random.randint(int(stats["maxlife"][0]*stat_bias),   
                                     int(stats["maxlife"][1]*stat_bias))

        stat_bias   = (level+stat_modifier(rarity))
        price       = random.randint(int(stats["price"][0]*stat_bias),     
                                     int(stats["price"][1]*stat_bias))

        xp          = random.randint(stats["xp"][0],        stats["xp"][1])
        # Check if the item is a chest
        if "chest" in name:
            return Chest(name, strength, speed, life, maxlife, price, level, xp, rarity)
        else:
            return Item(name, strength, speed, life, maxlife, price, level, xp, rarity)

item_stat_list = {
    "Healing Potion": {
        "strength": (0, 0),
        "speed":    (0, 0),
        "life":     (1, 10),
        "maxlife":  (0, 0),
        "price":    (4, 25),
        "level":    (1, 1),
        "xp":       (0, 0),
        "rarity": Rarity.Rarity.D
    },
    "speed Potion": {
        "strength": (0, 0),
        "speed":    (0, 1),
        "life":     (0, 0),
        "maxlife":  (0, 0),
        "price":    (100, 200),
        "level":    (1, 5),
        "xp":       (0, 0),
        "rarity": Rarity.Rarity.D
    },
    "strength Potion": {
        "strength": (0, 1),
        "speed":    (0, 0),
        "life":     (0, 0),
        "maxlife":  (0, 0),
        "price":    (100, 200),
        "level":    (1, 5),
        "xp":       (0, 0),
        "rarity": Rarity.Rarity.D
    },
    "Life Potion": {
        "strength": (0, 0),
        "speed":    (0, 0),
        "life":     (0, 0),
        "maxlife":  (0, 1),
        "price":    (100, 200),
        "level":    (1, 5),
        "xp":       (0, 0),
        "rarity": Rarity.Rarity.D
    },
    "Gold chest": {
        "strength": (0, 0),
        "speed":    (0, 0),
        "life":     (0, 0),
        "maxlife":  (0, 0),
        "price":    (100, 200),
        "level":    (1, 5),
        "xp":       (0, 0),
        "rarity": Rarity.Rarity.D
    },
    "Xp chest": {
        "strength": (0, 0),
        "speed":    (0, 0),
        "life":     (0, 0),
        "maxlife":  (0, 0),
        "price":    (100, 200),
        "level":    (1, 5),
        "xp":       (0, 0),
        "rarity": Rarity.Rarity.D
    },
}

class Chest(Item):
    """
    A class representing a chest in the game.
    Inherits from the Item class.
    """
    def __init__(self, name, strength, speed, life, maxlife, price, level, xp, rarity):
        super().__init__(name, strength, speed, life, maxlife, price, level, xp, rarity)
        self.name = name
        self.maxlife = maxlife
        self.level = level
        self.gold = price
        self.xp = xp
        self.rarity = rarity

    def use_item(self, character):
        """
        Open the chest and give the loot to the character.
        """
        ### gold chest
        if "Gold" in self.name:
            stat_bias   = (self.level+stat_modifier(self.rarity))
            min = 100*stat_bias
            max = 200*stat_bias
            gold = random.randint(min, max)
            print(f"\n{self.name} contains {ctxt(f'{gold}', Colors.YELLOW)} gold!")
            character.gold += gold

        ### xp chest
        elif "Xp" in self.name:
            stat_bias   = (self.level+stat_modifier(self.rarity))
            min = 10*stat_bias
            max = 20*stat_bias
            xp = random.randint(min, max)
            print(f"\n{self.name} contains {ctxt(f'{xp}', Colors.BLUE)} XP!")
            character.xp += xp
        

        print(f"{self.displayed_name()} has been Opened!\n")
        # Remove the item from the inventory
        character.remove_from_inventory(self)
        
