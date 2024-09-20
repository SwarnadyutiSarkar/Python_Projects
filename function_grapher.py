import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp

class FunctionGrapherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mathematical Function Grapher")

        # Create and configure the main frame
        self.frame = ttk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Function entry
        self.function_label = ttk.Label(self.frame, text="Enter Function (in x):")
        self.function_label.grid(row=0, column=0, padx=5, pady=5)

        self.function_entry = ttk.Entry(self.frame)
        self.function_entry.grid(row=0, column=1, padx=5, pady=5)

        # Plot button
        self.plot_btn = ttk.Button(self.frame, text="Plot Graph", command=self.plot_function)
        self.plot_btn.grid(row=0, column=2, padx=5, pady=5)

        # Matplotlib Figure
        self.figure = plt.Figure(figsize=(8, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)

        # Canvas for Matplotlib
        self.canvas = FigureCanvasTkAgg(self.figure, self.frame)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3)

    def plot_function(self):
        function_str = self.function_entry.get().strip()
        if not function_str:
            messagebox.showwarning("Input Error", "Please enter a function.")
            return

        # Create a symbolic variable and function
        x = sp.symbols('x')
        try:
            # Convert the string to a sympy function
            function = sp.sympify(function_str)
            # Create a numpy-friendly function
            func = sp.lambdify(x, function, 'numpy')

            # Generate x values
            x_vals = np.linspace(-10, 10, 400)
            y_vals = func(x_vals)

            # Clear previous plot
            self.ax.clear()
            self.ax.plot(x_vals, y_vals, label=str(function))
            self.ax.set_title(f'Graph of {function}')
            self.ax.set_xlabel('x')
            self.ax.set_ylabel('f(x)')
            self.ax.axhline(0, color='black',linewidth=0.5, ls='--')
            self.ax.axvline(0, color='black',linewidth=0.5, ls='--')
            self.ax.grid()
            self.ax.legend()
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"Invalid function: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FunctionGrapherApp(root)
    root.mainloop()
