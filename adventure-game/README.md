# Adventure Game 🎮

A simple text-based adventure game built with Python where players explore different rooms, collect items, and progress through the game.

## Description

This is a console-based adventure game where you navigate through various rooms, discover items, and build your inventory. The game features a simple command-line interface with an interactive menu system.

## Features

- 🚪 Multiple rooms to explore (Entrance, Hall, Treasure Room)
- 🎒 Inventory system to collect and manage items
- 🗝️ Item collection mechanism
- 💎 Progressive gameplay with connected rooms
- 🎯 Simple and intuitive text-based interface

## How to Run

1. Make sure you have Python installed (Python 3.x recommended)
2. Clone this repository or download the `adventure.py` file
3. Navigate to the project directory
4. Run the game:

```bash
python adventure.py
```

## Game Instructions

When you start the game, you'll be presented with options:

1. **Move forward** - Navigate to the next room
2. **Take item** - Pick up an item in the current room (if available)
3. **Show inventory** - Display all items you've collected
4. **Quit** - Exit the game

### Gameplay Tips

- Explore each room carefully to find items
- Check your inventory to see what you've collected
- Progress through all rooms to win the game

## Project Structure

```
adventure-game/
│
├── adventure.py      # Main game file containing all game logic
└── README.md         # Project documentation
```

## Game Classes

### Room
Represents a game room with:
- Name
- Description
- Optional item
- Connection to next room

### Player
Manages player state:
- Inventory system for collected items

## Future Enhancements

Potential features to add:
- Multiple paths and choices
- Puzzles and challenges
- Combat system
- Save/load game state
- More diverse items with special abilities
- Random room generation

## Requirements

- Python 3.x

## License

This project is open source and available for educational purposes.

## Author

Created as a learning project for Python game development.

---

Enjoy your adventure! 🗺️
