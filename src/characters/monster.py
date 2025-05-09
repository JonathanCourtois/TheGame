import random
from characters.character import Character
class Monster:
    def __init__(self, name, strength, speed, life):
        self.name       = name
        self.strength   = strength
        self.speed      = speed
        self.life       = life
        self.ca         = 10
        self.cr = self.calculate_cr()

    def display_stats(self):
        return f"Name: {self.name}, Strength: {self.strength}, Speed: {self.speed}, Life: {self.life}, CR: {self.cr}"
    
    def calculate_cr(self):
        """
        Calculate the Challenge Rating (CR) of the monster.
        CR is calculated as the average of the strength, speed, and life.
        """
        return (self.strength + self.speed + self.life)

    @staticmethod
    def generate_random_monster():
        name = random.choice(list(monster_stat_list.keys()))
        stats = monster_stat_list[name]
        strength = random.randint(stats["strength"][0], stats["strength"][1])
        speed = random.randint(stats["speed"][0], stats["speed"][1])
        life = random.randint(stats["life"][0], stats["life"][1])
        return Monster(name, strength, speed, life)
    
    def generate_random_monster_leveled(Character, range:int=5):
        carac_cr = Character.calculate_cr()
        monster = Monster.generate_random_monster()
        while monster.cr < carac_cr - range or monster.cr > carac_cr + range:
            monster = Monster.generate_random_monster()
        return monster

monster_stat_list = {
    "Goblin": {
        "strength": (5, 10),
        "speed": (5, 10),
        "life": (10, 20),
        "cr": ((5+10)+(5+10)+(10+20))/2
    },
    "Slime": {
        "strength": (1, 5),
        "speed": (1, 5),
        "life": (5, 15),
        "cr": ((1+5)+(1+5)+(5+15))/2
    },
    "Wolf": {
        "strength": (5, 10),
        "speed": (8, 15),
        "life": (15, 20),
        "cr": ((5+10)+(8+15)+(15+20))/2
    },
    "Bandit": {
        "strength": (10, 15),
        "speed": (8, 15),
        "life": (15, 25),
        "cr": ((10+15)+(8+15)+(15+25))/2
    }
}