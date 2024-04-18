import tkinter as tk
from tkinter import ttk, messagebox

class PersonalBudgetPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Budget Planner")

        # Initialize variables
        self.income_entries = []
        self.expense_entries = []

        # Create income section
        ttk.Label(root, text="Income").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ttk.Button(root, text="Add Income", command=self.add_income).grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Create expense section
        ttk.Label(root, text="Expenses").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        ttk.Button(root, text="Add Expense", command=self.add_expense).grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # Create calculate button
        ttk.Button(root, text="Calculate", command=self.calculate_budget).grid(row=2, columnspan=2, padx=10, pady=10)

        # Create budget summary text widget
        self.summary_text = tk.Text(root, width=50, height=10)
        self.summary_text.grid(row=3, columnspan=2, padx=10, pady=10)

    def add_income(self):
        income_frame = ttk.Frame(self.root)
        income_frame.grid(row=len(self.income_entries) + 1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        income_label = ttk.Label(income_frame, text="Description:")
        income_label.grid(row=0, column=0, padx=5, pady=5)
        income_entry = ttk.Entry(income_frame)
        income_entry.grid(row=0, column=1, padx=5, pady=5)

        income_label = ttk.Label(income_frame, text="Amount:")
        income_label.grid(row=0, column=2, padx=5, pady=5)
        income_amount = ttk.Entry(income_frame)
        income_amount.grid(row=0, column=3, padx=5, pady=5)

        self.income_entries.append((income_entry, income_amount))

    def add_expense(self):
        expense_frame = ttk.Frame(self.root)
        expense_frame.grid(row=len(self.expense_entries) + len(self.income_entries) + 2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        expense_label = ttk.Label(expense_frame, text="Description:")
        expense_label.grid(row=0, column=0, padx=5, pady=5)
        expense_entry = ttk.Entry(expense_frame)
        expense_entry.grid(row=0, column=1, padx=5, pady=5)

        expense_label = ttk.Label(expense_frame, text="Amount:")
        expense_label.grid(row=0, column=2, padx=5, pady=5)
        expense_amount = ttk.Entry(expense_frame)
        expense_amount.grid(row=0, column=3, padx=5, pady=5)

        self.expense_entries.append((expense_entry, expense_amount))

    def calculate_budget(self):
        total_income = sum(float(entry[1].get()) for entry in self.income_entries if entry[1].get())
        total_expense = sum(float(entry[1].get()) for entry in self.expense_entries if entry[1].get())
        net_income = total_income - total_expense

        summary = f"Total Income: ${total_income:.2f}\n"
        summary += f"Total Expenses: ${total_expense:.2f}\n"
        summary += f"Net Income: ${net_income:.2f}\n"

        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(tk.END, summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalBudgetPlanner(root)
    root.mainloop()
