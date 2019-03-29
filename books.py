import sqlite3

con = sqlite3.connect("books_db.sqlite3")
cur = con.cursor()

try:
	cur.execute("""CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT, rating REAL)""")
except sqlite3.OperationalError:
	print("Table already exists...")
cur.execute("""INSERT INTO books VALUES (1, "Exam worriors", 4)""")
cur.execute("""INSERT INTO books VALUES (2, "XYZ", 4.3)""")
cur.execute("""INSERT INTO books VALUES (3, "The king", 4.4)""")

con.commit()