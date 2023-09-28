from sqlite3 import enable_callback_tracebacks
import tkinter as tk
from tkinter import ttk
from bookData import fetch_data

root = tk.Tk()
root.title("Library Data")

# Create and pack the frame separately
table_frame = ttk.Frame(root)
table_frame.pack()

table = ttk.Treeview(table_frame)
table["columns"] = ("ID", "Author", "Year Published", "Title", "Genre", "State")

# Create headings for the table
for heading in table["columns"]:
    table.heading(heading, text=heading)


def get_and_insert_data():
    data = fetch_data()
    for item in data:
        table.insert("", tk.END, values=item[14])


getData = tk.Button(root, text="Get data", command=get_and_insert_data())
getData.pack()
table.pack()
root.mainloop()
