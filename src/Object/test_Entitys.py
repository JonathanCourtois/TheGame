import pytest
import random
from .Entity import Entity
from src.utils.random_generator import Rarity

# TheGame/src/Entity/test_Entity.py

def test_entity_initialization():
    entity = Entity()
    assert entity.name          == "Entity"
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

def test_get_equipement_name():
    entity = Entity()
    assert entity.get_equipement_name(random.randint(1, 100)) == "E Error"

def test_get_inventory_item_name():
    entity = Entity()
    assert entity.get_inventory_item_name(random.randint(1, 100)) == "E Error"

def test_calculate_cr():
    entity      = Entity()
    expected_cr = int((entity.constitution-1 + entity.strength-1 + entity.focus-1 + entity.level + entity.speed-1 + entity.maxlife/5) / 5)
    assert entity.calculate_cr() == expected_cr

def test_roll_d():
    entity = Entity()
    result = entity.roll_d(6)
    assert 0 <= result <= 6

def test_roll_n_d():
    entity = Entity()
    result = entity.roll_n_d(3, 6)
    assert 3 <= result <= 18

def test_attack():
    entity      = Entity()
    hit, damage = entity.attack()
    assert 0 <= hit <= entity.speed
    assert 1 <= damage <= entity.strength * 2 + 2 # Considering critical hit

def test_defend():
    entity          = Entity()
    initial_life    = entity.life
    entity.defend(hit=5, damage=3)
    assert entity.life <= initial_life

def test_heal():
    entity          = Entity()
    entity.maxlife  = 10
    entity.life     = 5
    entity.heal(10)
    assert entity.life == entity.maxlife

def test_rename():
    entity = Entity()
    entity.rename("NewName")
    assert entity.name == "NewName"

def test_check_level():
    entity      = Entity()
    entity.xp   = (5 * entity.level) ** 2
    entity.Check_level()
    assert entity.level == 2

def test_gain_xp():
    entity = Entity()
    entity.gain_xp((5 * entity.level) ** 2)
    assert entity.level == 2

def test_upgrade_stats():
    entity                  = Entity()
    initial_constitution    = entity.constitution
    entity.upgrade_stats(credit=1)
    assert entity.constitution >= initial_constitution

def test_generate():
    for i in range(10):
        rentity = Entity().generate()
        assert rentity.rarity.name in ["S", "A", "B", "C", "D"]
        assert 1 <= rentity.level <= rentity.maxlevel
        assert 1 <= rentity.constitution <= 50
        assert 1 <= rentity.strength <= 50
        assert 1 <= rentity.focus <= 50
        assert 1 <= rentity.speed <= 50
        assert 10 <= rentity.life <= 500
        assert 10 <= rentity.maxlife <= 500
        rentity = Entity().generate(level=5)
        assert rentity.level == 5
        assert rentity.rarity.name in ["S", "A", "B", "C", "D"]
        rentity = Entity().generate(rarity=Rarity.A)
        assert rentity.rarity.name == "A"
        assert 1 <= rentity.level <= rentity.maxlevel
        rentity = Entity().generate(level=3, rarity=Rarity.B)
        assert rentity.level == 3
        assert rentity.rarity.name == "B"