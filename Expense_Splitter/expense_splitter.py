import tkinter as tk
from tkinter import ttk, messagebox

class ExpenseSplitter:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Splitter")

        # Create variables
        self.total_expense_var = tk.DoubleVar()
        self.users_var = tk.StringVar(value="Alice, Bob, Charlie")
        self.expense_var = tk.StringVar()

        # Create labels
        ttk.Label(root, text="Total Expense:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Label(root, text="Users:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        ttk.Label(root, text="Expense (e.g., 100 for equal split or 100,50,30 for custom split):").grid(row=2, column=0, padx=5, pady=5, sticky="e")

        # Create entry widgets
        self.total_expense_entry = ttk.Entry(root, textvariable=self.total_expense_var)
        self.total_expense_entry.grid(row=0, column=1, padx=5, pady=5)
        self.users_entry = ttk.Entry(root, textvariable=self.users_var)
        self.users_entry.grid(row=1, column=1, padx=5, pady=5)
        self.expense_entry = ttk.Entry(root, textvariable=self.expense_var)
        self.expense_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create calculate button
        self.calculate_button = ttk.Button(root, text="Calculate", command=self.calculate_expense)
        self.calculate_button.grid(row=3, columnspan=2, padx=5, pady=5)

        # Create text widget for results
        self.result_text = tk.Text(root, width=40, height=10)
        self.result_text.grid(row=4, columnspan=2, padx=5, pady=5)

    def calculate_expense(self):
        total_expense = self.total_expense_var.get()
        users = self.users_var.get().split(",")
        expense_str = self.expense_var.get()
        expenses = [float(expense) for expense in expense_str.split(",")]

        if len(users) != len(expenses):
            messagebox.showerror("Error", "Number of users and expenses must match!")
            return

        total_expense_actual = sum(expenses)
        if total_expense_actual != total_expense:
            messagebox.showerror("Error", f"Total expense should be {total_expense_actual}!")
            return

        share_per_user = total_expense_actual / len(users)
        results = []

        for user, expense in zip(users, expenses):
            share_diff = expense - share_per_user
            if share_diff == 0:
                result = f"{user}: No additional payment needed\n"
            elif share_diff > 0:
                result = f"{user}: Owes {share_diff:.2f}\n"
            else:
                result = f"{user}: Will receive {-share_diff:.2f}\n"
            results.append(result)

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "".join(results))

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseSplitter(root)
    root.mainloop()
