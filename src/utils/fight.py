import os
from src.utils.display import ctxt, Colors

def fight(character, monster):
    """
    Simulates a fight between a character and a monster.
    The character and monster take turns attacking each other until one of them runs out of life.
    """
    print(f"A wild {monster.name} appears!")
    print(f"Monster Stats:\n{monster.display_stats()}")
    print(f"Character Stats:\n{character.display_stats()}")

    print(f"{character.name} vs {monster.name}!")
    print(f"your cr is {character.cr} and the monster's cr is {monster.cr} the fight looks {fight_difficulty(character, monster)}\n")
    input("press enter to start the fight !")

    open_inventory  = False
    flee            = False
    # Fight loop
    fighters = [character, monster]
    max_speed = max(fighter.speed for fighter in fighters)
    speed_counter = [0, 0]
    while character.life > 0 and monster.life > 0:
        for i, fighter in enumerate(fighters):
            speed_counter[i] += fighter.speed
            if speed_counter[i] >= max_speed:
                speed_counter[i] -= max_speed
                if open_inventory:
                    fighter.manage_inventory()
                    open_inventory  = False
                elif flee:
                    print(f"{character.name} tried to flee!")
                    # to flee, the character must succeed a d20 roll + speed facing the monster's d20 roll + speed
                    flee_roll    = character.roll_d(20) + character.speed
                    monster_roll = monster.roll_d(20) + monster.speed
                    if flee_roll > monster_roll:
                        print(f"{character.name} fled successfully!")
                        return
                    else:
                        print(f"{character.name} failed to flee!")
                else:
                    hit, damage = fighter.attack()
                    fighters[1-i].defend(hit, damage)
                action = input("\npress i to open inventory, f to flee or any other key to continue!\n")

                if action == "i":
                    open_inventory = True
                elif action == "f":
                    flee = True
                else:
                    open_inventory  = False
                    flee            = False
                if fighters[1-i].life <= 0:
                    break
    
    if character.life <= 0:
        print(f"{character.name} has been {ctxt('defeated',Colors.RED)} by {monster.name}!")
        # delete save file
        if os.path.exists("save/character_save.txt"):
            os.remove("save/character_save.txt")
        print(ctxt("\nSave file deleted.", Colors.RED))
        print(ctxt("GAME OVER\n", Colors.RED))
        exit()
    elif monster.life <= 0:
        print(f"{monster.name} has been {ctxt('defeated',Colors.RED)} by {character.name}!")
        character.get_loot_from_monster(monster)


def fight_difficulty(character, monster):
    """
    Determines the difficulty of the fight based on the character's and monster's CR.
    easy caracter cr >= monster cr + 2
    fair caracter cr is between monster cr - 2 and monster cr + 2
    hard caracter cr <= monster cr - 2
    """
    if character.cr >= monster.cr + 2:
        return "easy"
    elif character.cr <= monster.cr - 2:
        return "hard"
    else:
        return "fair"