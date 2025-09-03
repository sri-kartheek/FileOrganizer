import os
import shutil
from pathlib import Path

# Define categories and file extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        print("⚠️ Folder not found!")
        return

    for file in folder.iterdir():
        if file.is_file():
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if file.suffix.lower() in extensions:
                    category_folder = folder / category
                    category_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), str(category_folder / file.name))
                    print(f"✅ Moved {file.name} → {category}/")
                    moved = True
                    break

            if not moved:  # If no match, move to Others
                other_folder = folder / "Others"
                other_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(other_folder / file.name))
                print(f"📦 Moved {file.name} → Others/")

if __name__ == "__main__":
    path = input("Enter the folder path to organize: ").strip()
    organize_folder(path)
    print("🎉 Folder organized successfully!")
