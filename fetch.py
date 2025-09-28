import json, sqlite3

connection = sqlite3.connect("projects.db")
cursor = connection.cursor()

for row in cursor.execute("SELECT * FROM projects"):
    print(row)

connection.close()
