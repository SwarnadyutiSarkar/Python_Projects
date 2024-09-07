import tkinter as tk
from tkinter import scrolledtext
from spellchecker import SpellChecker

class SpellingCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Spelling Checker")

        self.spell = SpellChecker()

        # Create the text area
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=80)
        self.text_area.pack(padx=10, pady=10)
        self.text_area.bind("<KeyRelease>", self.check_spelling)

        self.status_label = tk.Label(root, text="", relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def check_spelling(self, event=None):
        content = self.text_area.get("1.0", tk.END)
        words = content.split()

        misspelled = self.spell.unknown(words)

        # Highlight misspelled words
        self.text_area.tag_remove("misspelled", "1.0", tk.END)
        for word in misspelled:
            start_index = "1.0"
            while True:
                start_index = self.text_area.search(word, start_index, stopindex=tk.END)
                if not start_index:
                    break
                end_index = f"{start_index}+{len(word)}c"
                self.text_area.tag_add("misspelled", start_index, end_index)
                start_index = end_index

            self.text_area.tag_config("misspelled", background="yellow")

        # Update status
        self.status_label.config(text=f"Misspelled words: {', '.join(misspelled) if misspelled else 'None'}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellingCheckerApp(root)
    root.mainloop()
