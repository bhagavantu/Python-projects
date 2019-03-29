# import sqlite3
# con.row_factory = sqlite3.Row
# cur = con.cursor()
# cur.execute("SELECT id, first_name, last_name FROM customers WHERE id = 2")
# result = cur.fetchone()
# id, first_name, last_name = result['id'], result['first_name'], result['last_name']
# print(f"Customer: {first_name} {last_name}'s id is {id}")
import sqlite3
cur.execute("SELECT id, first_name, last_name FROM customers")
results = cur.fetchall()
for row in results:
	print(row)
