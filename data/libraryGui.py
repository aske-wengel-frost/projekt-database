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


def view_data_books():
    con1 = sqlite3.connect("library-data.db")
    cur1 = con1.cursor()
    print(text_var.get())
    database_name = database_choice[str(text_var.get())]
    cur1.execute(f"SELECT * FROM {database_name}")
    rows = cur1.fetchall()
    for row in rows:
        print(row)
        tree_books.insert("", tk.END, value=row)
    con1.close()
    for rows in range(0, 7):
        tree_books.heading(f'#{rows}', text=f'{rows}')


def clear_table_data():
    for i in range(0, 7):
        tree_books.heading(f'#{i}', text='')
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
tree_books["columns"] = ("Bog_id", "Bog_titel", "År", "Titel", "Genre", "Status")

# Create headings for the table 'books'
for heading in tree_books["columns"]:
    tree_books.heading(heading, text=heading)

database_choice = {'Bøger': 'books', 'Lånere': 'lender', 'Udlån': 'bruh'}
text_var = tk.StringVar()
text_var.set('Bøger')
dropdown_menu = ttk.Combobox(root, values=list(database_choice.keys()), textvariable=text_var)
dropdown_menu.set('Vælg en database')
getData = tk.Button(root, text="Display Data", command=view_data_books)
clear_table = tk.Button(root, text='Clear Table', command=clear_table_data)

# Pack items
clear_table.pack()
getData.pack()
dropdown_menu.pack()
tree_books.pack()
root.mainloop()
