import tkinter as tk
from tkinter import ttk, messagebox
import feedparser

class RSSReader:
    def __init__(self, root):
        self.root = root
        self.root.title("RSS Feed Reader")

        # Create combobox to select RSS feed
        self.feed_urls = {
            "BBC News": "http://feeds.bbci.co.uk/news/rss.xml",
            "CNN": "http://rss.cnn.com/rss/edition.rss",
            "TechCrunch": "https://techcrunch.com/feed/",
            "NASA": "https://www.nasa.gov/rss/dyn/breaking_news.rss"
        }
        self.feed_combo = ttk.Combobox(root, values=list(self.feed_urls.keys()))
        self.feed_combo.set("Select Feed")
        self.feed_combo.pack(pady=20)

        # Create button to fetch and display feed
        self.fetch_button = ttk.Button(root, text="Fetch Feed", command=self.fetch_feed)
        self.fetch_button.pack(pady=10)

        # Create listbox to display feed items
        self.feed_listbox = tk.Listbox(root, width=100, height=20)
        self.feed_listbox.pack(pady=20)

        # Create scrollbar for listbox
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.feed_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.feed_listbox.config(yscrollcommand=self.scrollbar.set)

    def fetch_feed(self):
        selected_feed = self.feed_combo.get()
        feed_url = self.feed_urls.get(selected_feed)

        if not feed_url:
            messagebox.showwarning("Warning", "Please select a feed!")
            return

        try:
            feed = feedparser.parse(feed_url)
            self.display_feed(feed)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch feed: {e}")

    def display_feed(self, feed):
        self.feed_listbox.delete(0, tk.END)
        
        if "entries" in feed:
            for entry in feed.entries:
                title = entry.title
                link = entry.link
                self.feed_listbox.insert(tk.END, f"{title} - {link}")
        else:
            messagebox.showinfo("Info", "No feed items found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = RSSReader(root)
    root.mainloop()
