from tkinter import *
# importing the database
from backend import Database

# the database object
database = Database()


def get_selected_row(event):
    ''' Function that bind that the widget '''
    try:
        # this a global variable mean it can be accessed out of the function
        global selected_tuple
        # return the indeces of the selected item
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        # to fill the entries with the selected data
        e1.delete(0, END)  # to make sure the list is empty
        e1.insert(END, selected_tuple[1])  # to insert the data
        e2.delete(0, END)  # to make sure the list is empty
        e2.insert(END, selected_tuple[2])  # to insert the data
        e3.delete(0, END)  # to make sure the list is empty
        e3.insert(END, selected_tuple[3])  # to insert the data
        e4.delete(0, END)  # to make sure the list is empty
        e4.insert(END, selected_tuple[4])  # to insert the data
    except IndexError:
        pass


def view_command():
    ''' Function that execute the view command '''
    # to ensure that the list is empty before displaying any data
    list1.delete(0, END)
    for row in database.view_data():  # accessing the list
        # putting the row in the end of the list that are display
        list1.insert(END, row)


def search_command():
    ''' Function that execute the search command '''
    # to ensure that the list is empty before displaying any data
    list1.delete(0, END)
    # accessing the result as a list
    for row in database.search_data(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    ''' Function that execute the add command '''
    # insterting data to the database from the frontend
    database.insert_data(title_text.get(), author_text.get(),
                         year_text.get(), isbn_text.get())
    # to ensure that the list is empty before displaying any data
    list1.delete(0, END)
    # putting the row in the end of the list that are display
    list1.insert(END, (title_text.get(), author_text.get(),
                       year_text.get(), isbn_text.get()))


def delete_command():
    ''' Function that execute the add command '''
    # deleting data from the database
    database.delete_data(selected_tuple[0])


def update_command():
    ''' Function that execute the update command '''
    # updating data to the database
    database.update_data(selected_tuple[0], title_text.get(), author_text.get(),
                         year_text.get(), isbn_text.get())


# create an empty window
window = Tk()

# adding the title to our window
window.wm_title("Book Store")

# create a label
l1 = Label(window, text="Title")
# display a label
l1.grid(row=0, column=0)

# create a label
l2 = Label(window, text="Author")
l2.grid(row=0, column=2)  # display a label

# create a label
l2 = Label(window, text="Year")
l2.grid(row=1, column=0)  # display a label

# create a label
l2 = Label(window, text="ISBN")
l2.grid(row=1, column=2)  # display a label

# create an entry
title_text = StringVar()  # value holder for string value
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

# create an entry
author_text = StringVar()  # value holder for string value
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

# create an entry
year_text = StringVar()  # value holder for string value
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

# create an entry
isbn_text = StringVar()  # value holder for string value
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# create a Listbox
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# create a Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# configure a Scrollbar so that it can interact with the Listbox
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# binding a widget to a function in python
list1.bind('<<ListboxSelect>>', get_selected_row)

# create a view all button
b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)  # display the button

# create a search button
b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)  # display the button

# create an add button
b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)  # display the button

# create an update button
b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)  # display the button

# create a delete button
b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)  # display the button

# create a close button
b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)  # display the button

window.mainloop()
