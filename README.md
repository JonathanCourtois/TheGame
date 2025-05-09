# The Game

## Overview
The Game is a character-based adventure game where players can generate unique characters with varying statistics based on rarity classes. Players can manage their characters' inventory and equipment as they embark on their journey in a roguelike experience.

## Features
- **Random Character Generation**: Characters are created with unique stats like strength, speed, and life.
- **Rarity Classes**: Characters belong to rarity classes (S, A, B, C, D) that influence their stats.
- **Inventory Management**: Manage items across multiple inventory slots.
- **Equipment System**: Equip characters with gear across various slots.
- **Roguelike Gameplay**: Characters are deleted upon death, encouraging replayability with new characters.

## Project Structure
```
TheGame-0.0.1/
├── src/
│   ├── main.py          # Entry point for the game
│   ├── character.py     # Character generation and management
│   ├── inventory.py     # Inventory system
│   ├── equipment.py     # Equipment management
│   ├── rarity.py        # Rarity class definitions
│   ├── game.py          # Core game logic
│   └── utils.py         # Utility functions
├── play.py              # Script to start the game
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
```

## Getting Started

### Prerequisites
- **Git Bash**: Install Git Bash from [Git Downloads](https://git-scm.com/downloads).
- **UV Environment**: Install UV using one of the following methods:
   - Recommended: Follow the [UV Installation Guide](https://docs.astral.sh/uv/getting-started/installation).

### Installation
1. Download the latest release from [The Game Releases](https://github.com/astral-sh/TheGame/releases).
2. Unzip the downloaded file into a folder of your choice.
3. Open a Git Bash terminal in the folder where you unzipped the file (right-click and select "Git Bash Here").
4. Initialize the UV environment:
    ```bash
    uv sync
    ```
5. Run the game:
    ```bash
    uv run play.py
    ```

## Gameplay
- Start the game to generate a random character with unique stats.
- Manage your character's inventory and equipment.
- Explore the game world and face various challenges, from harmless to deadly.
- Characters are deleted upon death, but you can restart with a new character.
- Enjoy the roguelike experience with endless replayability.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to:
- Submit a pull request.
- Open an issue.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any questions or feedback, please open an issue on the [GitHub repository](https://github.com/astral-sh/TheGame).
