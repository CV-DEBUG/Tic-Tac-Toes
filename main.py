import random

# Printing the Board on the Screen
def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

# Create a sample board
board = [' '] * 10

# Call the function to draw the board
drawBoard(board)

# Letting the player choose X or O
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    
# Then who goes first
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else: 
        return 'player'
# Place a Mark on the board
def makeMove(board, letter, move):
    board[move] = letter
