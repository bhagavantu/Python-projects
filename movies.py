import sqlite3

con = sqlite3.connect("movies_db.sqlite3")
cur = con.cursor()

try:
	cur.execute("""CREATE TABLE movies (id INTEGER PRIMARY KEY, name TEXT, release_year INTEGER)""")
except sqlite3.OperationalError:
	print("Table already exists...")

cur.execute("""INSERT INTO movies VALUES (1, "Avatar", 2009)""")
cur.execute("""INSERT INTO movies VALUES (2, "Titanic", 1997)""")
cur.execute("""INSERT INTO movies VALUES (3, "The Lion King", 1994)""")
cur.execute("""INSERT INTO movies VALUES (4, "Disney's Up", 2009)""")
cur.execute("""INSERT INTO movies VALUES(5, "Star Wars: Episode IV - A New Hope", 1977)""")
cur.execute("""INSERT INTO movies VALUES(6, "Shrek 2", 2004)""")
con.commit()