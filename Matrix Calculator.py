import numpy as np
from tkinter import Tk, Label, Button, Entry, Text, Scrollbar, messagebox, END

class MatrixCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Matrix Calculator")

        self.label_a = Label(master, text="Matrix A (comma separated values):")
        self.label_a.pack()
        self.entry_a = Entry(master, width=50)
        self.entry_a.pack()

        self.label_b = Label(master, text="Matrix B (comma separated values):")
        self.label_b.pack()
        self.entry_b = Entry(master, width=50)
        self.entry_b.pack()

        self.result_text = Text(master, height=10, width=50)
        self.result_text.pack()
        self.scrollbar = Scrollbar(master, command=self.result_text.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.result_text.config(yscrollcommand=self.scrollbar.set)

        self.add_button = Button(master, text="Add", command=self.add_matrices)
        self.add_button.pack()

        self.subtract_button = Button(master, text="Subtract", command=self.subtract_matrices)
        self.subtract_button.pack()

        self.multiply_button = Button(master, text="Multiply", command=self.multiply_matrices)
        self.multiply_button.pack()

        self.invert_button = Button(master, text="Invert A", command=self.invert_matrix)
        self.invert_button.pack()

    def get_matrix(self, entry):
        try:
            matrix = np.array([[float(num) for num in row.split(',')] for row in entry.split(';')])
            return matrix
        except Exception as e:
            messagebox.showerror("Input Error", "Invalid matrix input. Please use the correct format.")
            return None

    def add_matrices(self):
        a = self.get_matrix(self.entry_a.get())
        b = self.get_matrix(self.entry_b.get())
        if a is not None and b is not None:
            try:
                result = np.add(a, b)
                self.display_result(result)
            except ValueError:
                messagebox.showerror("Matrix Error", "Matrices must have the same dimensions for addition.")

    def subtract_matrices(self):
        a = self.get_matrix(self.entry_a.get())
        b = self.get_matrix(self.entry_b.get())
        if a is not None and b is not None:
            try:
                result = np.subtract(a, b)
                self.display_result(result)
            except ValueError:
                messagebox.showerror("Matrix Error", "Matrices must have the same dimensions for subtraction.")

    def multiply_matrices(self):
        a = self.get_matrix(self.entry_a.get())
        b = self.get_matrix(self.entry_b.get())
        if a is not None and b is not None:
            try:
                result = np.dot(a, b)
                self.display_result(result)
            except ValueError:
                messagebox.showerror("Matrix Error", "Incompatible dimensions for multiplication.")

    def invert_matrix(self):
        a = self.get_matrix(self.entry_a.get())
        if a is not None:
            try:
                result = np.linalg.inv(a)
                self.display_result(result)
            except np.linalg.LinAlgError:
                messagebox.showerror("Matrix Error", "Matrix A is not invertible.")

    def display_result(self, result):
        self.result_text.delete(1.0, END)
        self.result_text.insert(END, str(result))

if __name__ == "__main__":
    root = Tk()
    app = MatrixCalculator(root)
    root.mainloop()
