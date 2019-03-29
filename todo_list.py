import sqlite3

con = sqlite3.connect("movies_db.sqlite3")
cur = con.cursor()

try:
	cur.execute("""CREATE TABLE todo_list (id INTEGER PRIMARY KEY, item TEXT, minutes INTEGER)""")
except sqlite3.OperationalError:
	print("Table already exists...")

cur.execute("""INSERT INTO todo_list VALUES (1, "Wash the dishes", 15)""")
cur.execute("""INSERT INTO todo_list VALUES (2, "vacuuming", 20)""")
cur.execute("""INSERT INTO todo_list VALUES (3, "Learn some stuff on KA", 30)""")
cur.execute("""INSERT INTO todo_list VALUES (4, "washing clothes", 65)""")
con.commit()