# -*- coding: utf-8 -*-
import src.Object.Entity as Entity

import random
import math
from enum import Enum

class Rarity(Enum):
    S = 5
    A = 4
    B = 3
    C = 2
    D = 1

    @classmethod
    def get_probability(cls):
        phi = (1+math.sqrt(5))/2
        d   = 100/sum([1/phi**i for i in range(0, 5)])
        c   = d/phi
        b   = c/phi
        a   = b/phi
        s   = a/phi
        return {
            cls.S: s,
            cls.A: a,
            cls.B: b,
            cls.C: c,
            cls.D: d
        }

    @classmethod
    def random_rarity(cls):
        probabilities = cls.get_probability()
        total = sum(probabilities.values())
        rand  = random.uniform(0, total)
        cumulative = 0
        for rarity, probability in probabilities.items():
            cumulative += probability
            if rand < cumulative:
                return rarity


def random_rarity():
    """
    Returns a random rarity based on the defined probabilities.
    """
    rarity = random.choices(
        list(Rarity.get_probability().keys()),
        weights=list(Rarity.get_probability().values()),
        k=1
    )[0]
    return rarity

def generate_entity(entity, level:int = None, rarity:Rarity = None):
    """
    Generates a random entity with a random rarity and stats.
    """
    if rarity is None: # Set rarity to random value
        entity.rarity = random_rarity()
    else:
        entity.rarity = rarity
    # Add credits upgrade from rarity
    rarity_credit = (entity.rarity.value-1)*5

    if level is None: # Set level to random value
        entity.level = random.randint(1, entity.maxlevel)
    else:
        entity.level = min(level, entity.maxlevel)
    # Add credits upgrade from level
    level_credit = entity.level-1

    total_credit = rarity_credit + level_credit
    # Upgrade stats
    entity.upgrade_stats(credit=total_credit)
    return entity



def generate_character():
    from src.Object.character import Character

    rarity = random_rarity()

    stats = {
        'strength': random.randint(0, 1)    + stat_modifier(rarity),
        'speed':    random.randint(1, 2)    + stat_modifier(rarity),
        'life':     random.randint(1, 10)   + stat_modifier(rarity),
    }
    character = Character(stats['strength'], stats['speed'], stats['life'], rarity)
    return character

def stat_modifier(rarity):
    """
    Returns a tuple of stat modifiers based on the rarity.
    """
    stat_mod = 0
    for i in range(0, rarity.value):
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