# The Game

## Overview
The Game is a character-based adventure game where players can generate unique characters with varying statistics based on rarity classes. Players can manage their characters' inventory and equipment as they embark on their journey.

## Features
- Random character generation with statistics: strength, speed, and life.
- Rarity classes: S, A, B, C, and D, each affecting character stats.
- Inventory management with multiple slots for items.
- Equipment system with various slots for different gear.

## Project Structure
```
TheGame-0.0.1/
├── src/
│   ├── main.py
│   ├── character.py
│   ├── inventory.py
│   ├── equipment.py
│   ├── rarity.py
│   ├── game.py
│   └── utils.py
├── play.py
├── requirements.txt
├── README.md
```

## Setup Instructions
### Requirements:
- Bash command line:
  1. Install Git Bash from: [Download Git](https://git-scm.com/downloads)
- UV environment:
  2. Install UV:
     - Recommended: `winget install --id=astral-sh.uv -e`
     - Alternative: [UV Installation Guide](https://docs.astral.sh/uv/getting-started/installation/)
  3. Download the latest release (Zip for Windows or tar.gz for Linux) from: [The Game Releases](https://github.com/astral-sh/TheGame/releases)
  4. Unzip the file into a folder of your choice.
  5. Open a Git Bash terminal in the folder where you unzipped the file (right-click and select "Git Bash Here").
  6. Initialize the UV environment with the command:
```bash
uv sync
```
  7. Run the game with the command:
```bash
uv run play.py
```


## Gameplay
- Upon starting the game, a random character will be generated.
- Players can view their character's stats and manage their inventory and equipment.
- Explore the game world and engage in various adventures with your unique character.
- Players can encounter various challenges, ranging from harmless to deadly.
- The game deletes the character upon death.
- As a roguelike game, players can restart with a new character after death.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.