# Read the file paths from filepath.txt
with open('file_name.txt', 'r') as f:
    file_paths = f.read().splitlines()

# Sort the file paths
sorted_file_paths = sorted(file_paths)

# Write the sorted file paths back to filepath.txt
with open('file_name.txt', 'w') as f:
    for file_path in sorted_file_paths:
        f.write(file_path + '\n')

print("File paths sorted in filepath.txt")
