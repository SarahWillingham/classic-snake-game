# 🐍 Snake Game (Python Turtle)

A classic Snake game built in Python using the `turtle` graphics module. This project is a simple but fun implementation that lets players control a growing snake to eat food, avoid walls, and prevent collisions with its own tail.

## Features
- Smooth snake movement using the arrow keys
- Increasing difficulty as the snake grows
- Food generation with randomized placement
- Score tracking and reset on collision
- Game over alert using `tkinter.messagebox`
- Speed scales with snake length for extra challenge
- Clean reset functionality after losing


## Project Structure
snake_game/
├── main.py # Main game loop and logic
├── snake_class.py # Snake behavior and movement
├── food.py # Food generation
├── score_board.py # Score tracking and display
├── README.md # This file
└── .gitignore # Recommended .gitignore


## Requirements
- Python 3.x
- No external libraries needed — just the standard `turtle` and `tkinter` modules (built into Python)

## How to Run
1. Clone the repo or download the files:
   ```bash
   git clone https://github.com/SarahWillingham/classic-snake-game.git
   cd classic-snake-game

 2. Run the game:
    python main.py
    
## Controls
Arrow Up — Move up, Arrow Down — Move down, Arrow Left — Move left, Arrow Right — Move right

## Ideas for Future Improvements
Pause/resume functionality, Sound effects, Difficulty settings, Obstacle generation, Smoother 180 turns
