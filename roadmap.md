# Project Roadmap
=====================================

## Phase 1: Stabilize the core loop (priority 1)
--------------------------------------------

| Task | Status |
| --- | --- |
| Fix combat flow bugs: ensure the winner is always determined correctly | [x] |
| Fix combat flow bugs: stop unintended exits or early termination | [x] |
| Fix combat flow bugs: validate turns, flee logic, and inventory actions during combat | [x] |
| Clean the main game loop: validate action choices | [x] |
| Clean the main game loop: avoid repeated or broken prompts | [x] |
| Clean the main game loop: improve user feedback and error handling | [x] |
| Fix save system: create a consistent save file structure | [x] |
| Fix save system: define save behavior for character creation, overwrite, delete, and loading | [x] |
| Fix save system: avoid accidental deletion or invalid state | [x] |
| Validate character progression: level-up logic | [x] |
| Validate character progression: XP gain and thresholds | [x] |
| Validate character progression: health restoration and death state | [x] |

## Phase 2: Complete the equipment and inventory system (priority 2)
--------------------------------------------

| Task | Status |
| --- | --- |
| Display equipment slots : Head, Body, Legs, Feet, right/left Hand, Neck, Belt, Rings | [x] |
| Generate blank item | [x] |
| Add / Remove item to character inventory | [x] |
| Create equipment generation rules by rarity and level | [x] |
| Add equip / unequip actions to the character inventory flow | [x] |
| Add stat bonuses from equipment items | [x] |
| Prevent invalid equipment placement or duplicate slot misuse | [X] |
| Ensure equipment is visible in the character sheet and inventory | [X] |
| Add equipment to merchant | [X] |

## Phase 3: Build progression and economy (priority 3)
--------------------------------------------

| Task | Status |
| --- | --- |
| Balance monster difficulty against player character level/CR | [ ] |
| Improve gold rewards and merchant pricing | [ ] |
| Improve item rarity scaling and sell/buy logic | [ ] |
| Implement level-up bonuses in a readable format | [ ] |
| Improve experience and reward curves for exploration and combat | [ ] |
| Define run progression: enemy scaling, item quality, merchant availability | [ ] |

## Phase 4: Expand content and world interactions (priority 4)
--------------------------------------------

| Task | Status |
| --- | --- |
| Add more monster types and templates | [ ] |
| Add persistant monster that kill previous ca | [ ] |
| Add more consumable item types and chest variations | [ ] |
| Create distinct event types: combat encounters | [ ] |
| Create distinct event types: treasures | [ ] |
| Create distinct event types: traps | [ ] |
| Create distinct event types: merchants | [ ] |
| Create distinct event types: healing events | [ ] |
| Create distinct event types: optional challenges | [ ] |
| Add dungeon or zone progression | [ ] |
| Add a world map or encounter sequence if the game expands beyond a simple loop | [ ] |

## Phase 5: Persistence, polish, and quality of life (priority 5)
--------------------------------------------

| Task | Status |
| --- | --- |
| Improve display and UI formatting | [ ] |
| Add a proper naming flow and character summary | [ ] |
| Improve logging for actions and combat state | [ ] |
| Add achievements or progression goals | [ ] |
| Add proper error handling and player feedback for edge cases | [ ] |
| Refactor repeated logic into cleaner modules and utilities | [ ] |
| Write unit tests for critical systems | [ ] |

## Phase 6: Long-term vision: deeper roguelike features
--------------------------------------------

### Possible future additions:
- different biomes or regions
- multiple character classes or archetypes
- deeper merchant and economy rules
- rarity-based crafting or upgrading
- procedural map generation
- death and run reset flow with persistent meta progression
- achievement and title system
- multiple save slots or profile management

## Release plan
- v0.1: stable core loop, basic combat, basic inventory
- v0.2: equipment system and progression fixes
- v0.3: improved monsters, loot, and merchant economy
- v0.4: save flow and quality-of-life upgrades
- v0.5: content expansion and balancing pass
- v1.0: polished, stable, and reasonably complete game loop

## Order of execution
1. Fix combat and save system
2. Complete equipment and inventory behavior
3. Balance progression and economy
4. Add more content and enemy variety
5. Refactor and polish for release

# Project Details :
## Skills:
- Constitution : use to counter attacks : is Hit_Value > 1d(CON) ?
- Strength : use to deal damage : Damage = 1d(STR) if Hit
- Focus : Percent limit to deal critical damage, it double the dice : if 1d100 <= focus -> Damage = 2d(STR) if Hit
- Speed : Set how many round you can have per turn in opositions to your opponent speed. Add use to hit 1d(SPD)
- Dexterity : Not added. but may be can be use to hit against speed ?

## CR
The challenge rating (CR) is a measure of the relative power of an encounter or creature. It helps to balance the encounter.

for now cr = (CON + STR + SPD + FOC + LVL + MAX_LIFE/10) / 6

## Rules for Balance:

There is 5 Caracteristics that can be increased : CON, STR, SPD, FOC, MaxLife.

Each level grant 1 skill point.

If we consider a mean of 5 pts per Carac, it means that we have 25 points to distribute and then the maximum level is set to 25

BUT, there is 2 other way to gain Skill point : Rarity and Equipment.

# Rarity
Rarity is set between S, A, B, C, D. Each rarity has a different effect on the skill points :
- S : : +25 Skills point 
- A : : +20 Skills point 
- B : : +15 Skills point 
- C : : +10 Skills point 
- D : : +5 Skills point 

# Rarity Probability Explanation
Character and objects rarity is define randomly at its creation.
The probability of the rarity is calculated using the Fibonacci sequence. The formula for calculating the probability of each rarity is:

D = 1/phi^0 (where phi is the golden ratio, approximately 1.61803398875)
C = D/phi
B = C/phi
A = B/phi
S = A/phi

In simpler terms, this means that:

- S (rare) has a probability of about 8.6% 
- A (uncommon) has a probability of about 15.3%
- B (average) has a probability of about 23.9%
- C (common) has a probability of about 38.2%
- D (very common) has a probability of about 61.8%


# Equipment

There is 10 different equipement slots on a character : 
'head', 'body', 'legs', 'feet', 'left hand', 'right hand', 'neck', 'ring1', 'ring2', 'belt'

Each slot can hold an item that has a specific type, rarity and caracteristics. The equipment system allows the player to equip items on their character, which will affect their stats if they have the levels required.

