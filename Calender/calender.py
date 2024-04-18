import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
from datetime import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")

        # Create DateEntry widget
        self.date_entry = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.pack(pady=20)

        # Create button to display selected date
        self.show_date_button = ttk.Button(self.root, text="Show Selected Date", command=self.show_selected_date)
        self.show_date_button.pack(pady=10)

        # Create button to add event
        self.add_event_button = ttk.Button(self.root, text="Add Event", command=self.add_event)
        self.add_event_button.pack(pady=10)

        # Create label to display events
        self.event_label = ttk.Label(self.root, text="")
        self.event_label.pack(pady=20)

        # Initialize events dictionary
        self.events = {}

    def show_selected_date(self):
        selected_date = self.date_entry.get_date()
        self.event_label.config(text=f"Selected Date: {selected_date.strftime('%Y-%m-%d')}\nEvents: {self.events.get(selected_date.strftime('%Y-%m-%d'), 'No events')}")
    
    def add_event(self):
        selected_date = self.date_entry.get_date()
        event = simpledialog.askstring("Add Event", "Enter event:")
        if event:
            self.events[selected_date.strftime('%Y-%m-%d')] = event
            self.event_label.config(text=f"Event added for {selected_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
