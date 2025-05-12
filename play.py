import random
from src.Object.character import Character
import src.utils.random_generator as randgen
import src.utils.fight as fight
# import src.utils.merchant as Merchant
import src.utils.display as dsp
import os


def main():

    # Initialize the game
    print("Welcome to The Game!\n")

    # check if save directory exists
    if not os.path.exists("save"):
        os.makedirs("save")
        print("Save directory created.")
    # Ask to load old save file ?
    try:
        with open("save/character_save.txt", "r") as f:
            action = input("A save file was found, do you want to load it? (y/n) ")
            if action.lower() == 'y':
                # Load character from save file
                character = Character.load(f.read())
                print(f"Character loaded: {character.name}")
            else:
                # Generate a random character
                character = Character().generate_character()
                print(f"New character created: {character.name}")
    except FileNotFoundError:
        # Generate a random character
        character = Character().generate_character()
        print(f"New character created: {character.name}")

    # Display character stats
    print(f"Character Stats:\n{character.display_stats()}")
    character.display_inventory_name_only()

    # Start the game loop (placeholder for now)
    while True:
        action = input("\nWhat would you like to do? (s: stats, i: inventory, e: explore, rename: rename character, exit: exit) ")
        print("")
        if action.lower() == 'exit':
            with open("save/character_save.txt", "w") as f:
                f.write(character.save())
            print("Character saved!\n")
            print("Exiting the game. Goodbye!")
            break
        elif action.lower() == 'rename':
            new_name = input("Enter a new name for your character: ")
            character.name = new_name
            print(f"Character renamed to {new_name}!")

        elif action.lower() == 's':
            print(f"Character Stats:\n{character.display_stats()}")

        elif action.lower() == 'i':
            character.manage_inventory()

        elif action.lower() == 'e':
            enconter_seed = random.random()
            if enconter_seed < 0.05: # Fight
                print("You found a random monster!")
                monster = Monster.generate_random_monster()
                fight.fight(character, monster)
            elif enconter_seed < 0.3:
                gold = randgen.gold_chest()
                print(f"You found {ctxt(f'{gold}',Colors.YELLOW)} gold!")
                character.gold += gold

            elif enconter_seed < 0.6:
                print("You found a healing potion!")
                heal_potion = randgen.heal_potion()
                character.heal(heal_potion)

            elif enconter_seed < 0.8:
                print("You found a merchant!")
                merchant = Merchant(character)
            else:
                monster = Monster.generate_random_monster_leveled(character)
                fight.fight(character, monster)

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