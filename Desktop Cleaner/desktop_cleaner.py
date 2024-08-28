import os
import shutil
from pathlib import Path

# Define the path to the Desktop
desktop_path = Path.home() / "Desktop"

# Define folders for different types of files
folders = {
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".tar", ".gz"],
}

# Create the folders if they do not exist
for folder in folders.keys():
    folder_path = desktop_path / folder
    if not folder_path.exists():
        folder_path.mkdir()

# Iterate through all files on the Desktop
for item in desktop_path.iterdir():
    if item.is_file():
        # Get file extension
        file_extension = item.suffix.lower()
        
        # Determine the correct folder based on the file extension
        for folder, extensions in folders.items():
            if file_extension in extensions:
                destination_folder = desktop_path / folder
                shutil.move(str(item), destination_folder / item.name)
                print(f"Moved {item.name} to {folder}")
                break
