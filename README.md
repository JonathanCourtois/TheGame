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
thegame
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── characters
│   │   ├── __init__.py
│   │   ├── character.py
│   │   └── rarity.py
│   ├── inventory
│   │   ├── __init__.py
│   │   └── inventory.py
│   ├── equipment
│   │   ├── __init__.py
│   │   └── equipment.py
│   └── utils
│       ├── __init__.py
│       └── random_generator.py
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies listed in `requirements.txt` using pip:
   ```
   pip install -r requirements.txt
   ```
4. Run the game by executing the `main.py` file:
   ```
   python src/main.py
   ```

## Gameplay
- Upon starting the game, a random character will be generated.
- Players can view their character's stats and manage their inventory and equipment.
- Explore the game world and engage in various adventures with your unique character.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.