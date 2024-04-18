import tkinter as tk
from tkinter import ttk

class SearchEngine:
    def __init__(self, root):
        self.root = root
        self.root.title("Search Engine")

        # Initialize documents
        self.documents = [
            "This is document 1.",
            "Here is document 2.",
            "Another document 3 is here."
        ]

        # Create search input and button
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(root, textvariable=self.search_var, width=50)
        self.search_entry.pack(pady=20)
        self.search_button = ttk.Button(root, text="Search", command=self.search_documents)
        self.search_button.pack(pady=10)

        # Create search results text widget
        self.results_text = tk.Text(root, width=50, height=10)
        self.results_text.pack(pady=20)

    def search_documents(self):
        query = self.search_var.get().lower()
        results = []

        for idx, document in enumerate(self.documents, 1):
            if query in document.lower():
                results.append(f"Document {idx}: {document}")

        if results:
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "\n".join(results))
        else:
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "No matching documents found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SearchEngine(root)
    root.mainloop()
