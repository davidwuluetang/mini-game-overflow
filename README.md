# Mini-Game Overflow
<img src="https://github.com/davidwuluetang/mini-game-overflow/assets/122414668/67d10e3e-ef79-45c1-b876-6404f94bc248" width="600">

### Game rules
This game is a 2D board game. Initially player 1 has a gem in the top left corner and player 2 has a gem in the bottom right corner. Players take turns adding one gem per turn to the board. A gem can be added to any empty square or any square where the player has at least one gem. If the number of gems in a square reaches the number of neighbours for the cell, the gems overflow into its neighbours, increasing the number of gems and changing the colour of gems to that player's colour.The game ends if every single gem on the board is the same colour. The player represented by that colour is the winner of the game.

### How to run the game
You will need install [Python](https://www.python.org/downloads/) and [Pygame](https://pypi.org/project/pygame/) to run this game.

Once you have them installed, run following command in the terminal where you have the files.
```python
python game.py
```

### About this project
This is a school project from my DSA course. The purpose of this repo is to demonstrate understanding of game tree data structure and minimax algorithm. Most of the pygame creation codes are provided by the professor. Here is the original [file](https://github.com/davidwuluetang/mini-game-overflow/blob/main/game_original.py). I added features like reset game, undo moves, and bot level adjustments on top of that.
