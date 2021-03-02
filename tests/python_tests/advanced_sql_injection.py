import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

user_input = input("table: ")
query = "CREATE TABLE IF NOT EXISTS {0}".format(user_input) + "(id INTEGER PRIMARY KEY)"

cursor.execute(query)
cursor.execute(f"CREATE TABLE IF NOT EXISTS {user_input} (id INTEGER PRIMARY KEY)")

conn.commit()
conn.close()
