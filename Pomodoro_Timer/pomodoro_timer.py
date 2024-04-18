import tkinter as tk
from tkinter import ttk
import time

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        # Initialize variables
        self.work_duration = 25 * 60  # 25 minutes in seconds
        self.break_duration = 5 * 60  # 5 minutes in seconds
        self.time_remaining = self.work_duration
        self.timer_running = False

        # Create labels
        self.time_label = ttk.Label(root, text=self.format_time(self.time_remaining))
        self.time_label.pack(pady=10)

        # Create buttons
        self.start_button = ttk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)
        self.pause_button = ttk.Button(root, text="Pause", command=self.pause_timer)
        self.pause_button.pack(pady=5)
        self.reset_button = ttk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(pady=5)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def pause_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.time_remaining = self.work_duration
        self.update_time_label()

    def update_timer(self):
        if self.timer_running and self.time_remaining > 0:
            self.time_remaining -= 1
            self.update_time_label()
            self.root.after(1000, self.update_timer)
        elif self.time_remaining == 0:
            self.timer_running = False
            self.root.bell()  # Play system bell sound when timer finishes

    def update_time_label(self):
        self.time_label.config(text=self.format_time(self.time_remaining))

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
