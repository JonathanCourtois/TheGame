from src.Object.character import Character
from src.Object.item import Item
import src.utils.random_generator as randgen
from src.utils.display import ctxt, Colors
import random

class Merchant(Character):
    def __init__(self) -> None:
        """
        Initialize the Merchant class.
        """
        super().__init__()
        # from Character :
        # self.inventory = []
        # self.equipment = {'head': None, 'body': None, 'legs': None, 'feet': None, 'left hand': None, 'right hand': None, 'neck': None, 'ring1': None, 'ring2': None, 'belt': None}
        self.name = "Merchant"
        self.customer = None
        self.store = None

    def trade(self, customer):
        self.customer = customer
        print(f"{self.name}: {self.customer.displayed_name()}, Welcome to my store!")
        self.dialogue()

    def generate(self, customer):
        """
        Generate a random store for the merchant.
        """
        self.customer = customer
        lvl_modifier = random.randint(-5, 5)
        level = int(self.customer.level+lvl_modifier)if int(self.customer.level+lvl_modifier)< self.maxlevel else self.maxlevel
        level = int(level if level > 0 else 1)
        super().generate(level=level)
        store = []
        number_of_item = random.randint(1, 6)
        for i in range(number_of_item):
            store.append(Item.generate_random_item(level=self.level))
        self.store = store
        return self
    
    def display_store(self):
        """
        Display the name and price of the items in the store.
        """
        print(f"{self.name}'s lvl {self.level} Store:")
        for i, item in enumerate(self.store):
            print(f"ID : {i:2d} : {item.displayed_name(left=True)} : lvl {item.level:2d} : {item.rarity.name} : {item.gold} gold")

    def dialogue(self):
        """
        Display the merchant's dialogue.
        """
        self.display_store()

        print(f"\nYour gold: {ctxt(f'{self.customer.gold}', Colors.YELLOW)}")
        print(f"Your inventory items : {len(self.customer.inventory)}/4\n")

        action = input("What would you like to do? (b: buy, s: sell, e: exit) ")
        if action.lower() == 'b':
            self.buy_item()
            self.dialogue()

        if action.lower() == 's':
            print(f"{ctxt('Sell Not implemented yet.',Colors.RED)}")
            self.dialogue()
            
        elif action.lower() == 'e':
            print("Goodbye!")
        
    def buy_item(self):
        """
        Buy an item from the store.
        """
        if len(self.store) <= 0:
            print(f"The Merchant as {ctxt('nothing',Colors.RED)} to sell.")
            return
        
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

        return