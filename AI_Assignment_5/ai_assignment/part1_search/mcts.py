import random
from game import check_winner, get_available_moves, make_move, switch_player


def random_playout(board, current_player):
    while True:
        winner = check_winner(board)

        if winner is not None:
            return winner

        moves = get_available_moves(board)
        move = random.choice(moves)

        board = make_move(board, move, current_player)
        current_player = switch_player(current_player)


def mcts(board, player, simulations=1000):
    moves = get_available_moves(board)

    if not moves:
        return None

    move_scores = {}

    for move in moves:
        wins = 0

        for _ in range(simulations):
            new_board = make_move(board, move, player)
            winner = random_playout(new_board, switch_player(player))

            if winner == player:
                wins += 1
            elif winner == "Draw":
                wins += 0.5

        move_scores[move] = wins

    best_move = max(move_scores, key=move_scores.get)

    return best_move
