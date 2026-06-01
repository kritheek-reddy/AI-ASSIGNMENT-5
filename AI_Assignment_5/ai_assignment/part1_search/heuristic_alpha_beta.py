from game import check_winner, get_available_moves, make_move, switch_player, EMPTY


def evaluate_line(line, player):
    opponent = switch_player(player)

    if line.count(player) == 3:
        return 100
    elif line.count(player) == 2 and line.count(EMPTY) == 1:
        return 10
    elif line.count(player) == 1 and line.count(EMPTY) == 2:
        return 1
    elif line.count(opponent) == 2 and line.count(EMPTY) == 1:
        return -10
    elif line.count(opponent) == 3:
        return -100

    return 0


def heuristic(board, player):
    lines = []

    lines.extend(board)

    for col in range(3):
        lines.append([board[0][col], board[1][col], board[2][col]])

    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    score = 0

    for line in lines:
        score += evaluate_line(line, player)

    return score


def heuristic_alpha_beta(board, current_player, maximizing_player, alpha, beta, depth):
    winner = check_winner(board)

    if winner == maximizing_player:
        return 100, None
    elif winner == switch_player(maximizing_player):
        return -100, None
    elif winner == "Draw":
        return 0, None

    if depth == 0:
        return heuristic(board, maximizing_player), None

    best_move = None

    if current_player == maximizing_player:
        best_score = -999

        for move in get_available_moves(board):
            new_board = make_move(board, move, current_player)

            score, _ = heuristic_alpha_beta(
                new_board,
                switch_player(current_player),
                maximizing_player,
                alpha,
                beta,
                depth - 1
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

            score, _ = heuristic_alpha_beta(
                new_board,
                switch_player(current_player),
                maximizing_player,
                alpha,
                beta,
                depth - 1
            )

            if score < best_score:
                best_score = score
                best_move = move

            beta = min(beta, best_score)

            if beta <= alpha:
                break

        return best_score, best_move
