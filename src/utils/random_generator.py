
import random
from enum import Enum

class Rarity(Enum):
    S = 1
    A = 2
    B = 3
    C = 4
    D = 5

    @classmethod
    def get_probability(cls):
        return {
            cls.S: 0.05,
            cls.A: 0.15,
            cls.B: 0.30,
            cls.C: 0.30,
            cls.D: 0.20
        }

    @classmethod
    def random_rarity(cls):
        probabilities = cls.get_probability()
        total = sum(probabilities.values())
        rand = random.uniform(0, total)
        cumulative = 0
        for rarity, probability in probabilities.items():
            cumulative += probability
            if rand < cumulative:
                return rarity
   
rarity_probabilities = {
        Rarity.S: 0.05,
        Rarity.A: 0.15,
        Rarity.B: 0.30,
        Rarity.C: 0.30,
        Rarity.D: 0.20,
    }

def generate_character():
    from src.Entity.character import Character

    rarity = random_rarity()

    stats = {
        'strength': random.randint(0, 1)    + stat_modifier(rarity),
        'speed':    random.randint(1, 2)    + stat_modifier(rarity),
        'life':     random.randint(1, 10)   + stat_modifier(rarity),
    }
    character = Character(stats['strength'], stats['speed'], stats['life'], rarity)
    return character

def random_rarity():
    """
    Returns a random rarity based on the defined probabilities.
    """
    rarity = random.choices(
        list(rarity_probabilities.keys()),
        weights=list(rarity_probabilities.values()),
        k=1
    )[0]
    return rarity

def stat_modifier(rarity):
    """
    Returns a tuple of stat modifiers based on the rarity.
    """
    rarity_ID = {
        Rarity.S: 5,
        Rarity.A: 4,
        Rarity.B: 3,
        Rarity.C: 2,
        Rarity.D: 1,
    }
    stat_mod = 0
    for i in range(0, rarity_ID[rarity]):
        stat_mod += random.randint(0, 1)
    return stat_mod

def gold_chest():
    """
    Returns a random amount of gold between 0 and 10.
    """
    return random.randint(0, 10)

def heal_potion():
    """
    Returns a random amount of heal potion between 1 and 10.
    """
    return random.randint(1, 10)
         
    
def color_from_rarity(name, rarity):
    """
    Returns a colored name based on the rarity.
    """
    color = {
        Rarity.S: "\033[1;35m",  # Magenta
        Rarity.B: "\033[1;34m",  # Blue
        Rarity.C: "\033[1;32m",  # Green
        Rarity.A: "\033[1;33m",  # Yellow
        Rarity.D: "\033[1;31m",  # Red
    }
    return f"{color[rarity]}{name}\033[0m"