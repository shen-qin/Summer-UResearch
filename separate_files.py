import os
import shutil

source_folder = ''
destination_folder = ''

# Get all files in the source folder
files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# Create new folders and move files
folder_count = 1
file_count = 0

# Make sure the destination folder exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

current_folder_path = os.path.join(destination_folder, f"folder_{folder_count}")

for file in files:
    # Create a new folder if the limit is reached
    if file_count % 2000 == 0:
        current_folder_path = os.path.join(destination_folder, f"folder_{folder_count}")
        
        if not os.path.exists(current_folder_path):
            os.makedirs(current_folder_path)
        
        folder_count += 1

    # Move file to the current folder
    shutil.move(os.path.join(source_folder, file), current_folder_path)
    
    file_count += 1

print("Files divided successfully!")
