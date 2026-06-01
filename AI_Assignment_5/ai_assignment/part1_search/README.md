# Assignment 1: Game Search Algorithms

## Objective

The objective of this assignment is to implement and compare different AI game search algorithms using a two-player game.

The algorithms implemented are:

1. Minimax Search
2. Alpha-Beta Pruning
3. Heuristic Alpha-Beta Search
4. Monte Carlo Tree Search

## Game Selected

The game selected for implementation is **Tic-Tac-Toe**.

Tic-Tac-Toe is a two-player, turn-based, zero-sum game. It is suitable for studying game search algorithms because both players try to make optimal moves and the game has clear winning, losing, and draw conditions.

## Folder Structure

```text
Assignment_1_Game_Search/
│
├── game.py
├── minimax.py
├── alpha_beta.py
├── heuristic_alpha_beta.py
├── mcts.py
├── test_cases.py
└── README.md
```

## File Description

### `game.py`

This file contains the basic Tic-Tac-Toe game logic.

It includes:

- Board display
- Checking winner
- Checking draw condition
- Getting available moves
- Making a move
- Switching player

### `minimax.py`

This file contains the Minimax algorithm.

Minimax explores all possible future moves and chooses the move that gives the best result for the current player.

### `alpha_beta.py`

This file contains the Alpha-Beta Pruning algorithm.

Alpha-Beta Pruning is an optimized version of Minimax. It avoids checking branches that cannot affect the final decision.

### `heuristic_alpha_beta.py`

This file contains depth-limited Alpha-Beta search using a heuristic evaluation function.

This is useful when searching the entire game tree is expensive.

### `mcts.py`

This file contains a simple Monte Carlo Tree Search implementation.

MCTS uses random simulations to estimate which move gives the best result.

### `test_cases.py`

This file runs all four algorithms on the same Tic-Tac-Toe board and prints the best move selected by each algorithm.

## Algorithms Explained

## 1. Minimax Search

Minimax is a recursive game search algorithm.

It assumes that both players play optimally.

The current player tries to maximize the score, while the opponent tries to minimize the score.

Scoring system used:

```text
Win  = +1
Loss = -1
Draw = 0
```

## 2. Alpha-Beta Pruning

Alpha-Beta Pruning improves Minimax by reducing the number of nodes searched.

It uses two values:

```text
Alpha = best value found so far for the maximizer
Beta  = best value found so far for the minimizer
```

If beta becomes less than or equal to alpha, the remaining branch is skipped.

This gives the same result as Minimax but with less computation.

## 3. Heuristic Alpha-Beta Search

Heuristic Alpha-Beta is a depth-limited version of Alpha-Beta Pruning.

Instead of searching the full game tree, it searches only up to a given depth.

After reaching the depth limit, it estimates the board value using a heuristic function.

The heuristic checks possible winning lines and gives scores based on how strong the position is.

Example:

```text
Three marks in a row        = 100
Two marks and one empty     = 10
One mark and two empty      = 1
Opponent threat             = negative score
```

## 4. Monte Carlo Tree Search

Monte Carlo Tree Search uses random simulations to select the best move.

For each possible move, the algorithm simulates many random games and counts how often the player wins.

The move with the highest number of wins is selected.

Since MCTS uses randomness, the result can sometimes vary between runs.

## Test Board Used

The following board is used in the test case:

```text
X | X |  
---------
O | O |  
---------
  |   |  
---------
```

Player X has an immediate winning move at position:

```text
(0, 2)
```

This means row 0 and column 2.

## How to Run

Open Terminal inside the assignment folder and run:

```bash
python3 test_cases.py
```

## Expected Output

The output should be similar to:

```text
Current Board:
X | X |  
---------
O | O |  
---------
  |   |  
---------

1. Minimax Result
Best score: 1
Best move: (0, 2)

2. Alpha-Beta Result
Best score: 1
Best move: (0, 2)

3. Heuristic Alpha-Beta Result
Best score: 100
Best move: (0, 2)

4. Monte Carlo Tree Search Result
Best move: (0, 2)
```

Note: The Monte Carlo Tree Search result may sometimes be different because it uses random simulations.

## Conclusion

Minimax gives the optimal move by checking all possible game states.

Alpha-Beta Pruning gives the same result as Minimax but avoids unnecessary search.

Heuristic Alpha-Beta is useful when full search is not possible due to large game trees.

Monte Carlo Tree Search chooses moves based on random simulations and improves as the number of simulations increases.
