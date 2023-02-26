import tkinter as tk
from tkinter import filedialog
from datetime import datetime

import file_organizer_log as log
import file_organizer_logic as logic

class FileOrganizerGUI:
    def __init__(self, master):
        self.master = master
        master.title("File Organizer")

        self.background_color = "#131517"
        self.foreground_color = "#731F00"
        self.accent_color = self.background_color
        self.active_color = "#000000"

        self.text_font = ("Arial", 12)

        self.window_width = 380
        self.window_height = 170
        self.x_coordinate = int((master.winfo_screenwidth() / 2) - (self.window_width / 2))
        self.y_coordinate = int((master.winfo_screenheight() / 2) - (self.window_height / 2))

        master.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x_coordinate, self.y_coordinate))
        master.config(bg=self.background_color)

        self.background_canvas = tk.Canvas(master, bg=self.foreground_color, highlightthickness=0)
        self.background_canvas.place(relwidth=1, relheight=1)

        self.lines = []
        self.lines.append(self.background_canvas.create_line(0, 0, 500, 300, fill=self.background_color))
        self.lines.append(self.background_canvas.create_line(500, 0, 0, 300, fill=self.background_color))
        
        self.background_canvas.after(500, self.animate)

        self.folder_label = tk.Label(master, text="Please select a folder", bg=self.background_color, fg=self.foreground_color, font=self.text_font)
        self.select_button = tk.Button(master, text="Select Folder", bg=self.accent_color, fg=self.foreground_color, activebackground=self.active_color, activeforeground=self.foreground_color, font=self.text_font, command=self.select_folder)
        self.organize_button = tk.Button(master, text="Organize", bg=self.accent_color, fg=self.foreground_color, activebackground=self.active_color, activeforeground=self.foreground_color, font=self.text_font, command=self.organize_files)

        self.folder_label.pack(pady=10)
        self.select_button.pack()
        self.organize_button.pack(pady=10)

        self.selection_var = tk.StringVar(value="Date")
        self.selection_frame = tk.Frame(master, bg=self.background_color)
        self.radio_button1 = tk.Radiobutton(self.selection_frame, text="Move by date", variable=self.selection_var, value="Date", bg=self.background_color, fg=self.foreground_color, activebackground=self.active_color, activeforeground=self.foreground_color, font=self.text_font)
        self.radio_button2 = tk.Radiobutton(self.selection_frame, text="Move by extension", variable=self.selection_var, value="Extension", bg=self.background_color, fg=self.foreground_color, activebackground=self.active_color, activeforeground=self.foreground_color, font=self.text_font)

        self.selection_frame.pack()
        self.radio_button1.pack(side="left")
        self.radio_button2.pack(side="left")

    def animate(self):
        self.move_lines()
        self.background_canvas.after(100, self.animate)

    def move_lines(self):
        for i, line in enumerate(self.lines):
            coords = self.background_canvas.coords(line)
            if i % 2 == 0:
                coords[0] += 10
                coords[2] += 10
            else:
                coords[0] -= 10
                coords[2] -= 10
            if coords[0] > self.window_width:
                coords[0] = -10
                coords[2] = self.window_width - 490
            elif coords[2] < 0:
                coords[0] = self.window_width - 10
                coords[2] = 490
            self.background_canvas.coords(line, *coords)


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