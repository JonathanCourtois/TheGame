# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import random
import math
from src.utils.random_generator import random_rarity, Rarity
from src.utils.display import color_from_rarity, color_text_from_rarity, ctxt, Colors

class Entity:
    def __init__(self):
        self.name = "Entity"
        self.rarity         = Rarity.D

        self.constitution   = 1 # for defense
        self.strength       = 1 # for attack
        self.focus          = 1 # for critical hit
        self.speed          = 1
        self.life           = 10
        self.maxlife        = 10

        self.level          = 1
        self.maxlevel       = 25  

        self.cr             = self.calculate_cr()
        self.gold           = 0
        self.xp             = 0

    def display_stats(self, cr:bool=True, life:bool=True, cst:bool=True, spd:bool=True, strg:bool=True, fcs:bool=True,
                      gold:bool=False, xp:bool=False):
        """
        Display the stats of the entity.
        """
        
        stats = f"Name : {color_text_from_rarity(f'{self.name:^20s}', self.rarity)} : "
        stats = f"{stats}Class {color_text_from_rarity(self.rarity.name, self.rarity)}\n"
        stats = f"{stats}Level {'-'*21} :{' '*3}{self.level:2d}\n"
        if cr:
            stats = f"{stats}CR {'-'*24} :{' '*2}{self.cr:3d}\n"
        if life:
            stats = f"{stats}Life {'-'*22} :{' '*2}{ctxt(f'{self.life:3d}',Colors.GREEN)}/{ctxt(f'{self.maxlife:<3d}',Colors.GREEN)}\n"
        if cst:
            stats = f"{stats}Constitution {'-'*14} :{' '*3}{self.constitution:2d}\n"
        if spd:
            stats = f"{stats}Speed {'-'*21} :{' '*3}{self.speed:2d}\n"
        if strg:
            stats = f"{stats}Strength {'-'*18} :{' '*3}{self.strength:2d}\n"
        if fcs:
            stats = f"{stats}Focus {'-'*21} :{' '*3}{self.focus:2d}\n"
        if gold:
            stats = f"{stats}Gold {'-'*22} :{' '*1}{ctxt(f'{self.gold:4d}',Colors.YELLOW)}\n"
        if xp:
            stats = f"{stats}XP {'-'*24} :{' '*2}{ctxt(f'{self.xp:3d}',Colors.CYAN)}/{ctxt(f'{(4*self.level)**2:<3d}',Colors.CYAN)}\n"
        return stats

    def get_equipement_name(self, slot):
        """
        Get the name of the equipment in the given slot.
        Return E Error because Entity has no equipment.
        """
        return "E Error"

    def get_inventory_item_name(self, index):
        """
        Get the name of the item in the inventory at the given index.
        Return E Error because Entity has no inventory.
        """
        return "E Error"

    def display_sheet(self, equipement=False, inventory=False, xp=False):
        """
        Display the stats in a sheet format:
        # HEADER #
        # Stat 0 | equipment 0 #
        # Stat 1 | equipment 1 #
        # ...
        # Stat n | #
        # Inventory #
        """
        # HEADER
        sw = 120 # Sheet width
        np = 20 # Name padding
        ep = 12 # Equipment padding
        cp = 15 # Empty Cell padding
        vp = 11 # Stat Value padding
        st = 14 # Stat padding
        ip = 45 # Inventory padding
        
        Header  = f"# Name : {color_text_from_rarity(f'{self.name:^{np}s}', self.rarity)} :"
        class_slot = f"Class {color_text_from_rarity(f'{self.rarity.name:1s}', self.rarity)}"
        Header += f"{class_slot:^{vp+11}s}"
        if equipement:
            Header += f"{'#'*(sw-vp-np-29)}"
        Header += f"#\n"

        sheet = f"{Header}# Level {'-'*(st+7)} :{self.level:^{vp}d}"
        eq_h = ''
        if equipement:
            eq_h = f"#{' ':{cp}s}⌈{' Head':^{ep}s}⌉{' ':{cp}s}"
            eq_h += f"⌈{' Neck':^{ep}s}⌉ "

        sheet += f"{eq_h}#\n"
        sheet = f"{sheet}# CR {'-'*(st+10)} :{self.cr:^{vp}d}"
        if equipement:
            eq_h = f"#{' ':{cp}s}⌊{self.get_equipement_name('head'):^{ep}s}⌋{' ':{cp}s}"
            eq_h += f"⌊{self.get_equipement_name('neck'):^{ep}s}⌋ "
        sheet += f"{eq_h}#\n"

        sheet = f"{sheet}# Life {'-'*(st+8)} :{ctxt(f'{self.life:>{int(vp/2)}d}',Colors.GREEN)}/{ctxt(f'{self.maxlife:<{int(vp/2)}d}',Colors.GREEN)}"
        if equipement:
            eq_h = f"# ⌈{'Left  Hand':^{ep}s}⌉"
            eq_h += f"⌈{'Body':^{ep}s}⌉"
            eq_h += f"⌈{'Right Hand':^{ep}s}⌉ "
            eq_h += f"⌈{'Belt':^{ep}s}⌉ "
        sheet += f"{eq_h}#\n"

        sheet += f"# Constitution {'-'*(st)} :{self.constitution:^{vp}d}"
        if equipement:
            eq_h = f"# ⌊{self.get_equipement_name('left hand'):^{ep}s}⌋"
            eq_h += f"⌊{self.get_equipement_name('body'):^{ep}s}⌋"
            eq_h += f"⌊{self.get_equipement_name('right hand'):^{ep}s}⌋ "
            eq_h += f"⌊{self.get_equipement_name('belt'):^{ep}s}⌋ "
        sheet += f"{eq_h}#\n"

        sheet += f"# Speed {'-'*(st+7)} :{self.speed:^{vp}d}"
        if equipement:
            eq_h = f"#{' ':{cp}s}⌈{'Legs':^{ep}s}⌉{' ':{cp}s}"
            eq_h += f"⌈{'Ring 1':^{ep}s}⌉ "
        sheet += f"{eq_h}#\n"

        sheet += f"# Strength {'-'*(st+4)} :{self.strength:^{vp}d}"
        if equipement:
            eq_h = f"#{' ':{cp}s}⌊{self.get_equipement_name('legs'):^{ep}s}⌋{' ':{cp}s}"
            eq_h += f"⌊{self.get_equipement_name('ring1'):^{ep}s}⌋ "
        sheet += f"{eq_h}#\n"

        sheet += f"# Focus {'-'*(st+7)} :{self.focus:^{vp}d}"
        if equipement:
            eq_h = f"#{' ':{cp}s}⌈{'Feet':^{ep}s}⌉{' ':{cp}s}"
            eq_h += f"⌈{'Ring 2':^{ep}s}⌉ "
        sheet += f"{eq_h}#\n"

        sheet += f"# Gold {'-'*(st+8)} :{ctxt(f'{self.gold:^{vp}d}',Colors.YELLOW)}"
        if equipement:
            eq_h = f"#{' ':{cp}s}⌊{self.get_equipement_name('feet'):^{ep}s}⌋{' ':{cp}s}"
            eq_h += f"⌊{self.get_equipement_name('ring2'):^{ep}s}⌋ "
        sheet += f"{eq_h}#\n"

        if xp:
            sheet += f"# XP {'-'*(st+10)} :{ctxt(f'{self.xp:>{int(vp/2)}d}',Colors.CYAN)}/{ctxt(f'{(4*self.level)**2:<{int(vp/2)}d}',Colors.CYAN)}"
            if equipement:
                sheet += f"#{' '*(4*cp-1)}#\n"
            else:
                sheet += f"#\n"

        if inventory:
            # sheet += self.display_inventory_sheet(name_only=True)
            sheet += f"# Inventory {'#'*(st+5+vp+1+4*cp)}\n"
            inventory = ""
            for i in range(2):
                for j in range(2):
                    inventory += f"# [{self.get_inventory_item_name(i):^{ip}s}] #"
                    if j == 0:
                        inventory += " "
                inventory += f"\n"
            sheet += f"{inventory}"

        if inventory or equipement:
            sheet += f"{'#'*(2*ip+ep+1)}\n"
        else:
            sheet += f"{'#'*(np+st+vp-2)}\n"

        return sheet

    def calculate_cr(self):
        """
        Calculate the Challenge Rating (CR) of the entity.
        CR is calculated as the sum of the average competence rolls and the half of the life.
        """
        return int((self.constitution-1 + self.strength-1 + self.focus-1 + self.level + self.speed-1 + self.maxlife/5) / 5)
    
    def displayed_name(self):
        """
        Returns the name of the entity.
        """
        return color_text_from_rarity(f'{self.name:>20s}', self.rarity)

    def roll_d(self, sides):
        """
        Roll a dice with a given number of sides.
        Returns the result of the roll.
        """
        return random.randint(0, sides)

    def roll_n_d(self, n, sides):
        """
        Roll n dice with a given number of sides.
        Returns the result of the roll.
        """
        return sum(self.roll_d(sides) for _ in range(n))

    def attack(self):
        """
        Simulate an attack.
        Returns a tuple of hit and damage.
        """
        combat_log  = ""
        hit         = self.roll_d(self.speed)
        crit        = True if self.roll_d(100) <= self.focus else False
        damage      = 0
        if hit > 0:
            if crit:
                damage  = self.roll_n_d(2, self.strength)+2
                combat_log += f"{self.displayed_name()} made {ctxt(f'{hit:3d}',Colors.RED)} to {ctxt('Crit Hit!',Colors.RED)} for {ctxt(f'{damage:3d}',Colors.RED)} Damage !\n"
            else:
                damage  = self.roll_d(self.strength-1)+1
                combat_log += f"{self.displayed_name()} made {ctxt(f'{hit:3d}',Colors.RED)} to Hit for {ctxt(f'{damage:3d}',Colors.RED)} Damage !\n"
        return hit, damage, combat_log
    
    def defend(self, hit, damage, combat_log=""):
        """
        Simulate defending against an attack.
        If the hit is greater than the CA, reduce life by damage.
        """
        const_check = self.roll_d(self.constitution)
        combat_log  = combat_log
        
        if hit == 0:
            combat_log  = ""
            return combat_log
        
        elif hit > const_check:
            self.life -= damage
            combat_log += f"{self.displayed_name()} takes {ctxt(f'{damage:2d}',Colors.RED)} damage!\n"
            combat_log += self.life_status()

        proba_display = random.random()
        if hit < const_check/2 and proba_display < 0.5:
            combat_log += f"{self.displayed_name()} dodges the attack!\n"
        elif proba_display < 0.5:
            combat_log += f"{self.displayed_name()} blocks the attack!\n"
        else:
            combat_log  = ""
        
        return combat_log

    def life_color(self):
        """
        Returns the color of the life based on the current life.
        """
        if self.life < self.maxlife*0.2:
            return Colors.RED
        elif self.life < self.maxlife*0.5:
            return Colors.YELLOW
        else:
            return Colors.GREEN

    def life_status(self, add_name=True):
        """
        Returns a sentence relating the life status of the entity.
        """
        if add_name:
            name = self.displayed_name()
        else:
            name = ""
        if self.life <= 0:
            return f"{name} is dead!\n"
        elif self.life < self.maxlife*0.2:
            return f"{name} looks really bad!\n"
        elif self.life < self.maxlife*0.5:
            return f"{name} looks wounded!\n"
        else:
            return f"{name} looks to handle it!\n"

    def heal(self, amount):
        """
        Heal the entity by a certain amount.
        If the healed life exceeds max life, set it to max life.
        """
        self.life += amount
        if self.life > self.maxlife:
            self.life = self.maxlife
        print(f"{self.displayed_name()} heals and{self.life_status(add_name=False)}")

    def rename(self, name):
        """
        Rename the entity.
        """
        rename_display = f"{self.displayed_name()} has been renamed to "
        self.name = name
        rename_display += f"{self.displayed_name()} !"
        print(rename_display)

    def Check_level(self, randomize=False, debug=False):
        """
        Check the xp and set the level of the entity
        Give one credit to upgrade stats per level until max level.
        """
        if self.xp >= (4*self.level)**2: # Level up condition
            self.xp -=  (4*self.level)**2
            if self.level >= self.maxlevel:
                print(f"{self.displayed_name()} is already at max level!")
                return
            self.level += 1
            print(f"{self.displayed_name()} leveled up! New level: {self.level}")
            self.upgrade_stats(credit=1, randomize=randomize, debug=debug)
        return 
    
    def gain_xp(self, xp, randomize=False, debug=False):
        """
        Gain xp and check if the entity levels up.
        """
        self.xp += xp
        print(f"{self.displayed_name()} gained {xp} XP!")
        self.Check_level(randomize=randomize, debug=debug)

    def upgrade_stats(self, credit=1, randomize=False, debug=False):
        """
        Upgrade the entity's stats.
        Allows the entity to upgrade n stats randomly.
        """
        stats = {1: "constitution", 2: "strength", 3: "focus", 4: "speed", 5: "maxlife"}
        while credit > 0:
            if randomize:
                action = random.randint(1, 5)
                if debug:
                    print(f"{self.displayed_name()} randomly chose to upgrade {stats[action]}!")
            else:
                print(f"\n{self.display_sheet(equipement=True, inventory=True, xp=True)}")
                print(f"{self.displayed_name()} has {credit} upgrade credits left.")
                print("Available stats to upgrade:")
                for i, stat in stats.items():
                    print(f"{i} - {stat}")
                action = input("Enter the number of the stat you want to upgrade: ")
                try:
                    action = int(action)
                    if action < 1 or action > 5:
                        print("Invalid input. Please enter a number between 1 and 5.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
            if action == 1:
                self.constitution += 1
            elif action == 2:
                self.strength += 1
            elif action == 3:
                self.focus += 1
            elif action == 4:
                self.speed += 1
            elif action == 5:
                self.maxlife    += 10
                self.life       += 10
            credit -= 1
            if debug:
                print(f"{self.displayed_name()} upgraded {stat} to {getattr(self, stat)}!")
        self.cr = self.calculate_cr()
        if debug:
            print(f"{self.displayed_name()} CR is now {self.cr}!")
            print(self.display_stats(xp=True))

    def generate(self, level:int = None, rarity:Rarity = None):
        """
        Generates a random entity with a random rarity and stats.
        """
        if rarity is None: # Set rarity to random value
            self.rarity = random_rarity()
        else:
            self.rarity = rarity
        # Add credits upgrade from rarity
        rarity_credit = (self.rarity.value-1)*5

        if level is None: # Set level to random value
            self.level = random.randint(1, self.maxlevel)
        else:
            self.level = min(level, self.maxlevel)
        # Add credits upgrade from level
        level_credit = self.level-1

        total_credit = rarity_credit + level_credit
        # Upgrade stats
        self.upgrade_stats(credit=total_credit, randomize=True, debug=False)
        return self

if __name__ == "__main__":
    entity = Entity()
    print(entity.display_stats())
    entity.attack()
    entity.defend(5, 3)
    entity.heal(5)
    entity.rename("NewName")
    entity.gain_xp(10)
    entity.upgrade_stats(credit=2, debug=True)
    for i in range(10):
        rentity = Entity().generate()
        rentity.rename("RandomEntity")
        print(rentity.display_stats())
    
    rentity = Entity().generate(level=25)
    rentity.xp = 10000
    for i in range(2**3):
        a,b,x = bin(i)[2:].zfill(3)
        print(rentity.display_sheet(inventory=bool(int(a)), equipement=bool(int(b)), xp=bool(int(x))))
    rentity.display_sheet(equipement=True, inventory=True, xp=True)
        