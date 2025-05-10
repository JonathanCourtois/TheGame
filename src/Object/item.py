from src.Object.Entity import Entity
import src.utils.rarity as Rarity

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
        
