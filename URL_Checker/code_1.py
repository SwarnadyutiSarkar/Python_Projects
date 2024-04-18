import tkinter as tk
from tkinter import ttk, messagebox
import requests
import time

class URLChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Checker")

        # Create label and entry for URL
        ttk.Label(root, text="Enter URL:").pack(pady=10)
        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.pack(pady=10)

        # Create button to check URL
        self.check_button = ttk.Button(root, text="Check URL", command=self.check_url)
        self.check_button.pack(pady=20)

        # Create text widget to display results
        self.result_text = tk.Text(root, width=60, height=10)
        self.result_text.pack(pady=20)

    def check_url(self):
        url = self.url_entry.get()

        if not url:
            messagebox.showwarning("Warning", "Please enter a URL!")
            return

        try:
            start_time = time.time()
            response = requests.get(url, timeout=10)
            end_time = time.time()

            response_time = round(end_time - start_time, 2)

            if response.status_code == 200:
                status = "Available"
            else:
                status = "Not Available"

            result = f"Status: {status}\nResponse Time: {response_time} seconds\n"
            result += f"Response Code: {response.status_code}\n"
            result += f"Content Type: {response.headers.get('Content-Type', 'Unknown')}\n"
            result += f"Content Length: {response.headers.get('Content-Length', 'Unknown')} bytes"

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)

        except requests.RequestException as e:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Error: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = URLChecker(root)
    root.mainloop()
 