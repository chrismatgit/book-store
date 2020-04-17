from tkinter import *
# importing the database
from backend import Database

# the database object
database = Database()


class Window(object):
    ''' Class that contain the window object'''

    def __init__(self, window):  # constructor
        self.window = window

        # adding the title to our window
        self.window.wm_title("Book Store")

        # create a label
        self.l1 = Label(window, text="Title")
        # display a label
        self.l1.grid(row=0, column=0)

        # create a label
        self.l2 = Label(window, text="Author")
        self.l2.grid(row=0, column=2)  # display a label

        # create a label
        self.l3 = Label(window, text="Year")
        self.l3.grid(row=1, column=0)  # display a label

        # create a label
        self.l4 = Label(window, text="ISBN")
        self.l4.grid(row=1, column=2)  # display a label

        # create an entry
        self.title_text = StringVar()  # value holder for string value
        self.e1 = Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        # create an entry
        self.author_text = StringVar()  # value holder for string value
        self.e2 = Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        # create an entry
        self.year_text = StringVar()  # value holder for string value
        self.e3 = Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        # create an entry
        self.isbn_text = StringVar()  # value holder for string value
        self.e4 = Entry(window, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        # create a Listbox
        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        # create a Scrollbar
        self.sb1 = Scrollbar(window)
        self.sb1.grid(row=2, column=2, rowspan=6)

        # configure a Scrollbar so that it can interact with the Listbox
        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        # binding a widget to a function in python
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # create a view all button
        self.b1 = Button(window, text="View all",
                         width=12, command=self.view_command)
        self.b1.grid(row=2, column=3)  # display the button

        # create a search button
        self.b2 = Button(window, text="Search entry",
                         width=12, command=self.search_command)
        self.b2.grid(row=3, column=3)  # display the button

        # create an add button
        self.b3 = Button(window, text="Add entry",
                         width=12, command=self.add_command)
        self.b3.grid(row=4, column=3)  # display the button

        # create an update button
        self.b4 = Button(window, text="Update selected",
                         width=12, command=self.update_command)
        self.b4.grid(row=5, column=3)  # display the button

        # create a delete button
        self.b5 = Button(window, text="Delete selected",
                         width=12, command=self.delete_command)
        self.b5.grid(row=6, column=3)  # display the button

        # create a close button
        self.b6 = Button(window, text="Close", width=12,
                         command=window.destroy)
        self.b6.grid(row=7, column=3)  # display the button

    def get_selected_row(self, event):
        ''' Function that bind that the widget '''
        try:
            # return the indeces of the selected item
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            # to fill the entries with the selected data
            self.e1.delete(0, END)  # to make sure the list is empty
            # to insert the data
            self.e1.insert(END, self.selected_tuple[1])
            self.e2.delete(0, END)  # to make sure the list is empty
            # to insert the data
            self.e2.insert(END, self.selected_tuple[2])
            self.e3.delete(0, END)  # to make sure the list is empty
            # to insert the data
            self.e3.insert(END, self.selected_tuple[3])
            self.e4.delete(0, END)  # to make sure the list is empty
            # to insert the data
            self.e4.insert(END, self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        ''' Function that execute the view command '''
        # to ensure that the list is empty before displaying any data
        self.list1.delete(0, END)
        for self.row in database.view_data():  # accessing the list
            # putting the row in the end of the list that are display
            self.list1.insert(END, self.row)

    def search_command(self):
        ''' Function that execute the search command '''
        # to ensure that the list is empty before displaying any data
        self.list1.delete(0, END)
        # accessing the result as a list
        for row in database.search_data(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        ''' Function that execute the add command '''
        # insterting data to the database from the frontend
        database.insert_data(self.title_text.get(), self.author_text.get(),
                             self.year_text.get(), self.isbn_text.get())
        # to ensure that the list is empty before displaying any data
        self.list1.delete(0, END)
        # putting the row in the end of the list that are display
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(),
                                self.year_text.get(), self.isbn_text.get()))

    def delete_command(self):
        ''' Function that execute the add command '''
        # deleting data from the database
        database.delete_data(self.selected_tuple[0])

    def update_command(self):
        ''' Function that execute the update command '''
        # updating data to the database
        database.update_data(self.selected_tuple[0], self.title_text.get(), self.author_text.get(),
                             self.year_text.get(), self.isbn_text.get())


# create an empty window
window = Tk()
Window(window)
window.mainloop()
