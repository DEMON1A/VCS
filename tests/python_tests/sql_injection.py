import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

user_input = input("table: ")

cursor.execute(f"CREATE TABLE IF NOT EXISTS {user_input} (id INTEGER PRIMARY KEY)")
cursor.execute("CREATE TABLE IF NOT EXISTS {0} (id INTEGER PRIMARY KEY)".format(user_input))
cursor.execute("CREATE TABLE IF NOT EXISTS %s (id INTEGER PRIMARY KEY)" % user_input)

conn.commit()
conn.close()