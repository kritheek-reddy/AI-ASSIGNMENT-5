from game import print_board, PLAYER_X
from minimax import minimax
from alpha_beta import alpha_beta
from heuristic_alpha_beta import heuristic_alpha_beta
from mcts import mcts


board = [
    ["X", "X", " "],
    ["O", "O", " "],
    [" ", " ", " "]
]

print("Current Board:")
print_board(board)

print("\n1. Minimax Result")
score, move = minimax(board, PLAYER_X, PLAYER_X)
print("Best score:", score)
print("Best move:", move)

print("\n2. Alpha-Beta Result")
score, move = alpha_beta(board, PLAYER_X, PLAYER_X, -999, 999)
print("Best score:", score)
print("Best move:", move)

print("\n3. Heuristic Alpha-Beta Result")
score, move = heuristic_alpha_beta(board, PLAYER_X, PLAYER_X, -999, 999, depth=3)
print("Best score:", score)
print("Best move:", move)

print("\n4. Monte Carlo Tree Search Result")
move = mcts(board, PLAYER_X, simulations=500)
print("Best move:", move)
