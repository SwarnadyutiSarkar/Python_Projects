import tkinter as tk
from tkinter import messagebox
import time
import threading
import pygame
import random

# Initialize Pygame for sound playback
pygame.mixer.init()

# Load soothing sound (replace with your own sound file)
pygame.mixer.music.load("path_to_your_soothing_sound.mp3")

# List of motivational quotes
quotes = [
    "Peace comes from within. Do not seek it without.",
    "The mind is everything. What you think you become.",
    "You, yourself, as much as anybody in the entire universe, deserve your love and affection.",
    "Meditation is not about stopping thoughts, but recognizing that we are more than our thoughts and our feelings.",
    "In the silence of meditation, you find your true self.",
    "Meditation brings wisdom; lack of meditation leaves ignorance. Know well what leads you forward and what holds you back.",
    "The quieter you become, the more you can hear."
]

class MeditationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meditation App")
        self.root.geometry("400x300")
        
        self.time_var = tk.StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self.root, text="Set Meditation Timer (minutes):", font=("Helvetica", 12)).pack(pady=10)
        
        self.time_entry = tk.Entry(self.root, textvariable=self.time_var, font=("Helvetica", 12))
        self.time_entry.pack(pady=5)
        
        self.start_button = tk.Button(self.root, text="Start Meditation", command=self.start_meditation, font=("Helvetica", 12), bg="green", fg="white")
        self.start_button.pack(pady=20)
        
        self.quote_label = tk.Label(self.root, text="", font=("Helvetica", 10), wraplength=350, justify="center")
        self.quote_label.pack(pady=20)
        
    def start_meditation(self):
        try:
            minutes = int(self.time_var.get())
            if minutes <= 0:
                raise ValueError("Time must be positive.")
            self.start_button.config(state="disabled")
            self.quote_label.config(text=random.choice(quotes))
            threading.Thread(target=self.run_timer, args=(minutes,)).start()
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
        
    def run_timer(self, minutes):
        seconds = minutes * 60
        pygame.mixer.music.play(-1)  # Loop the soothing sound
        
        for _ in range(seconds):
            time.sleep(1)
            
        pygame.mixer.music.stop()
        messagebox.showinfo("Meditation Complete", "Your meditation session has ended.")
        self.start_button.config(state="normal")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = MeditationApp(root)
    root.mainloop()
