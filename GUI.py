import tkinter as tk

def draw_grid():
    for column in range(3):
        for row in range(3):
            button = tk.Button(root, text="X", font=("Arial", 100))
            button.grid(row=row, column=column)

# Création de la fenetre du jeu
root = tk.Tk()

# Personnalisation de la fenetre
root.title("Morpion")
root.minsize(500, 500)
root.mainloop()