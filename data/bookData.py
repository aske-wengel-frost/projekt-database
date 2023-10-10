import sqlite3

con = sqlite3.connect("library-data.db")
cur = con.cursor()

# Define tables
cur.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, author, yearpublished, title, genre, state)")
cur.execute("CREATE TABLE lender(id INTEGER PRIMARY KEY, name, title, datelending)")

# Data insertion
# First define Data
book_data = [
    (1, "Harper Lee", 1960, "To Kill a Mockingbird", "Fiction", True),
    (2, "J.K. Rowling", 1997, "Harry Potter and the Philosopher's Stone", "Fantasy", True),
    (3, "George Orwell", 1949, "1984", "Dystopian", True),
    (4, "Jane Austen", 1813, "Pride and Prejudice", "Romance", False),
    (
        5, "Gabriel García Márquez",
        1967, "One Hundred Years of Solitude", "Magical Realism", True,
    ),
    (6, "Agatha Christie", 1934, "Murder on the Orient Express", "Mystery", True),
    (7, "F. Scott Fitzgerald", 1925, "The Great Gatsby", "Classic", False),
    (8, "J.R.R. Tolkien", 1954, "The Lord of the Rings", "Fantasy", True),
    (9, "Chimamanda Ngozi Adichie", 2003, "Purple Hibiscus", "Fiction", False),
    (10, "Khaled Hosseini", 2003, "The Kite Runner", "Historical Fiction", True),
]

lending_data = [
    (1, "Aske", "Murder on the Orient Express", "03-10-23"),
    (2, "Yaser", "The Kite Runner", "03-10-23"),
    (3, "Noah", "The Lord of the Rings", "03-10-23"),
    (4, "Tobias", "One Hundred Years of Solitude", "03-10-23"),
    (5, "Kasper", "Pride and Predujice", "03-10-23"),
]

cur.executemany('INSERT INTO lender VALUES(?,?,?,?)', lending_data)
cur.executemany('INSERT INTO books VALUES(?,?,?,?,?,?)', book_data)
con.commit()  # Commit transaction after executing INSERT
