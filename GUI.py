import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        # Create main window
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        # Game variables
        self.current_player = "X"
        self.board = [""] * 9
        
        # Get player names
        self.player1 = input("Enter name for Player 1 (X): ")
        self.player2 = input("Enter name for Player 2 (O): ")
        
        # Create turn label
        self.label = tk.Label(
            self.window,
            text=f"Turn: {self.player1} (X)"
        )
        self.label.pack(pady=10)
        
        # Create game board
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        
        # Create buttons
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.frame,
                    text="",
                    font=('Arial', 20),
                    width=5,
                    height=2,
                    command=lambda x=i, y=j: self.play(x, y)
                )
                button.grid(row=i, column=j)
                self.buttons.append(button)
        
        # Create reset button
        tk.Button(
            self.window,
            text="New Game",
            command=self.reset_game
        ).pack(pady=10)

    def play(self, row, col):
        index = row * 3 + col
        
        # Check if cell is empty
        if self.board[index] == "":
            # Update button and board
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            
            # Check for winner
            if self.check_winner():
                winner = self.player1 if self.current_player == "X" else self.player2
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.reset_game()
            # Check for tie
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            # Switch player
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                current_name = self.player1 if self.current_player == "X" else self.player2
                self.label.config(text=f"Turn: {current_name} ({self.current_player})")

    def check_winner(self):
        # All winning combinations
        wins = [
            [0,1,2], [3,4,5], [6,7,8],  # Rows
            [0,3,6], [1,4,7], [2,5,8],  # Columns
            [0,4,8], [2,4,6]            # Diagonals
        ]
        
        # Check each combination
        for combo in wins:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] != ""):
                return True
        return False

    def reset_game(self):
        # Clear board and reset player
        self.board = [""] * 9
        self.current_player = "X"
        
        # Reset buttons
        for button in self.buttons:
            button.config(text="")
            
        # Reset label
        self.label.config(text=f"Turn: {self.player1} (X)")

    def run(self):
        self.window.mainloop()

# Start game
if __name__ == "__main__":
    game = TicTacToe()
    game.run()