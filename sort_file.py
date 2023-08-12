import os
import re
from dotenv import load_dotenv

load_dotenv()

def is_source_code_content(content):
    # Use regular expressions to identify patterns
    pattern = r'\b(html|javascript|python)\b'
    if re.search(pattern, content):
        return True
    return False

def analyze_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read(1024)  # Read the first 1024 bytes of the file
        return is_source_code_content(content)

folder_path = os.getenv("VIRUS_FOLDER_PATH")
potential_source_code_files = []

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        if analyze_file(file_path):
            potential_source_code_files.append(file_path)


# Save the found file paths to filepath.txt
with open('filepath.txt', 'w') as f:
    for file_path in potential_source_code_files:
        f.write(file_path + '\n')

print("File paths saved in filepath.txt")