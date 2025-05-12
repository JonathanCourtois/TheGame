import pytest
from .character import Character
from src.utils.random_generator import Rarity

# TheGame/src/Entity/test_character.py

def test_character_initialization():
    entity = Character()
    assert entity.name          == "Character"
    assert entity.rarity.name   == "D"
    assert entity.constitution  == 1
    assert entity.strength      == 1
    assert entity.focus         == 1
    assert entity.speed         == 1
    assert entity.life          == 10
    assert entity.maxlife       == 10
    assert entity.level         == 1
    assert entity.maxlevel      == 25
    assert entity.cr            == entity.calculate_cr()
    assert entity.gold          == 0
    assert entity.xp            == 0

def test_generate_character():
    for i in range(10):
        rentity = Character().generate_character()
        assert rentity.rarity.name in ["S", "A", "B", "C", "D"]
        assert rentity.level == 1
        assert 1 <= rentity.constitution <= 50
        assert 1 <= rentity.strength <= 50
        assert 1 <= rentity.focus <= 50
        assert 1 <= rentity.speed <= 50
        assert 10 <= rentity.life <= 500
        assert 10 <= rentity.maxlife <= 500
        rentity = Character().generate_character(level=5)
        assert rentity.level == 5
        assert rentity.rarity.name in ["S", "A", "B", "C", "D"]
        rentity = Character().generate_character(rarity=Rarity.A)
        assert rentity.rarity.name == "A"
        assert 1 <= rentity.level <= rentity.maxlevel
        rentity = Character().generate_character(level=3, rarity=Rarity.B)
        assert rentity.level == 3
        assert rentity.rarity.name == "B"