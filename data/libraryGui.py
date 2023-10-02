import tkinter as tk
from tkinter import ttk
import sqlite3


def connect_to_db():
    con1 = sqlite3.connect("library-data.db")
    cur1 = con1.cursor()
    cur1.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, author, yearpublished, title, genre, state)")
    con1.commit()
    con1.close()


def view_data():
    con1 = sqlite3.connect("library-data.db")
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM books")
    rows = cur1.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, value=row)
    con1.close()


# Connect to database
connect_to_db()
root = tk.Tk()
root.title("Library Data")
root.geometry("1400x800")

# Create and pack the frame separately
table_frame = ttk.Frame(root)
table_frame.pack()

tree = ttk.Treeview(table_frame)
tree["columns"] = ("ID", "Author", "Year Published", "Title", "Genre", "State")

# Create headings for the table
for heading in tree["columns"]:
    tree.heading(heading, text=heading)


getData = tk.Button(root, text="Display Data", command=view_data)
getData.pack()
tree.pack()
root.mainloop()
