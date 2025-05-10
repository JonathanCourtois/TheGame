from src.Object.character import Character, Item
import src.utils.random_generator as randgen
from src.utils.display import ctxt, Colors
import random

class Merchant:
    def __init__(self, character) -> None:
        """
        Initialize the Merchant class.
        """
        self.name = "Merchant"
        self.customer = character
        self.store = self.generate_merchant_store()
        print(f"{self.name}: {self.customer.displayed_name()}, Welcome to my store!")
        self.display_store()
        self.dialogue()

    def generate_merchant_store(self):
        """
        Generate a random store for the merchant.
        """
        store = []
        number_of_item = random.randint(1, 6)
        for i in range(number_of_item):
            store.append(Item.generate_random_item())
        return store
    
    def display_name_item_and_price(self):
        """
        Display the name and price of the items in the store.
        """
        print(f"{self.name}'s Store:")
        for i, item in enumerate(self.store):
            print(f"ID : {i:2d} : {item.displayed_name():30} : lvl {item.level:2d} : {item.rarity.name} : {item.gold} gold")

    def display_store(self):
        """
        Display the store items.
        """
        print(f"{self.name}'s Store:")
        for i, item in enumerate(self.store):
            print(f"ID : {i:2d}\n{item.display_stats()}")

    def dialogue(self):
        """
        Display the merchant's dialogue.
        """
        self.display_name_item_and_price()

        print(f"\nYour gold: {ctxt(f'{self.customer.gold}', Colors.YELLOW)}")
        print(f"Your inventory space : {len(self.customer.inventory)}/4\n")

        action = input("What would you like to do? (b: buy, s: item stat, e: exit) ")
        if action.lower() == 'b':
            self.buy_item()

        if action.lower() == 's':
            self.display_store()
            self.dialogue()
            
        elif action.lower() == 'e':
            print("Goodbye!")
        
    def buy_item(self):
        """
        Buy an item from the store.
        """
        item_index = int(input("Enter the index of the item you want to buy: "))
        if item_index < 0 or item_index >= len(self.store):
            print("Invalid index.")
            return
        item = self.store[item_index]
        if self.customer.gold > item.gold:
            if len(self.customer.inventory) >= 4:
                print("You can't carry more than 4 items.")
            else:
                print(f"You bought {item.name} for {item.gold} gold.")
                # Add the item to the character's inventory
                self.customer.inventory.append(item)
                # character.inventory.append(item)
                # Remove the item from the store
                self.store.pop(item_index)
                self.customer.gold -= item.gold
                print(f"You have {ctxt(f'{self.customer.gold}',Colors.YELLOW)} gold left.")
        else:
            print("You don't have enough gold.")
        self.dialogue()