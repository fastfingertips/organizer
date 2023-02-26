import os
import shutil
from datetime import datetime

import file_organizer_log as log

# Function to organize files by date
def organize_files_by_date(folder_path):
    base_path = folder_path
    for filename in os.listdir(base_path):
        if os.path.isfile(os.path.join(base_path, filename)):
            file_path = os.path.join(base_path, filename)
            # Get last modified time of file
            file_modified_time = os.path.getmtime(file_path)
            file_modified_date = datetime.fromtimestamp(file_modified_time).strftime('%Y')
            # Create folder for the year if it does not exist
            folder_name = file_modified_date
            folder_path = os.path.join(base_path, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            # Move file to folder
            shutil.move(file_path, os.path.join(folder_path, filename))

            log.write_log(f"{filename} moved to {folder_name} folder.")

# Function to organize files by extension
def organize_files_by_extension(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_path = os.path.join(folder_path, filename)
            file_extension = os.path.splitext(filename)[1]
            folder_name = file_extension[1:].upper() + " Files"
            folder_path_ext = os.path.join(folder_path, folder_name)

            # Create folder for the extension if it does not exist
            if not os.path.exists(folder_path_ext):
                os.makedirs(folder_path_ext)

            # Move file to folder
            shutil.move(file_path, os.path.join(folder_path_ext, filename))

            log.write_log(f"{filename} moved to {folder_name} folder.")
