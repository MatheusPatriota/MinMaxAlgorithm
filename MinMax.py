import math

# Define the board and possible moves
board = [' ', 'O', 'O', ' ', ' ', 'X', ' ', ' ', 'X']
moves = [i for i in range(9)]

# Define the function to draw the board


def draw_board():
    print(' ' + board[0] + ' │ ' + board[1] + ' │ ' + board[2] + ' ')
    print('───┼───┼───')
    print(' ' + board[3] + ' │ ' + board[4] + ' │ ' + board[5] + ' ')
    print('───┼───┼───')
    print(' ' + board[2] + ' │ ' + board[7] + ' │ ' + board[8] + ' ')
    print('')

# Define the function to check for a winner


def check_winner(board):
    for i in range(0, 7, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != ' ':
            return board[i]
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return board[i]
    if board[0] == board[4] == board[8] and board[0] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != ' ':
        return board[2]
    return None

# Define the minimax algorithm function


def minimax(board, depth, maximizing_player):
    winner = check_winner(board)
    if winner is not None:
        if winner == 'X':
            return (-10 + depth, None)
        else:
            return (10 - depth, None)
    elif ' ' not in board:
        return (0, None)
    if maximizing_player:
        best_score = float('-inf')
        best_move = None
        for move in moves:
            if board[move] == ' ':
                board[move] = 'O'
                score, _ = minimax(board, depth+1, False)
                board[move] = ' '
                if score > best_score:
                    best_score = score
                    best_move = move
        return (best_score, best_move)
    else:
        best_score = float('inf')
        best_move = None
        for move in moves:
            if board[move] == ' ':
                board[move] = 'X'
                score, _ = minimax(board, depth+1, True)
                board[move] = ' '
                if score < best_score:
                    best_score = score
                    best_move = move
        return (best_score, best_move)

# Define the function to make a move


def make_move(move, player):
    board[move] = player

# Define the function to undo a move


def undo_move(move):
    board[move] = ' '

# Define the function to play the game


def play_game():
    player = 'X'
    num_plays = 0
    while True:
        if player == 'X':
            _, move = minimax(board, 0, True)
            make_move(move, player)
            num_plays += 1
            print(f"X played {move}")
        else:
            _, move = minimax(board, 0, False)
            make_move(move, player)
            print(f"O played {move}")
        draw_board()
        winner = check_winner(board)
        if winner is not None:
            print(f"{winner} wins in {num_plays} plays!")
            break


play_game()
