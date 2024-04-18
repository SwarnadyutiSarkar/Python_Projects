import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class RecipeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe App")

        # Create menu bar
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Load Recipes", command=self.load_recipes)
        self.file_menu.add_command(label="Save Recipes", command=self.save_recipes)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

        # Create search bar
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.root, textvariable=self.search_var)
        self.search_entry.pack(pady=10)
        self.search_entry.bind("<KeyRelease>", self.search_recipes)

        # Create listbox for recipes
        self.recipe_listbox = tk.Listbox(self.root, width=50, height=15)
        self.recipe_listbox.pack(pady=10)

        # Create text widget for recipe details
        self.recipe_text = tk.Text(self.root, width=50, height=10)
        self.recipe_text.pack(pady=10)

        # Initialize recipes
        self.recipes = []

    def load_recipes(self):
        file_path = tk.filedialog.askopenfilename(filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.recipes = json.load(file)
            self.update_recipe_listbox()

    def save_recipes(self):
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                json.dump(self.recipes, file)

    def exit_app(self):
        self.root.quit()

    def search_recipes(self, event=None):
        search_term = self.search_var.get().lower()
        filtered_recipes = [recipe for recipe in self.recipes if search_term in recipe["name"].lower()]
        self.update_recipe_listbox(filtered_recipes)

    def update_recipe_listbox(self, recipes=None):
        self.recipe_listbox.delete(0, tk.END)
        if recipes is None:
            recipes = self.recipes
        for recipe in recipes:
            self.recipe_listbox.insert(tk.END, recipe["name"])

    def show_recipe_details(self, event):
        selected_index = self.recipe_listbox.curselection()
        if selected_index:
            recipe = self.recipes[selected_index[0]]
            self.recipe_text.delete(1.0, tk.END)
            self.recipe_text.insert(tk.END, f"Name: {recipe['name']}\n\nIngredients:\n{', '.join(recipe['ingredients'])}\n\nInstructions:\n{recipe['instructions']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()
