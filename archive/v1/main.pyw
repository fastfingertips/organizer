import os
import shutil
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

import file_organizer_log as log

class FileOrganizer:
    def __init__(self, master):
        self.master = master
        master.title("File Organizer")

        self.folder_path = ""
        self.folder_label = tk.Label(master, text="Please select a folder")
        self.folder_label.pack(pady=10)

        self.select_button = tk.Button(master, text="Select Folder", command=self.select_folder)
        self.select_button.pack()

        self.organize_button = tk.Button(master, text="Organize", command=self.organize_files)
        self.organize_button.pack(pady=10)
        self.selection_var = tk.StringVar()
        self.selection_var.set("Date")
        self.selection_frame = tk.Frame(master)
        self.selection_frame.pack()
        self.radio_button1 = tk.Radiobutton(self.selection_frame, text="Move by date", variable=self.selection_var, value="Date")
        self.radio_button2 = tk.Radiobutton(self.selection_frame, text="Move by extension", variable=self.selection_var, value="Extension")
        self.radio_button1.pack(side="left")
        self.radio_button2.pack(side="left")

    # Function to select folder
    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        self.folder_label.configure(text="Selected folder: " + self.folder_path)

    # Function to organize files
    def organize_files(self):
        if not self.folder_path:
            self.folder_label.configure(text="Please select a folder")
            return

        # Move files by date
        if self.selection_var.get() == "Date":
            for filename in os.listdir(self.folder_path):
                if os.path.isfile(os.path.join(self.folder_path, filename)):
                    file_path = os.path.join(self.folder_path, filename)
                    # Get last modified time of file
                    file_modified_time = os.path.getmtime(file_path)
                    file_modified_date = datetime.fromtimestamp(file_modified_time).strftime('%Y')
                    # Create folder for the year if it does not exist
                    folder_name = file_modified_date
                    folder_path = os.path.join(self.folder_path, folder_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    # Move file to folder
                    shutil.move(file_path, os.path.join(folder_path, filename))

                    log.write_log(f"{filename} moved to {folder_name} folder.")

            self.folder_label.configure(text="Files successfully organized by date.")
        
        # Move files by extension
        elif self.selection_var.get() == "Extension":
            for filename in os.listdir(self.folder_path):
                if os.path.isfile(os.path.join(self.folder_path, filename)):
                    file_path = os.path.join(self.folder_path, filename)
                    file_extension = os.path.splitext(filename)[1]
                    folder_name = file_extension[1:].upper() + " Files"
                    folder_path = os.path.join(self.folder_path, folder_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(file_path, os.path.join(folder_path, filename))

                    log.write_log(f"{filename} moved to {folder_name} folder.")

            self.folder_label.configure(text="Files successfully organized by extension.")
        else:
            self.folder_label.configure(text="Please make a selection")

root = tk.Tk()
my_gui = FileOrganizer(root)
root.mainloop()
