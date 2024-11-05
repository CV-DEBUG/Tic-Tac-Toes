import random
import os
import time

# Clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display the board
def draw_board(board):
    clear_terminal()
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---+---+---")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print()

# Choose the player's symbol
def get_player_letter():
    letter = ''
    while letter not in ['X', 'O']:
        letter = input('Do you want to be X or O? ').upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

# Determine who goes first
def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

# Place a symbol on the board
def make_move(board, letter, move):
    board[move] = letter

# Check if a player has won
def is_winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))

# Check if the board is full
def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True

# Check if a space is free
def is_space_free(board, move):
    return board[move] == ' '

# Get the player's move
def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        move = input('What is your next move? (1-9) ')
    return int(move)

# Choose a random move from a list of possible moves
def choose_random_move(board, moves_list):
    possible_moves = [move for move in moves_list if is_space_free(board, move)]
    if possible_moves:
        return random.choice(possible_moves)
    else:
        return None

# Get the computer's move
def get_computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Try to win
    for i in range(1, 10):
        copy = board[:]
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i

    # Try to block the player from winning
    for i in range(1, 10):
        copy = board[:]
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    # Take the center if it's free
    if is_space_free(board, 5):
        return 5

    # Take a free corner
    return choose_random_move(board, [1, 3, 7, 9])

print('Welcome to Tic-Tac-Toe!')

while True:
    # Reset the board
    the_board = [' '] * 10
    player_letter, computer_letter = get_player_letter()
    turn = who_goes_first()
    print(f'The {turn} goes first.')
    game_is_playing = True

    while game_is_playing:
        if turn == 'player':
            # Player's turn
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print('Congratulations! You have won!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn
            draw_board(the_board)
            print("The Terminator is thinking...")
            time.sleep(2)  # 2-second delay before the computer's move
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print('The Terminator has won. You lost.')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break