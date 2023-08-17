import os
import shutil

# 1. Read the valid file paths from the .txt file
with open('analysis_ids.txt', 'r') as f:
    valid_files = {line.split(':')[0].strip() for line in f}  # Extract path before the colon

# 2. List all files in the target directory
target_directory = ''
all_files = {os.path.join(target_directory, file_name) for file_name in os.listdir(target_directory) if os.path.isfile(os.path.join(target_directory, file_name))}

# 3. Prepare the destination folder
destination_folder = os.path.join(target_directory, '')
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 4. Compare and move files not in the valid list
for file_path in all_files:
    if file_path not in valid_files:
        print(f"Moving: {file_path}")
        shutil.move(file_path, destination_folder)

print("Files moved successfully!")
