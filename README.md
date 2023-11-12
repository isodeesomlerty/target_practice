# Target Practice

Welcome to Target Practice, a Python-based game where your objective is to hit a moving target with bullets fired from a stationary ship.

![Target Practice Game](images/Target%20Practice%20Poster.png)

## How to Play

Once you start the game, a target will appear on the screen, moving back and forth. Your goal is to control the ship at the bottom of the screen to shoot bullets at the target. You must aim carefully and predict the target's movement because you only have a limited number of bullets!

## Controls

- **UP Arrow Key**: Move the ship up.
- **DOWN Arrow Key**: Move the ship down.
- **SPACEBAR**: Fire a bullet.
- **Q Key**: Quit the game.
- **Mouse Click**: Click the 'Play' button on the screen to start the game.

## Installation

To play Target Practice, you will need Python and Pygame installed on your system. If you do not have Python or Pygame installed, you can download them from [python.org](https://www.python.org/) and [pygame.org](https://www.pygame.org/), respectively.

After installing Python and Pygame, follow these steps:

1. Download or clone the repository to your local machine.
2. Navigate to the directory where you downloaded the game.
3. Run the game with `python target_practice.py`.

## Requirements

- Python 3.x
- Pygame

## Features

- Fullscreen gameplay
- Dynamic difficulty (the game gets harder every time you hit the target)
- Simple and intuitive controls

## Custom Game Settings

You can customize the game settings by editing `settings.py`. This includes screen size, bullet speed, and other game-related configurations.

## Game Components

The game consists of several modules:

- `settings.py`: Contains the settings for the game.
- `game_stats.py`: Tracks statistics such as how many misses are left.
- `button.py`: Creates a button for starting the game.
- `ship.py`: Manages the player's ship.
- `bullet.py`: Manages the bullets fired by the ship.
- `rectangle.py`: Manages the target.

## Contributions

Feel free to fork the project, open issues, and submit pull requests. Your contributions are welcome!

Enjoy the game!
