import random
from src.Entity.Entity import Entity
from src.utils.display import ctxt, Colors

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
