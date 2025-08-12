# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import random
from src.Object.character import Character
from src.Object.monster import Monster
from src.utils.display import ctxt, Colors, timed_input

def fight(fighters_list:list):
    """
    Simulates a fight between a character and a monster.
    The character and monster take turns attacking each other until one of them runs out of life.
    """
    print("\n\n### FIGHT ###\n")
    # Check if fighters_list is empty
    if not fighters_list:
        print(f"{ctxt('ERROR', Colors.RED)}: No fighters to fight.")
        return
    # Check if fighters_list has more than 2 fighters
    if len(fighters_list) > 2:
        print(f"{ctxt('ERROR', Colors.RED)}: Too many fighters to fight. Only 2 fighters are allowed for now.")
        return  
    fighters = []
    # Initialize fighters list with each item of list being a list with :
    # [0:fighter, 1:speed_counter, 2:flee, 3:open_inventory]
    for entity in fighters_list:
        fighters.append([entity, 0, False, False])
    # Fight loop
    max_speed = max(entity.speed for entity, _, _, _ in fighters)

    while all(entity.life > 0 for entity, _, _, _ in fighters):
        for i, fighter in enumerate(fighters):
            action = ""
            combat_log = "\n"
            fighter[1] += fighter[0].speed
            if fighter[1] >= max_speed:
                fighter[1] -= max_speed
                if fighter[3]:
                    fighter[0].manage_inventory()
                    fighter[3] = False
                elif fighter[2]:
                    print(f"{fighter[0].displayed_name()} tried to flee!")
                    # to flee, the character must succeed a d'speed' roll facing the monster's d'speed' roll
                    flee_roll    = fighter[0].roll_d(fighter[0].speed)
                    opponent_roll = fighters[1-i][0].roll_d(fighters[1-i][0].speed)
                    if flee_roll > opponent_roll:
                        print(f"{fighter[0].displayed_name()} fled successfully!")
                        return
                    else:
                        print(f"{fighter[0].displayed_name()} failed to flee!")
                else:
                    hit, damage, combat_log = fighter[0].attack()
                    combat_log = fighters[1-i][0].defend(hit, damage, combat_log)

                if isinstance(fighter[0], Character):
                    if not(combat_log == "" or combat_log == "\n"):
                        print(combat_log)
                        action = timed_input("\npress i to open inventory, f to flee or any other key to continue\n", timeout=1)
                    # else:
                        # action = timed_input("", timeout=1)
                elif isinstance(fighter[0], Monster):
                    if fighter[0].life < fighter[0].maxlife / 4:
                        flee_roll = fighter[0].roll_d(100)
                        if flee_roll < fighter[0].life * 100 / fighter[0].maxlife:
                            action = "f"

                if action == "i":
                    fighter[3] = True
                elif action == "f":
                    fighter[2] = True
                else:
                    fighter[3] = False
                    fighter[2] = False
                if fighters[1-i][0].life <= 0:
                    break


    # Check which fighter has been defeated
    for i, fighter in enumerate(fighters):
        if fighter[0].life <= 0:
            print(f"\n{fighter[0].displayed_name()} has been {ctxt('defeated',Colors.RED)} by {fighters[1-i][0].displayed_name()}!")
            # delete save file if it's a character
            if isinstance(fighter[0], Character):
                fighter[0].delete_save_file()
                exit()
            else:
                print(f"{fighters[1-i][0].displayed_name()} wins the fight!")
                won_gold = fighter[0].gold
                xpc      = (4*fighter[0].level)**2
                won_xp   = random.randint(int(xpc*0.1), int(xpc*0.3))
                fighters[1-i][0].gold += won_gold
                fighters[1-i][0].xp   += won_xp
                if isinstance(fighters[1-i][0], Character):
                    print(f"{fighters[1-i][0].displayed_name()} gained {ctxt(f'{won_gold}', Colors.YELLOW)} gold and {ctxt(f'{won_xp}', Colors.BLUE)} experience points!")  

                if isinstance(fighters[1-i][0], Character):
                    fighters[1-i][0].Check_level(randomize=False, debug=False)
                else:
                    fighters[1-i][0].Check_level(randomize=True, debug=False)
            return
    print(f"{ctxt('ERROR', Colors.RED)}: Fight ended without a winner. This should not happen.")
    return

def fight_difficulty(character, monster):
    """
    Determines the difficulty of the fight based on the character's and monster's CR.
    easy caracter cr >= monster cr + 2
    fair caracter cr is between monster cr - 2 and monster cr + 2
    hard caracter cr <= monster cr - 2
    """
    if character.cr >= monster.cr + 1:
        return "easy"
    elif character.cr <= monster.cr - 1:
        return "hard"
    else:
        return "fair"