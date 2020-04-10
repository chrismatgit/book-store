import psycopg2

def create_table():
    ''' Function to insert create table store into the database'''
    # create a connection
    connection = psycopg2.connect("dbname='database1' user='postgres' password='' host='localhost' port='5432'")
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
    connection = psycopg2.connect("dbname='database1' user='postgres' password='' host='localhost' port='5432'")
    # create a cursor
    cursor = connection.cursor()
    # Sql comment goes in the function execute
    # cursor.execute("INSERT INTO store VALUES('%s','%s','%s')" % (item,quantity,price))
    # to avoid an sql injection we should use this orther statement
    cursor.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    # Commit or execute the query
    connection.commit()
    # At the end close the connection
    connection.close()

def view_data():
    ''' Function to view data from the database'''
    # create a connection
    connection = psycopg2.connect("dbname='database1' user='postgres' password='' host='localhost' port='5432'")
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


def delete_data(item):
    ''' Function to delete data from the database'''
    # create a connection
    connection = psycopg2.connect("dbname='database1' user='postgres' password='' host='localhost' port='5432'")
    # create a cursor
    cursor = connection.cursor()
    # Sql comment goes in the function execute
    cursor.execute("DELETE FROM store WHERE item=%s", (item,))
    # Commit or execute the query
    connection.commit()
    # At the end close the connection
    connection.close()

def update_data(quantity,price,item):
    ''' Function to delete data from the database'''
    # create a connection
    connection = psycopg2.connect("dbname='database1' user='postgres' password='' host='localhost' port='5432'")
    # create a cursor
    cursor = connection.cursor()
    # Sql comment goes in the function execute
    cursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity,price,item,))
    # Commit or execute the query
    connection.commit()
    # At the end close the connection
    connection.close()

# create_table()
update_data(80, 19,"Juice") # update data from the database
# delete_data("milk") # delete data  
# insert_data("Juice", 70, 20) #insert data into the table
print(view_data()) 
