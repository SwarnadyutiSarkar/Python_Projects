import tkinter as tk
from tkinter import ttk, messagebox

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        # Create entry grid
        self.entries = []
        for i in range(9):
            row = []
            for j in range(9):
                entry = ttk.Entry(root, width=5)
                entry.grid(row=i, column=j)
                row.append(entry)
            self.entries.append(row)

        # Create solve button
        self.solve_button = ttk.Button(root, text="Solve", command=self.solve_sudoku)
        self.solve_button.grid(row=9, columnspan=9)

    def solve_sudoku(self):
        board = [[0 if entry.get() == '' else int(entry.get()) for entry in row] for row in self.entries]
        
        if self.solve(board):
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(board[i][j]))
        else:
            messagebox.showinfo("Info", "No solution found!")

    def find_empty_cell(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def is_valid(self, board, num, pos):
        # Check row
        if num in board[pos[0]]:
            return False

        # Check column
        if num in [board[i][pos[1]] for i in range(9)]:
            return False

        # Check 3x3 box
        box_row, box_col = 3 * (pos[0] // 3), 3 * (pos[1] // 3)
        if num in [board[i][j] for i in range(box_row, box_row + 3) for j in range(box_col, box_col + 3)]:
            return False

        return True

    def solve(self, board):
        empty_cell = self.find_empty_cell(board)
        
        if not empty_cell:
            return True
        
        row, col = empty_cell
        
        for num in range(1, 10):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num
                
                if self.solve(board):
                    return True
                
                board[row][col] = 0
                
        return False

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
