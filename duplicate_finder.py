import os
import hashlib
import shutil

SOURCE_FOLDER = "/path/to/source"
DUPLICATE_FOLDER = "/path/to/folderB"  # Folder B

os.makedirs(DUPLICATE_FOLDER, exist_ok=True)

def file_hash(path):
    hasher = hashlib.md5()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

seen = {}

for root, _, files in os.walk(SOURCE_FOLDER):
    for file in files:
        path = os.path.join(root, file)

        # skip Folder B itself to avoid loops
        if DUPLICATE_FOLDER in path:
            continue

        try:
            h = file_hash(path)

            if h in seen:
                # duplicate → move to Folder B
                target_path = os.path.join(DUPLICATE_FOLDER, file)

                # avoid overwriting if same filename already exists
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(target_path):
                    target_path = os.path.join(DUPLICATE_FOLDER, f"{base}_{counter}{ext}")
                    counter += 1

                shutil.move(path, target_path)
                print(f"Moved duplicate: {path} → {target_path}")

            else:
                seen[h] = path
                print(f"Keeping original: {path}")

        except Exception as e:
            print(f"Error with {path}: {e}")

print("Done scanning duplicates.")