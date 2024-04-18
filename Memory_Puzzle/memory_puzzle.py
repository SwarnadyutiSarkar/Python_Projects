import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

class MemoryPuzzle:
    def __init__(self, root, rows=4, cols=4):
        self.root = root
        self.root.title("Memory Puzzle")

        self.rows = rows
        self.cols = cols

        # Create buttons
        self.start_button = ttk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=20)

        # Create canvas for grid
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack(pady=20)

        # Initialize game variables
        self.cards = []
        self.card_values = []
        self.selected_cards = []
        self.moves = 0
        self.start_time = None

    def start_game(self):
        # Clear canvas
        self.canvas.delete("all")

        # Reset game variables
        self.cards = []
        self.card_values = []
        self.selected_cards = []
        self.moves = 0

        # Generate card values
        values = [str(i) for i in range(1, (self.rows * self.cols) // 2 + 1)]
        self.card_values = values + values
        random.shuffle(self.card_values)

        # Create cards
        card_width = 80
        card_height = 80
        for i in range(self.rows):
            for j in range(self.cols):
                x1 = j * card_width + 10
                y1 = i * card_height + 10
                x2 = x1 + card_width
                y2 = y1 + card_height
                card = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", tags="card")
                self.cards.append(card)
                self.canvas.tag_bind(card, "<Button-1>", lambda e, i=i, j=j: self.select_card(i, j))

        # Start timer
        self.start_time = time.time()

    def select_card(self, i, j):
        if len(self.selected_cards) < 2:
            index = i * self.cols + j
            card = self.cards[index]
            value = self.card_values[index]
            
            if card not in self.selected_cards:
                self.canvas.itemconfig(card, fill="white", tags="card_selected")
                self.selected_cards.append(card)

                if len(self.selected_cards) == 2:
                    self.root.after(1000, self.check_match)

    def check_match(self):
        card1, card2 = self.selected_cards
        index1 = self.cards.index(card1)
        index2 = self.cards.index(card2)

        if self.card_values[index1] == self.card_values[index2]:
            self.canvas.itemconfig(card1, fill="green", tags="card_matched")
            self.canvas.itemconfig(card2, fill="green", tags="card_matched")
        else:
            self.canvas.itemconfig(card1, fill="blue", tags="card")
            self.canvas.itemconfig(card2, fill="blue", tags="card")

        self.selected_cards.clear()
        self.moves += 1

        if all(self.canvas.gettags(card)[0] == "card_matched" for card in self.cards):
            elapsed_time = time.time() - self.start_time
            messagebox.showinfo("Congratulations", f"Congratulations! You completed the game in {self.moves} moves and {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryPuzzle(root)
    root.mainloop()
