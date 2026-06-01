EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    lines = []

    lines.extend(board)

    for col in range(3):
        lines.append([board[0][col], board[1][col], board[2][col]])

    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] != EMPTY and line[0] == line[1] == line[2]:
            return line[0]

    if is_full(board):
        return "Draw"

    return None


def is_full(board):
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def get_available_moves(board):
    moves = []

    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                moves.append((r, c))

    return moves


def make_move(board, move, player):
    r, c = move
    new_board = [row[:] for row in board]
    new_board[r][c] = player
    return new_board


def switch_player(player):
    if player == PLAYER_X:
        return PLAYER_O
    return PLAYER_X
