import random
from src.Object.character import Character
from src.Object.monster import Monster
import src.utils.random_generator as randgen
import src.utils.fight as fight
# import src.utils.merchant as Merchant
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
        action = input("\nWhat would you like to do? (s: stats, i: inventory, e: explore, rename: rename character, exit: exit) ")
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
            print(f"{dsp.ctxt('ERROR', dsp.Colors.RED)}: Inventory management is not implemented yet.")
            # character.manage_inventory()

        elif action.lower() == 'e':
            enconter_seed = random.random()
            enconter_seed = 0.9
            if enconter_seed < 0.05: # Fight
                print("You found a random monster!")
                monster = Monster().generate()
                fight.fight([character, monster])

            elif enconter_seed < 0.3:
                gold = randgen.gold_chest()
                print(f"You found {dsp.ctxt(f'{gold}',dsp.Colors.YELLOW)} gold!")
                character.gold += gold

            elif enconter_seed < 0.6:
                print("You found a healing potion!")
                heal_potion = randgen.heal_potion()
                character.heal(heal_potion)

            elif enconter_seed < 0.8:
                print("You found a merchant!")
                print(f"{dsp.ctxt('ERROR', dsp.Colors.RED)}: merchant is not implemented yet.")
                # merchant = Merchant(character)
            else:
                print("You found a monster!")
                monster = Monster().generate_ranged(character)
                print(f"Monster encountered:\n{monster.display_sheet()}")
                action = input("Do you want to fight the monster? (yes/no) ")
                if action.lower() == 'yes':
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
        elif action.lower() == 'gold': # debug
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