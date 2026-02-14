# Tic-Tac-Toe Game

A classic two-player Tic-Tac-Toe game implemented in Python for the console.

## Features

- 🎮 Two-player gameplay
- 🎯 Simple console interface
- ✅ Win detection
- 🤝 Draw detection
- 🔢 Position-based input (1-9)

## Requirements

- Python 3.x

## How to Run

```bash
python tictactoe.py
```

## How to Play

1. The game displays a 3x3 grid
2. Players take turns (X goes first)
3. Enter a position number (1-9) to place your mark:
   ```
   1 | 2 | 3
   --+---+--
   4 | 5 | 6
   --+---+--
   7 | 8 | 9
   ```
4. First player to get 3 in a row wins!
5. Game ends in a draw if all positions are filled

## Winning Conditions

Win by getting 3 marks in a row:
- Horizontally (rows)
- Vertically (columns)
- Diagonally

## Example Gameplay

```
 X |   |  
--+---+--
   | O |  
--+---+--
   |   | X

Player X, choose position (1-9): 5
```

## Game Rules

- Players alternate turns
- Cannot place mark on occupied position
- X always goes first
- Game ends when someone wins or board is full

## Code Structure

- `show_board()`: Displays the current game board
- `check_winner()`: Checks if a player has won
- `is_draw()`: Checks if the game is a draw
- `play_game()`: Main game loop

## Future Enhancements

- Single-player mode with AI
- Difficulty levels
- Score tracking across multiple games
- Different board sizes (4x4, 5x5)
- Colorful interface
- Undo move feature
