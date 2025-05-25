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

def test_generate():
    for i in range(10):
        rentity = Character().generate()
        assert rentity.rarity.name in ["S", "A", "B", "C", "D"]
        assert rentity.level == 1
        assert 1 <= rentity.constitution <= 50
        assert 1 <= rentity.strength <= 50
        assert 1 <= rentity.focus <= 50
        assert 1 <= rentity.speed <= 50
        assert 10 <= rentity.life <= 500
        assert 10 <= rentity.maxlife <= 500
        rentity = Character().generate(level=5)
        assert rentity.level == 5
        assert rentity.rarity.name in ["S", "A", "B", "C", "D"]
        rentity = Character().generate(rarity=Rarity.A)
        assert rentity.rarity.name == "A"
        assert 1 <= rentity.level <= rentity.maxlevel
        rentity = Character().generate(level=3, rarity=Rarity.B)
        assert rentity.level == 3
        assert rentity.rarity.name == "B"

def test_display_sheet():
    entity = Character().generate(level=1, rarity=Rarity.D)
    sheet = entity.display_sheet()
    print(sheet)
    assert "Name :" in sheet
    assert "Character" in sheet
    assert "Class " in sheet
    assert "D" in sheet
    assert "Level " in sheet
    assert "10" in sheet
    assert "1" in sheet
    assert "CR " in sheet
    assert "Life " in sheet
    assert "Constitution " in sheet
    assert "Speed " in sheet
    assert "Strength " in sheet
    assert "Focus " in sheet
    assert "Gold " in sheet
    assert "XP " in sheet   
    assert "16" in sheet
    assert "Inventory" in sheet
    assert "Empty" in sheet
    assert "Left" in sheet
    assert "Right" in sheet
    assert "Hand" in sheet
    assert "Head" in sheet
    assert "Body" in sheet
    assert "Legs" in sheet
    assert "Feet" in sheet
    assert "Neck" in sheet
    assert "Ring 1" in sheet
    assert "Ring 2" in sheet
    assert "Belt" in sheet

def test_displayed_name():
    entity = Character().generate(level=1, rarity=Rarity.D)
    displayed_name = entity.displayed_name()
    assert displayed_name == "\x1b[1;31mCharacter\x1b[0m"

    entity.name = "Hero"
    displayed_name = entity.displayed_name()
    assert displayed_name == "\x1b[1;31mHero\x1b[0m"


        