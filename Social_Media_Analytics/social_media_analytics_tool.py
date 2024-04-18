import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np

class SocialMediaAnalyticsTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Media Analytics Tool")

        # Create menu bar
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Load Data", command=self.load_data)
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

        # Create buttons
        self.analyze_button = ttk.Button(root, text="Analyze Data", command=self.analyze_data)
        self.analyze_button.pack(pady=20)

        # Initialize data
        self.data = {"Posts": 100, "Likes": 200, "Comments": 50, "Shares": 30, "Followers": 5000}

    def load_data(self):
        # Simulate loading data from social media API
        # Replace with actual implementation to fetch data from social media API
        self.data = {"Posts": 100, "Likes": 200, "Comments": 50, "Shares": 30, "Followers": 5000}
        messagebox.showinfo("Info", "Data loaded successfully!")

    def exit_app(self):
        self.root.quit()

    def analyze_data(self):
        # Create bar chart
        categories = list(self.data.keys())
        values = list(self.data.values())

        plt.figure(figsize=(10, 6))
        plt.bar(categories, values, color='blue')
        plt.xlabel('Metrics')
        plt.ylabel('Values')
        plt.title('Social Media Analytics')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = SocialMediaAnalyticsTool(root)
    root.mainloop()
