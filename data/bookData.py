import sqlite3

con = sqlite3.connect("library-data.db")
cur = con.cursor()

# Define table
# cur.execute("CREATE TABLE books(author, yearpublished, title, genre, state)")

# Data insertion
# First define Data
data = [
    ("Harper Lee", 1960, "To Kill a Mockingbird", "Fiction", True),
    ("J.K. Rowling", 1997, "Harry Potter and the Philosopher's Stone", "Fantasy", True),
    ("George Orwell", 1949, "1984", "Dystopian", True),
    ("Jane Austen", 1813, "Pride and Prejudice", "Romance", False),
    (
        "Gabriel García Márquez",
        1967,
        "One Hundred Years of Solitude",
        "Magical Realism",
        True,
    ),
    ("Agatha Christie", 1934, "Murder on the Orient Express", "Mystery", True),
    ("F. Scott Fitzgerald", 1925, "The Great Gatsby", "Classic", False),
    ("J.R.R. Tolkien", 1954, "The Lord of the Rings", "Fantasy", True),
    ("Chimamanda Ngozi Adichie", 2003, "Purple Hibiscus", "Fiction", False),
    ("Khaled Hosseini", 2003, "The Kite Runner", "Historical Fiction", True),
]
cur.executemany("INSERT INTO books VALUES(?,?,?,?,?)", data)
con.commit()  # Commit transaction after excuting INSERT


def fetch_data():
    # Fetch Data
    for row in cur.execute(
        "SELECT author,yearpublished, title, genre, state FROM books"
    ):
        return [row]
