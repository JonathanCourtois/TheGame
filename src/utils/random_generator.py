# -*- coding: utf-8 -*-
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

def stat_modifier(rarity):
    """
    Returns a tuple of stat modifiers based on the rarity.
    """
    stat_mod = 0
    for i in range(0, rarity.value):
        stat_mod += random.randint(0, 1)
    return stat_mod

def rand_gold(max_gold:int=10):
    """
    Returns a random amount of gold between 0 and max_gold, default is 10.
    """
    return random.randint(1, max_gold)

def get_heal(max_heal:int=10):
    """
    Returns a random amount of heal potion between 1 and max_heal, default is 10.
    """
    return random.randint(1, max_heal)

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

def generate_item(level:int = None, rarity:Rarity = None):
    from src.Object.item import Item

    return Item.generate_random_item(level = level, rarity = rarity)

def generate_equipment(level:int = None, rarity:Rarity = None, type:str = None):
    from src.Object.equipment import Equipment

    return Equipment.generate_random_equipment(level = level, rarity = rarity, type = type)