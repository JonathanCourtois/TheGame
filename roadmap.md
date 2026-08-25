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
| Fix save system: create a consistent save file structure | [ ] |
| Fix save system: define save behavior for character creation, overwrite, delete, and loading | [x] |
| Fix save system: avoid accidental deletion or invalid state | [ ] |
| Validate character progression: level-up logic | [x] |
| Validate character progression: XP gain and thresholds | [x] |
| Validate character progression: health restoration and death state | [x] |

## Phase 2: Complete the equipment and inventory system (priority 2)
--------------------------------------------

| Task | Status |
| --- | --- |
| Implement equipment slots properly: weapon | [ ] |
| Implement equipment slots properly: body armor | [ ] |
| Implement equipment slots properly: head/helmet | [ ] |
| Implement equipment slots properly: belt | [ ] |
| Implement equipment slots properly: neck | [ ] |
| Implement equipment slots properly: rings | [ ] |
| Implement equipment slots properly: boots | [ ] |
| Implement equipment slots properly: gloves/arms | [ ] |
| Add equip / unequip actions to the character inventory flow | [ ] |
| Add stat bonuses from equipment items | [ ] |
| Prevent invalid equipment placement or duplicate slot misuse | [ ] |
| Create equipment generation rules by rarity and level | [ ] |
| Ensure equipment is visible in the character sheet and inventory | [ ] |

## Phase 3: Build progression and economy (priority 3)
--------------------------------------------

| Task | Status |
| --- | --- |
| Balance monster difficulty against player character level/CR | [ ] |
| Improve gold rewards and merchant pricing | [ ] |
| Add item rarity scaling and sell/buy logic | [ ] |
| Implement level-up bonuses in a readable format | [ ] |
| Add experience and reward curves for exploration and combat | [ ] |
| Define run progression: enemy scaling, item quality, merchant availability | [ ] |

## Phase 4: Expand content and world interactions (priority 4)
--------------------------------------------

| Task | Status |
| --- | --- |
| Add more monster types and templates | [ ] |
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

