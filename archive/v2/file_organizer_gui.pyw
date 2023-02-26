import tkinter as tk
from tkinter import filedialog
from datetime import datetime

import file_organizer_log as log
import file_organizer_logic as logic

class FileOrganizerGUI:
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
            logic.organize_files_by_date(self.folder_path)

            self.folder_label.configure(text="Files successfully organized by date.")
        
        # Move files by extension
        elif self.selection_var.get() == "Extension":
            logic.organize_files_by_extension(self.folder_path)

            self.folder_label.configure(text="Files successfully organized by extension.")
        else:
            self.folder_label.configure(text="Please make a selection")

root = tk.Tk()
my_gui = FileOrganizerGUI(root)
root.mainloop()