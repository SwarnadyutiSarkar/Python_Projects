import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class PortfolioAnalyzer:
    def __init__(self, master):
        self.master = master
        master.title("Financial Portfolio Analyzer")

        self.assets = []
        self.values = []

        # Labels
        self.label = tk.Label(master, text="Enter Your Investment Portfolio")
        self.label.pack()

        # Asset Name
        self.asset_label = tk.Label(master, text="Asset Name:")
        self.asset_label.pack()
        self.asset_entry = tk.Entry(master)
        self.asset_entry.pack()

        # Asset Value
        self.value_label = tk.Label(master, text="Asset Value ($):")
        self.value_label.pack()
        self.value_entry = tk.Entry(master)
        self.value_entry.pack()

        # Add Asset Button
        self.add_asset_button = tk.Button(master, text="Add Asset", command=self.add_asset)
        self.add_asset_button.pack()

        # Show Allocation Button
        self.show_allocation_button = tk.Button(master, text="Show Asset Allocation", command=self.show_allocation)
        self.show_allocation_button.pack()

    def add_asset(self):
        asset_name = self.asset_entry.get()
        asset_value = self.value_entry.get()

        if asset_name and asset_value.replace('.', '', 1).isdigit():
            self.assets.append(asset_name)
            self.values.append(float(asset_value))

            messagebox.showinfo("Success", f"Added asset: {asset_name} with value: ${asset_value}.")
            self.asset_entry.delete(0, tk.END)
            self.value_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a valid asset name and value.")

    def show_allocation(self):
        if not self.assets:
            messagebox.showwarning("No Data", "No assets logged.")
            return

        # Plotting asset allocation
        plt.figure(figsize=(10, 6))
        plt.pie(self.values, labels=self.assets, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Asset Allocation of Investment Portfolio')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    portfolio_analyzer = PortfolioAnalyzer(root)
    root.mainloop()
