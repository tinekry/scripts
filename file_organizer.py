import os
import shutil

FOLDER = "/path/to/your/folder"

file_types = {
    "Images": [".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

for file in os.listdir(FOLDER):
    file_path = os.path.join(FOLDER, file)

    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()

        for folder, extensions in file_types.items():
            if ext in extensions:
                target_folder = os.path.join(FOLDER, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, file))
                break

print("Done organizing!")