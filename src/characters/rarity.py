from enum import Enum
import random

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
            
    
def color_name_from_rarity(name, rarity):
    """
    Returns a colored name based on the rarity.
    """
    color = {
        Rarity.S: "\033[1;35m",  # Magenta
        Rarity.A: "\033[1;34m",  # Blue
        Rarity.B: "\033[1;32m",  # Green
        Rarity.C: "\033[1;33m",  # Yellow
        Rarity.D: "\033[1;31m",  # Red
    }
    return f"{color[rarity]}{name}\033[0m"