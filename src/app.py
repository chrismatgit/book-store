import sqlite3

# create a connection
connection = sqlite3.connect("lite.db")

# create a cursor
cursor = connection.cursor()

# Sql comment goes in the function execute
cursor.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")

# Commit or execute the query
connection.commit()

# At the end close the connection
connection.close()