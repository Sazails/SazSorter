import os
import shutil
import datetime
import tkinter as tk
from tkinter import filedialog
import random

startup_lines = [
    "SazSorter: The cheesiest way to organize your files!",
    "SazSorter: The ultimate file organizer!",
    "SazSorter: Where organization meets efficiency!",
    "SazSorter: The secret weapon against file mess!",
    "SazSorter: The superhero of file organization!",
    "SazSorter: The master of file sorting!",
    "SazSorter: The magician of file management!",
    "SazSorter: Making file chaos a thing of the past!",
    "SazSorter: The most efficient way to bring order to your files!"
]

# global vars
activity_text = None
create_separate_folders_var = None
source_folder_path = None
destination_folder_path = None

def get_files_from_directory(chosen_dir):
    files = os.listdir(chosen_dir)
    return files

def create_directory(chosen_dir):
    if os.path.exists(chosen_dir):
        activity_text.insert(tk.END, 'Directory: {} already exists!\n'.format(chosen_dir))
        return
    os.makedirs(chosen_dir)
    activity_text.insert(tk.END, 'Created directory: {}\n'.format(chosen_dir))

def update_GUI_activity_text(text):
    global activity_text
    activity_text.configure(state="normal")  # Enable editing of the activity_text textbox
    activity_text.insert(tk.INSERT, text + '\n')  # Insert the text at the beginning of the textbox
    activity_text.see(tk.END)  # Scroll to the end of the textbox
    activity_text.configure(state="disabled")  # Disable editing of the activity_text textbox
    activity_text.update_idletasks()  # Update the GUI immediately after inserting the text

def move_single_file(file_path, destination_path):
    global activity_text
    global source_folder_path
    global destination_folder_path
    global create_separate_folders_var
    
    if not os.path.exists(destination_path):
        create_directory(destination_path)

    try:
        if create_separate_folders_var.get():
            file_extension = os.path.splitext(file_path)[1]
            extension_folder = os.path.join(destination_path, file_extension[1:])
            create_directory(extension_folder)
            shutil.move(file_path, extension_folder)
            update_GUI_activity_text('Moved file "{}" to "{}"\n'.format(file_path, extension_folder))
        else:
            shutil.move(file_path, destination_path)
            update_GUI_activity_text('Moved file "{}" to "{}"\n'.format(file_path, destination_path))
    except FileNotFoundError:
        update_GUI_activity_text('File "{}" not found.\n'.format(file_path))
    except Exception as e:
        update_GUI_activity_text('An error occurred while moving the file: {}\n'.format(str(e)))

def select_source_folder():
    global source_folder_path
    
    chosen_dir = filedialog.askdirectory()
    source_folder_path.set(chosen_dir)

def select_destination_folder():
    global destination_folder_path
    
    chosen_dir = filedialog.askdirectory()
    destination_folder_path.set(chosen_dir)

def move_files():
    global source_folder_path
    global destination_folder_path
    
    # Clear the activity_text textbox
    global activity_text
    activity_text.configure(state="normal")
    activity_text.delete(1.0, tk.END)
    activity_text.configure(state="disabled")
    
    source_dir = source_folder_path.get()
    destination_dir = destination_folder_path.get()
    
    if not source_dir:
        update_GUI_activity_text('ERROR: Source folder path is empty.\n')
        return
    
    if not destination_dir:
        update_GUI_activity_text('ERROR: Destination folder path is empty.\n')
        return
    
    if not os.path.exists(source_dir):
        update_GUI_activity_text('ERROR: Source folder path does not exist.\n')
        return
    
    if not os.path.exists(destination_dir):
        update_GUI_activity_text('ERROR: Destination folder path does not exist.\n')
        return
    
    got_files = get_files_from_directory(source_dir)

    if not got_files:
        update_GUI_activity_text('WARNING: No files found in the selected source folder.\n')
        return

    for file in got_files:
        temp = datetime.datetime.fromtimestamp(
            os.path.getctime(os.path.join(source_dir, file)))
        date = temp.strftime("%Y_%m_%d")
        move_single_file(os.path.join(source_dir, file), os.path.join(destination_dir, date))

    update_GUI_activity_text('All files moved successfully!\n')

def create_gui():
    global activity_text
    global source_folder_path
    global destination_folder_path
    global create_separate_folders_var
    
    root = tk.Tk()
    root.title("Saz-Sorter")

    # Create GUI elements
    title_label = tk.Label(root, text="Saz-Sorter")
    instructions_label = tk.Text(root, wrap="word", height=10, width=80)
    instructions_label.insert(tk.END, "To use this program, follow these steps:\n\n1. Click the \"Source folder\" button to select the folder containing the files you want to sort.\n2. Click the \"Destination folder\" button to select the folder where you want to move the sorted files.\n3. Click the \"Move files\" button to initiate the sorting process.")
    instructions_label.configure(state="disabled")

    source_folder_button = tk.Button(root, text="Source folder", command=select_source_folder, width=20)
    source_folder_path = tk.StringVar()
    source_folder_path_entry = tk.Entry(root, textvariable=source_folder_path, state="readonly")

<<<<<<< HEAD
    destination_folder_button = tk.Button(root, text="Destination folder", command=select_destination_folder, width=20)
    destination_folder_path = tk.StringVar()
    destination_folder_path_entry = tk.Entry(root, textvariable=destination_folder_path, state="readonly")

    move_files_button = tk.Button(root, text="Move files", command=move_files)

    create_separate_folders_var = tk.IntVar()  # Initialize create_separate_folders_var after the Tkinter root window has been created
    create_separate_folders_checkbox = tk.Checkbutton(root, text="Create separate folders for file extensions", variable=create_separate_folders_var)

    activity_text = tk.Text(root, height=10, width=50)
    activity_text.configure(state="disabled")

    # Grid layout
    root.resizable(False, False)  # Disable window resizing
    root.geometry("840x720")  # Set window size to 1024x1024 pixels

    # Grid layout
    root.grid_rowconfigure(0, weight=0)  # Set weight to 0 to take only fraction of space
    root.grid_rowconfigure(6, weight=1)  # Stretch the last row
    root.grid_columnconfigure(0, weight=1)  # Stretch the first column
    root.grid_columnconfigure(1, weight=8)  # Stretch the second column to take 3/4 of the width

    title_label.grid(row=0, column=0, columnspan=2, sticky="ew")
    instructions_label.grid(row=1, column=0, columnspan=2, sticky="ew")  # Use sticky to stretch label to fit all text

    source_folder_button.grid(row=2, column=0, sticky="w", padx=10, pady=5)  # Align button to the left
    source_folder_path_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=5)  # Use sticky to stretch entry width

    destination_folder_button.grid(row=3, column=0, sticky="w", padx=10, pady=5)  # Align button to the left
    destination_folder_path_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=5)  # Use sticky to stretch entry width

    move_files_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)  # Add padding to center the button
    create_separate_folders_checkbox.grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=5)  # Add checkbox

    activity_text.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)  # Use sticky to stretch text box

    update_GUI_activity_text(random.choice(startup_lines))

    root.mainloop()

if __name__ == "__main__":
    create_gui()
=======
for file in gotFiles:
    temp = _dateTime.datetime.fromtimestamp(
        _os.path.getctime(RANDOMFILESPATH + file))
    date = temp.strftime("%Y_%m_%d")
    MoveFile(RANDOMFILESPATH + file, '{}{}'.format(SORTEDFILESPATH, date))

input("Press Enter to exit...")
>>>>>>> 593e4c7789ffbfaf64a0740d9f9f53529846d1c9
