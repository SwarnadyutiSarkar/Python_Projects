import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pygame
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        # Initialize pygame mixer
        pygame.mixer.init()

        # Create playlist
        self.playlist = []

        # Create buttons
        self.add_button = ttk.Button(root, text="Add Song", command=self.add_song)
        self.add_button.pack(pady=20)
        self.play_button = ttk.Button(root, text="Play", command=self.play_song)
        self.play_button.pack(pady=20)
        self.pause_button = ttk.Button(root, text="Pause", command=self.pause_song)
        self.pause_button.pack(pady=20)
        self.stop_button = ttk.Button(root, text="Stop", command=self.stop_song)
        self.stop_button.pack(pady=20)
        self.next_button = ttk.Button(root, text="Next", command=self.next_song)
        self.next_button.pack(pady=20)
        self.prev_button = ttk.Button(root, text="Previous", command=self.prev_song)
        self.prev_button.pack(pady=20)

        # Create playlist listbox
        self.playlist_listbox = tk.Listbox(root, width=50, height=10)
        self.playlist_listbox.pack(pady=20)

    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3"), ("WAV Files", "*.wav"), ("All Files", "*.*")])
        if song_path:
            self.playlist.append(song_path)
            song_name = os.path.basename(song_path)
            self.playlist_listbox.insert(tk.END, song_name)

    def play_song(self):
        selected_song = self.playlist_listbox.curselection()
        if selected_song:
            song_path = self.playlist[selected_song[0]]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

    def pause_song(self):
        pygame.mixer.music.pause()

    def stop_song(self):
        pygame.mixer.music.stop()

    def next_song(self):
        selected_song = self.playlist_listbox.curselection()
        if selected_song:
            next_song_index = (selected_song[0] + 1) % len(self.playlist)
            self.playlist_listbox.selection_clear(0, tk.END)
            self.playlist_listbox.selection_set(next_song_index)
            self.playlist_listbox.activate(next_song_index)
            self.play_song()

    def prev_song(self):
        selected_song = self.playlist_listbox.curselection()
        if selected_song:
            prev_song_index = (selected_song[0] - 1) % len(self.playlist)
            self.playlist_listbox.selection_clear(0, tk.END)
            self.playlist_listbox.selection_set(prev_song_index)
            self.playlist_listbox.activate(prev_song_index)
            self.play_song()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
