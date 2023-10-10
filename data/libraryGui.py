import tkinter as tk
from tkinter import ttk
import sqlite3


def connect_to_db():
    con1 = sqlite3.connect("library-data.db")
    cur1 = con1.cursor()
    cur1.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, author, yearpublished, title, genre, state)")
    cur1.execute("CREATE TABLE IF NOT EXISTS lender(id INTEGER PRIMARY KEY, name, title, datelending)")
    con1.commit()
    con1.close()


def view_data():
    clear_table_data()
    con1 = sqlite3.connect("library-data.db")
    cur1 = con1.cursor()
    database_name = database_choice[str(text_var.get())]
    cur1.execute(f"SELECT * FROM {database_name}")
    rows = cur1.fetchall()

    for row in rows:
        print(row)
        tree_books.insert("", tk.END, value=row)

    con1.close()

    if database_name == 'books':
        tree_books["columns"] = ("Bog_id", "Bog_titel", "År", "Titel", "Genre", "Status")
    elif database_name == 'lender':
        tree_books["columns"] = ("Bog_id", "Bog_titel", "Navn", "Dato_udlånt")
    else:
        return

    for heading in tree_books["columns"]:
        tree_books.heading(heading, text=heading)


def clear_table_data():
    for row in tree_books.get_children():
        tree_books.delete(row)


# Connect to database
connect_to_db()
root = tk.Tk()
root.title("Library Data")
root.geometry("1400x300")

# Create and pack the frame separately
table_frame = ttk.Frame(root)
table_frame.pack()
tree_books = ttk.Treeview(table_frame)

database_choice = {'Bøger': 'books', 'Lånere': 'lender', 'Udlån': 'bruh'}
text_var = tk.StringVar()
text_var.set('Bøger')
dropdown_menu = ttk.Combobox(root, values=list(database_choice.keys()), textvariable=text_var)
dropdown_menu.set('Vælg en database')
getData = tk.Button(root, text="Display Data", command=view_data)

# Pack items
getData.pack()
dropdown_menu.pack()
tree_books.pack()
root.mainloop()
