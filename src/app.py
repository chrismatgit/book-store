from tkinter import *

# create an empty window
window = Tk()

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

# create a button
b1 = Button(window, text="View all", width=12)
b1.grid(row=2, column=3)  # display the button

# create a button
b2 = Button(window, text="Search entry", width=12)
b2.grid(row=3, column=3)  # display the button

# create a button
b3 = Button(window, text="Add entry", width=12)
b3.grid(row=4, column=3)  # display the button

# create a button
b4 = Button(window, text="Update selected", width=12)
b4.grid(row=5, column=3)  # display the button

# create a button
b5 = Button(window, text="Delete selected", width=12)
b5.grid(row=6, column=3)  # display the button

# create a button
b6 = Button(window, text="Close", width=12)
b6.grid(row=7, column=3)  # display the button

window.mainloop()
