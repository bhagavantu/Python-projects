import sqlite3

con = sqlite3.connect("dproject_db.sqlite3")
cur = con.cursor()

try:
	cur.execute("""CREATE TABLE bikes (id INTEGER PRIMARY KEY, item TEXT, model INTEGER, quantity INTEGER, price REAL)""")
except sqlite3.OperationalError:
	print("Table already exists...")

cur.execute("""INSERT INTO bikes VALUES (1, "Hero", 2000, 3,35000)""")
cur.execute("""INSERT INTO bikes VALUES (2, "Apachi", 2001, 4, 60000)""")
cur.execute("""INSERT INTO bikes VALUES (3, "Fashion pro", 2002, 2, 50000)""")
cur.execute("""INSERT INTO bikes VALUES (4, "Fashion plus", 2007, 1, 45000)""")
cur.execute("""INSERT INTO bikes VALUES (5, "Yamaha", 1998, 2, 67000)""")
cur.execute("""INSERT INTO bikes VALUES (6, "TVS", 1995, 4, 40000)""")
cur.execute("""INSERT INTO bikes VALUES (7, "Hero honda", 1999, 2, 70000)""")
cur.execute("""INSERT INTO bikes VALUES (8, "Activa", 2003, 3, 47000)""")
cur.execute("""INSERT INTO bikes VALUES (9, "Activa plus", 2008, 1,28000)""")
cur.execute("""INSERT INTO bikes VALUES (10, "Splender", 2015, 2,90000)""")
cur.execute("""INSERT INTO bikes VALUES (11, "KTM", 2016, 2, 100000)""")
cur.execute("""INSERT INTO bikes VALUES (12, "Avengers", 2017, 3, 98000)""")
cur.execute("""INSERT INTO bikes VALUES (14, "Royal challenge", 2012, 2, 76000)""")
cur.execute("""INSERT INTO bikes VALUES (15, "FZ", 2018, 2, 99000)""")
con.commit()




