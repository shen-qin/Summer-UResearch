import os
import shutil
from dotenv import load_dotenv

load_dotenv()

# Path to the folder containing the files
source_folder = os.getenv("VIRUS_FOLDER_PATH")

# Read the file paths from filepath.txt
with open('filepath.txt', 'r') as f:
    file_paths = f.read().splitlines()

# Create the "Sorted VirusShare" folder if it doesn't exist
destination_folder = os.getenv("SORTED_VIRUS_FOLDER_PATH")
os.makedirs(destination_folder, exist_ok=True)

# Move the files to the destination folder
for file_path in file_paths:
    file_name = os.path.basename(file_path)
    destination_path = os.path.join(destination_folder, file_name)
    shutil.move(file_path, destination_path)

print("Files moved to the 'Sorted VirusShare' folder.")
