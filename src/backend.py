import sqlite3


def connect_db():
    ''' Function to connect to the database'''
    # create a connection
    connection = sqlite3.connect("books.db")
    # create a cursor
    cursor = connection.cursor()
    # Sql comment goes in the function execute
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    # Commit or execute the query
    connection.commit()
    # At the end close the connection
    connection.close()


def insert_data(title, author, year, isbn):
    ''' Function to insert data into the database'''
    # create a connection
    connection = sqlite3.connect("books.db")
    # create a cursor
    cursor = connection.cursor()
    # Sql comment goes in the function execute
    cursor.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",
                   (title, author, year, isbn))
    # Commit or execute the query
    connection.commit()
    # At the end close the connection
    connection.close()


def view_data():
    ''' Function to view data from the database'''
    # create a connection
    connection = sqlite3.connect("books.db")
    # create a cursor
    cursor = connection.cursor()
    # Sql comment goes in the function execute
    cursor.execute("SELECT * FROM book")
    # store the result into a variable by returning a tuple
    res = cursor.fetchall()
    # At the end close the connection
    connection.close()
    # returning the result of the function as a list
    return res


def search_data(title='', author='', year='', isbn=''):
    ''' Function to search data from the database'''
    # create a connection
    connection = sqlite3.connect("books.db")
    # create a cursor
    cursor = connection.cursor()
    # Sql comment goes in the function execute
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",
                   (title, author, year, isbn))
    # store the result into a variable by returning a tuple
    res = cursor.fetchall()
    # At the end close the connection
    connection.close()
    # returning the result of the function as a list
    return res


def delete_data(id):
    ''' Function to delete data from the database'''
    # create a connection
    connection = sqlite3.connect("books.db")
    # create a cursor
    cursor = connection.cursor()
    # Sql comment goes in the function execute
    cursor.execute("DELETE FROM book WHERE id=?", (id,))
    # Commit or execute the query
    connection.commit()
    # At the end close the connection
    connection.close()


def update_data(id, title, author, year, isbn):
    ''' Function to update data from the database'''
    # create a connection
    connection = sqlite3.connect("books.db")
    # create a cursor
    cursor = connection.cursor()
    # Sql comment goes in the function execute
    cursor.execute(
        "UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    # Commit or execute the query
    connection.commit()
    # At the end close the connection
    connection.close()


connect_db()
# insert_data("The Sum", "John Smith", 1950, 1349987599)
# delete_data(3)
update_data(4, 'The moon', 'John Smith', 1959, 13499875585)
print(view_data())
# print(search_data(author='John Smith'))
