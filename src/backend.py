import sqlite3


class Database:
    ''' Class that hundles the database operations '''

    def __init__(self):
        ''' Constructor to connect to the database'''
        # create a connection
        connection = sqlite3.connect("books.db")
        # create a cursor
        cursor = connection.cursor()
        # Sql comment goes in the method execute
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        # Commit or execute the query
        connection.commit()
        # At the end close the connection
        connection.close()

    def insert_data(self, title, author, year, isbn):
        ''' method to insert data into the database'''
        # create a connection
        connection = sqlite3.connect("books.db")
        # create a cursor
        cursor = connection.cursor()
        # Sql comment goes in the method execute
        cursor.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",
                       (title, author, year, isbn))
        # Commit or execute the query
        connection.commit()
        # At the end close the connection
        connection.close()

    def view_data(self):
        ''' method to view data from the database'''
        # create a connection
        connection = sqlite3.connect("books.db")
        # create a cursor
        cursor = connection.cursor()
        # Sql comment goes in the method execute
        cursor.execute("SELECT * FROM book")
        # store the result into a variable by returning a tuple
        res = cursor.fetchall()
        # At the end close the connection
        connection.close()
        # returning the result of the method as a list
        return res

    def search_data(self, title='', author='', year='', isbn=''):
        ''' method to search data from the database'''
        # create a connection
        connection = sqlite3.connect("books.db")
        # create a cursor
        cursor = connection.cursor()
        # Sql comment goes in the method execute
        cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",
                       (title, author, year, isbn))
        # store the result into a variable by returning a tuple
        res = cursor.fetchall()
        # At the end close the connection
        connection.close()
        # returning the result of the method as a list
        return res

    def delete_data(self, id):
        ''' method to delete data from the database'''
        # create a connection
        connection = sqlite3.connect("books.db")
        # create a cursor
        cursor = connection.cursor()
        # Sql comment goes in the method execute
        cursor.execute("DELETE FROM book WHERE id=?", (id,))
        # Commit or execute the query
        connection.commit()
        # At the end close the connection
        connection.close()

    def update_data(self, id, title, author, year, isbn):
        ''' method to update data from the database'''
        # create a connection
        connection = sqlite3.connect("books.db")
        # create a cursor
        cursor = connection.cursor()
        # Sql comment goes in the method execute
        cursor.execute(
            "UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        # Commit or execute the query
        connection.commit()
        # At the end close the connection
        connection.close()

    # connect_db()
    # insert_data("The Sum", "John Smith", 1950, 1349987599)
    # delete_data(3)
    # update_data(4, 'The moon', 'John Smith', 1959, 13499875585)
    # print(view_data())
    # print(search_data(author='John Smith'))
