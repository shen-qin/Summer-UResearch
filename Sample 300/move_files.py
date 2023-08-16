import os
import shutil
from dotenv import load_dotenv

load_dotenv()

def copy_files_from_list(file_list_path, destination_folder):
    with open(file_list_path, 'r') as file:
        file_paths = file.readlines()
    
    file_paths = [path.strip() for path in file_paths if path.strip()]  # Remove empty lines and whitespace
    
    for source_path in file_paths:
        try:
            shutil.copy(source_path, destination_folder)
            print(f"Successfully copied {source_path} to {destination_folder}")
        except Exception as e:
            print(f"Error copying {source_path}: {e}")

if __name__ == "__main__":
    source_list_path = os.getenv("SAMPLE_FILE_PATH")
    destination_folder = os.getenv("SAMPLES")
    
    copy_files_from_list(source_list_path, destination_folder)
