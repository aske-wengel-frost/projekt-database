import sqlite3

con = sqlite3.connect("library-data.db")
cur = con.cursor()

# Define table
cur.execute("CREATE TABLE books(id, author, yearpublished, title, genre, state)")

# Data insertion
# First define Data
data = [
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

cur.executemany('INSERT INTO books VALUES(?,?,?,?,?,?)', data)
con.commit()  # Commit transaction after excuting INSERT
