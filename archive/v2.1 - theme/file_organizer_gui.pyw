import tkinter as tk
from tkinter import filedialog
from datetime import datetime

import file_organizer_log as log
import file_organizer_logic as logic

class FileOrganizerGUI:
    def __init__(self, master):
        self.master = master
        master.title("File Organizer")
        
        # Renkler
        self.background_color = "#1B1B1B"
        self.foreground_color = "#FFFFFF"
        self.accent_color = "#3A3A3A"
        self.active_color = "#6C6C6C"
        self.text_font = ("Arial", 12)
        
        # Pencere boyutları
        self.window_width = 500
        self.window_height = 300
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.x_coordinate = int((self.screen_width / 2) - (self.window_width / 2))
        self.y_coordinate = int((self.screen_height / 2) - (self.window_height / 2))
        
        # Pencere ayarları
        self.master.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x_coordinate, self.y_coordinate))
        self.master.config(bg=self.background_color)

        self.folder_path = ""
        self.folder_label = tk.Label(master, text="Please select a folder", bg=self.background_color, fg=self.foreground_color, font=self.text_font)
        self.folder_label.pack(pady=10)

        self.select_button = tk.Button(master, text="Select Folder", bg=self.accent_color, fg=self.foreground_color, activebackground=self.active_color, activeforeground=self.foreground_color, font=self.text_font, command=self.select_folder)
        self.select_button.pack()

        self.organize_button = tk.Button(master, text="Organize", bg=self.accent_color, fg=self.foreground_color, activebackground=self.active_color, activeforeground=self.foreground_color, font=self.text_font, command=self.organize_files)
        self.organize_button.pack(pady=10)

        self.selection_var = tk.StringVar()
        self.selection_var.set("Date")

        self.selection_frame = tk.Frame(master, bg=self.background_color)
        self.selection_frame.pack()

        self.radio_button1 = tk.Radiobutton(self.selection_frame, text="Move by date", variable=self.selection_var, value="Date", bg=self.background_color, fg=self.foreground_color, activebackground=self.active_color, activeforeground=self.foreground_color, font=self.text_font)
        self.radio_button2 = tk.Radiobutton(self.selection_frame, text="Move by extension", variable=self.selection_var, value="Extension", bg=self.background_color, fg=self.foreground_color, activebackground=self.active_color, activeforeground=self.foreground_color, font=self.text_font)
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