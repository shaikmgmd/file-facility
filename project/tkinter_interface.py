import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from get_recent_files import get_recent_files
import time as time
import os
from functions import date_format

# [0] = curr_file_path
# [1] = file_acces_time
# [2] = file_creation_time
# [3] = file_modification_time

recent_files = get_recent_files("C:\\Users\\chica\\OneDrive\\Bureau")


def search(data):
    search_term = search_bar.get()
    selected_date = calendar.get_date()
    filtered_data = [file for file in data if search_term in file[0]
                     and date_format(time.ctime(file[3])) == str(selected_date)]
    update_display(filtered_data)


def update_display(data):
    tree.delete(*tree.get_children())
    for file in data:
        tree.insert("", "end", values=(
            os.path.basename(file[0]), file[0], time.ctime(file[1]), time.ctime(file[2]), time.ctime(file[3])))


def open_file(event):
    selected_file = tree.focus()
    selected_file_path = tree.item(selected_file)['values'][1]
    if selected_file_path:
        os.startfile(selected_file_path)


root = tk.Tk()
root.title("Recent Files")

search_bar = tk.Entry(root)
search_bar.pack()

calendar = DateEntry(root, width=12, background='darkblue',
                     foreground='white', borderwidth=2)
calendar.pack()

tree = ttk.Treeview(root, columns=(
    "name", "path", "access_time", "created_time", "modificated_time"))
tree.heading("name", text="Name")
tree.heading("path", text="Path")
tree.heading("access_time", text="Access Time")
tree.heading("created_time", text="Created Time")
tree.heading("modificated_time", text="Modified Time")
tree.column("#0", width=0, stretch=False)
tree.column("name", stretch=tk.NO)
tree.column("path", stretch=tk.YES)
tree.column("access_time", stretch=tk.NO)
tree.column("created_time", stretch=tk.NO)
tree.column("modificated_time", stretch=tk.NO)
tree.pack()

update_display(recent_files)

search_bar.bind("<Return>", lambda event: search(recent_files))
tree.bind("<Double-Button-1>", lambda event: open_file(event))
calendar.bind("<<DateEntrySelected>>", lambda event: search(recent_files))

root.mainloop()
