import pytest
import random
from .item import Item, item_list
from src.utils.random_generator import Rarity


item_names = ["Healing Potion", "Gold Chest", "XP Chest", "Mystery Chest", "Mastery Chest"]

def test_entity_initialization():
    item = Item()
    assert item.name          == "Item"
    assert item.rarity.name   == "D"
    assert item.constitution  == 0
    assert item.strength      == 0
    assert item.focus         == 0
    assert item.speed         == 0
    assert item.life          == 0
    assert item.maxlife       == 0
    assert item.level         == 0
    assert item.maxlevel      == 20
    assert item.cr            == 0
    assert item.gold          == 0
    assert item.xp            == 0
    assert item.gold_amount   == 0
    assert item.affect        == []
    assert item.chose         == []

def test_generate():
    for i in range(10):
        item = Item().generate_random_item(level=None, rarity=None)
        assert item.rarity.name in ["S", "A", "B", "C", "D"]
        assert 1<= item.level <= item.maxlevel
        assert 0 <= item.constitution <= 50
        assert 0 <= item.strength <= 50
        assert 0 <= item.focus <= 50
        assert 0 <= item.speed <= 50
        assert 0 <= item.life <= 500
        assert 0 <= item.maxlife <= 500
    item = Item().generate_random_item(level=2, rarity=Rarity.A)
    assert item.rarity.name == "A"
    assert item.level == 2

def test_item_list():
    assert isinstance(item_list, dict)
    assert len(item_list) > 0
    key_names = list(item_list.keys())
    for name in key_names:
        assert name in item_names, f"{name} not found in item_list keys"