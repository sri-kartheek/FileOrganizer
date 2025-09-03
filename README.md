# 🗂️ File Organizer (Python)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange.svg)](https://github.com/yourusername/file-organizer/issues)
A Python automation script that **organizes files in a folder** into subfolders based on their type (Images, Documents, Music, Videos, Code, etc.). Keeps your **Downloads, Desktop, or any directory** neat and structured.

## 🚀 Features
- Automatically sorts files into categories based on extensions.
- Creates subfolders if they don’t exist.
- Works on any folder you provide (Downloads, Desktop, etc.).
- Handles uncategorized files by moving them into an Others/ folder.
- Supports most common file types (PDF, DOCX, MP3, MP4, PNG, ZIP, etc.).

## 📂 Project Structure
file-organizer/  
│── file_organizer.py # Main Python script
│── README.md # Project documentation
│── LICENSE # MIT License

## ▶️ Example Run
**Before running the script (`Downloads/` folder):**
photo.jpg
resume.pdf
song.mp3
script.py
movie.mkv

**After running the script:**
Downloads/
├── Images/
│ └── photo.jpg
├── Documents/
│ └── resume.pdf
├── Music/
│ └── song.mp3
├── Code/
│ └── script.py
├── Videos/
│ └── movie.mkv


## 💻 Usage
1. Clone the repository  


git clone https://github.com/yourusername/file-organizer.git

cd file-organizer


2. Run the program  


python file_organizer.py


3. Enter the folder path when prompted  
Example:  


Enter the folder path to organize: C:\Users\YourName\Downloads


## 📘 Concepts Used
- os → File and folder operations
- shutil → Moving files
- pathlib → Clean path handling

## ✨ Future Improvements
- Add scheduling to auto-organize Downloads/Desktop at intervals.
- Add a configuration file (config.json) for custom categories.
- Add GUI for non-technical users.

## 👨‍💻 Author
**Sri Kartheek**  
- 🌐 https://www.linkedin.com/in/vinathi-chitturi-147669255/  
- 💻 Python Developer | Problem Solver | Automation Enthusiast  

## 📜 License
This project is licensed under the MIT License.
