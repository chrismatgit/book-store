import sqlite3

def create_table():
    ''' Function to insert create table store into the database'''
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

def insert_data(item, quantity, price):
    ''' Function to insert data into the database'''
    # create a connection
    connection = sqlite3.connect("lite.db")
    # create a cursor
    cursor = connection.cursor()
    # Sql comment goes in the function execute
    cursor.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    # Commit or execute the query
    connection.commit()
    # At the end close the connection
    connection.close()

insert_data("Juice", 50, 8)

def view_data():
    ''' Function to view data from the database'''
    # create a connection
    connection = sqlite3.connect("lite.db")
    # create a cursor
    cursor = connection.cursor()
    # Sql comment goes in the function execute
    cursor.execute("SELECT*FROM store")
    # store the result into a variable
    res = cursor.fetchall()
    # At the end close the connection
    connection.close()
    # returning the result of the function as a list
    return res

print(view_data())