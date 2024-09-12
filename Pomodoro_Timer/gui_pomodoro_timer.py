import tkinter as tk
from tkinter import messagebox
import time
import threading

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x150")
        
        self.is_running = False
        self.remaining_time = 0
        self.timer_thread = None

        # Define the UI components
        self.time_display = tk.Label(root, text="25:00", font=("Helvetica", 48))
        self.time_display.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.pomodoro_duration = 25 * 60  # 25 minutes in seconds
        self.break_duration = 5 * 60      # 5 minutes in seconds
        self.long_break_duration = 15 * 60 # 15 minutes in seconds
        self.cycle_count = 0
        
        self.update_display()

    def update_display(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        time_str = f"{minutes:02}:{seconds:02}"
        self.time_display.config(text=time_str)

    def start_timer(self):
        if not self.is_running:
            self.remaining_time = self.pomodoro_duration
            self.is_running = True
            self.timer_thread = threading.Thread(target=self.run_timer)
            self.timer_thread.start()

    def stop_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.remaining_time = self.pomodoro_duration
        self.update_display()

    def run_timer(self):
        while self.is_running and self.remaining_time > 0:
            time.sleep(1)
            self.remaining_time -= 1
            self.update_display()
        
        if self.is_running and self.remaining_time <= 0:
            self.cycle_count += 1
            if self.cycle_count % 4 == 0:
                self.remaining_time = self.long_break_duration
                self.show_message("Long Break", "Take a long break!")
            else:
                self.remaining_time = self.break_duration
                self.show_message("Break Time", "Take a short break!")
            self.update_display()

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
