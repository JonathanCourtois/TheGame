import pytest
import random
from .monster import Monster
from src.utils.random_generator import Rarity

def test_monster_initialization():
    monster = Monster()
    assert monster.name          == "Monster"
    assert monster.rarity.name   == "D"
    assert monster.constitution  == 1
    assert monster.strength      == 1
    assert monster.focus         == 1
    assert monster.speed         == 1
    assert monster.life          == 10
    assert monster.maxlife       == 10
    assert monster.level         == 1
    assert monster.maxlevel      == 25
    assert monster.cr            == monster.calculate_cr()
    assert monster.gold          == 0
    assert monster.xp            == 0
    assert monster.inventory     == []
    for key in monster.equipment.keys():
        assert monster.equipment[key] == None

def test_generate():
    for i in range(10):
        monster = Monster().generate()
        assert monster.rarity.name in ["S", "A", "B", "C", "D"]
        assert 1 <= monster.level <= 25
        assert 1 <= monster.constitution <= 50
        assert 1 <= monster.strength <= 50
        assert 1 <= monster.focus <= 50
        assert 1 <= monster.speed <= 50
        assert 10 <= monster.life <= 500
        assert 10 <= monster.maxlife <= 500
        monster = Monster().generate(level=5)
        assert monster.level == 5
        assert monster.rarity.name in ["S", "A", "B", "C", "D"]
        monster = Monster().generate(rarity=Rarity.A)
        assert monster.rarity.name == "A"
        assert 1 <= monster.level <= monster.maxlevel
        monster = Monster().generate(level=3, rarity=Rarity.B)
        assert monster.level == 3
        assert monster.rarity.name == "B"