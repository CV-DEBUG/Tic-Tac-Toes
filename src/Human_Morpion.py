import os
from typing import List

class TicTacToe:
    def __init__(self):
        self.board: List[str] = [' '] * 10
        self.current_player: str = ''
        self.player_letter: str = ''
        self.other_letter: str = ''

    def draw_board(self) -> None:
        """
        Display the current state of the board.

        Print the board with the current state of the game.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f' {self.board[7]} | {self.board[8]} | {self.board[9]} ')
        print('-----------')
        print(f' {self.board[4]} | {self.board[5]} | {self.board[6]} ')
        print('-----------')
        print(f' {self.board[1]} | {self.board[2]} | {self.board[3]} ')

    def setup_game(self) -> None:
        """Initialize the game settings."""
        print('Welcome to Tic Tac Toe!')
        self.player_letter = self.input_player_letter()
        self.other_letter = 'O' if self.player_letter == 'X' else 'X'
        self.display_board_positions()

    def input_player_letter(self) -> str:
        """Let player choose X or O."""
        while True:
            choice = input('Do you want to be X or O? ').upper()
            if choice in ['X', 'O']:
                return choice
            print("Please enter either 'X' or 'O'")

    def display_board_positions(self) -> None:
        """Show the position numbers on the board."""
        print('\nBoard positions are numbered as follows:')
        print(' 7 | 8 | 9 ')
        print('-----------')
        print(' 4 | 5 | 6 ')
        print('-----------')
        print(' 1 | 2 | 3 ')
        print()

    def is_winner(self, letter: str) -> bool:
        """Check if the given letter has won."""
        winning_combinations = [
            [7, 8, 9], [4, 5, 6], [1, 2, 3],  # Rows
            [7, 4, 1], [8, 5, 2], [9, 6, 3],  # Columns
            [7, 5, 3], [9, 5, 1]              # Diagonals
        ]
        return any(all(self.board[pos] == letter for pos in combo)
                  for combo in winning_combinations)

    def is_space_free(self, position: int) -> bool:
        """Check if a position is available."""
        return self.board[position] == ' '

    def is_board_full(self) -> bool:
        """Check if the board is full."""
        return ' ' not in self.board[1:]

    def get_player_move(self) -> int:
        """Get and validate player's move."""
        while True:
            try:
                move = int(input('What is your next move? (1-9) '))
                if 1 <= move <= 9 and self.is_space_free(move):
                    return move
                print('That position is either invalid or already taken.')
            except ValueError:
                print('Please enter a number between 1 and 9.')

    def make_move(self, position: int, letter: str) -> None:
        """Place a letter on the board."""
        self.board[position] = letter

    def play_game(self) -> None:
        """Main game loop."""
        self.setup_game()
        current_letter = self.player_letter

        while True:
            self.draw_board()
            position = self.get_player_move()
            self.make_move(position, current_letter)

            if self.is_winner(current_letter):
                self.draw_board()
                print(f'Player {current_letter} has won!')
                break
            
            if self.is_board_full():
                self.draw_board()
                print("It's a tie!")
                break

            current_letter = self.other_letter if current_letter == self.player_letter else self.player_letter

    def play_again(self) -> bool:
        """Ask if players want to play another game."""
        return input('Do you want to play again? (yes/no) ').lower().startswith('y')

def main():
    """Main function to start and manage the Tic Tac Toe game loop."""
    game = TicTacToe()  # Initialize a new game instance
    while True:
        game.play_game()  # Play a single game of Tic Tac Toe
        if not game.play_again():  # Check if players want to play again
            print('Thanks for playing!')
            break  # Exit the loop if the players do not want to play again
        game = TicTacToe()  # Re-initialize the game for a new round

if __name__ == '__main__':
    main()