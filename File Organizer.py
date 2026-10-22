
import os
import shutil

# Folder containing the files to organize
FOLDER_PATH = os.path.join(os.getcwd(), "TestFiles")

# File categories and their extensions
FILE_TYPES = {
    "PDFs": [".pdf"],
    "Word_Files": [".docx", ".doc"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv"],
    "Text_Files": [".txt"]
}

# Check that the test folder exists
if not os.path.isdir(FOLDER_PATH):
    raise FileNotFoundError(
        "TestFiles folder not found. Create it inside FileOrganizer."
    )

# Create category folders inside TestFiles
for folder in FILE_TYPES:
    folder_path = os.path.join(FOLDER_PATH, folder)
    os.makedirs(folder_path, exist_ok=True)

# Organize the files
for file in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    ext = os.path.splitext(file)[1].lower()

    # Move the file into its matching category
    for folder, extensions in FILE_TYPES.items():
        if ext in extensions:
            destination = os.path.join(
                FOLDER_PATH, folder, file
            )
            shutil.move(file_path, destination)
            print(f"Moved {file} to {folder}")
            break

print("File organization completed!")
