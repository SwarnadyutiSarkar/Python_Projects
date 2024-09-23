import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

class LinearRegressionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Linear Regression Tool")

        self.data_x = []
        self.data_y = []

        # Input for X values
        Label(root, text="Enter X values (comma-separated):").pack(pady=5)
        self.x_entry = Entry(root)
        self.x_entry.pack(pady=5)

        # Input for Y values
        Label(root, text="Enter Y values (comma-separated):").pack(pady=5)
        self.y_entry = Entry(root)
        self.y_entry.pack(pady=5)

        # Run Regression Button
        self.regression_button = Button(root, text="Run Linear Regression", command=self.run_regression)
        self.regression_button.pack(pady=10)

    def run_regression(self):
        # Clear previous data
        self.data_x.clear()
        self.data_y.clear()

        try:
            # Parse input data
            self.data_x = list(map(float, self.x_entry.get().split(',')))
            self.data_y = list(map(float, self.y_entry.get().split(',')))

            if len(self.data_x) != len(self.data_y):
                raise ValueError("X and Y must have the same number of elements.")

            # Convert to numpy arrays
            X = np.array(self.data_x)
            Y = np.array(self.data_y)

            # Perform linear regression
            A = np.vstack([X, np.ones(len(X))]).T
            m, c = np.linalg.lstsq(A, Y, rcond=None)[0]

            # Calculate R²
            Y_pred = m * X + c
            r_squared = 1 - (np.sum((Y - Y_pred) ** 2) / np.sum((Y - np.mean(Y)) ** 2))

            # Visualize results
            self.plot_results(X, Y, m, c, r_squared)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def plot_results(self, X, Y, m, c, r_squared):
        plt.figure(figsize=(10, 6))
        plt.scatter(X, Y, color='blue', label='Data points')
        plt.plot(X, m * X + c, color='red', label=f'Regression Line: y={m:.2f}x + {c:.2f}')
        plt.title(f'Linear Regression (R² = {r_squared:.2f})')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    root = Tk()
    app = LinearRegressionTool(root)
    root.mainloop()
