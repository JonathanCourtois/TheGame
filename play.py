import random
from src.Object.character import Character
from src.Object.monster import Monster
from src.utils.merchant import Merchant
import src.utils.random_generator as randgen
import src.utils.fight as fight
import src.utils.display as dsp
import os


def main():

    # Initialize the game
    print("\n### Welcome to The Game! ###\n\n")
    print(" DEV MSG TO DEV : ADD Utils/message.py where there will be all the messages to display.\n")

    character = Character().manage_save()
    if character is None:
        character = Character().generate()
        print(f"New character created:\n")

    # Display character stats
    print(character.display_sheet())

    # Start the game loop (placeholder for now)
    while True:
        action = input("\nWhat would you like to do? (s: stats, i: inventory, e: explore, r: rest, rename: rename character, exit: exit) ")
        print("")
        if action.lower() == 'exit':
            character.save()
            print("\n### Exiting the game. Goodbye! ###")
            break

        elif action.lower() == 'rename':
            new_name = input("Enter a new name for your character: ")
            character.name = new_name
            print(f"Character renamed to {character.displayed_name()}!")

        elif action.lower() == 's':
            print(f"Character Stats:\n{character.display_sheet()}")

        elif action.lower() == 'i':
            print(f"{dsp.ctxt('WARNING', dsp.Colors.RED)}: Inventory management is work in progress.")
            character.manage_inventory()

        elif action.lower() == 'r':
            rest_heal = randgen.get_heal(max_heal=3)-1
            character.heal(rest_heal)
            print(f"You rested and recovered {dsp.ctxt(f'{rest_heal}', dsp.Colors.GREEN)} health!")

        elif action.lower() == 'e':
            encounter_seed = random.random() # Random seed for encounters

            if encounter_seed < 0.05: # Fight 0.05
                print("You found a random monster!")
                monster = Monster().generate()
                print(f"{monster.display_sheet()}")
                fight.fight([character, monster])

            elif encounter_seed < 0.2:
                gold = randgen.rand_gold(max_gold=8+int(character.level*2))
                print(f"You found {dsp.ctxt(f'{gold}',dsp.Colors.YELLOW)} gold!")
                character.gold += gold

            elif encounter_seed < 0.4:
                print("You found a healing plant!")
                some_life = randgen.get_heal()
                character.heal(some_life)

            elif encounter_seed < 0.6:
                print("You found nothing in this peacefull world.")

            elif encounter_seed < 0.8:
                print("You found a merchant!")
                merchant = Merchant().generate(character)
                merchant.trade(character)

            else:
                print("You encountered a monster!")
                monster = Monster().generate_ranged(character, range=character.level-1)
                print(f"{monster.display_sheet()}")
                fight.fight([character, monster])

        elif action.lower() == 'level':
            action = input("Enter the level you want to reach: ")
            try:
                level = int(action)
                if level > 0:
                    character.level = level
                    print(f"Character leveled up to {level}!")
                else:
                    print("Level must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif action.lower() == 'motherload': # debug
            action = input("Enter the amount of gold you want to add: ")
            try:
                gold = int(action)
                if gold > 0:
                    character.gold += gold
                    print(f"Added {gold} gold to character!")
                else:
                    print("Gold must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a number.")  
        elif action.lower() == 'spawn item': # debug
            item = randgen.generate_item()
            character.add_to_inventory(item)
            print(f"Spawned item: {item.displayed_name()}")

        elif action.lower() == 'rg': # debug
            character = randgen.generate_character()
            print(f"New Character Stats:\n{character.display_stats()}")

        
        else:
            print("Action not recognized. Please try again.")

if __name__ == "__main__":
    main()