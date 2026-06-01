from game import check_winner, get_available_moves, make_move, switch_player


def alpha_beta(board, current_player, maximizing_player, alpha, beta):
    winner = check_winner(board)

    if winner == maximizing_player:
        return 1, None
    elif winner == switch_player(maximizing_player):
        return -1, None
    elif winner == "Draw":
        return 0, None

    best_move = None

    if current_player == maximizing_player:
        best_score = -999

        for move in get_available_moves(board):
            new_board = make_move(board, move, current_player)

            score, _ = alpha_beta(
                new_board,
                switch_player(current_player),
                maximizing_player,
                alpha,
                beta
            )

            if score > best_score:
                best_score = score
                best_move = move

            alpha = max(alpha, best_score)

            if beta <= alpha:
                break

        return best_score, best_move

    else:
        best_score = 999

        for move in get_available_moves(board):
            new_board = make_move(board, move, current_player)

            score, _ = alpha_beta(
                new_board,
                switch_player(current_player),
                maximizing_player,
                alpha,
                beta
            )

            if score < best_score:
                best_score = score
                best_move = move

            beta = min(beta, best_score)

            if beta <= alpha:
                break

        return best_score, best_move
