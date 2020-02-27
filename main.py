'''
A program that stores book information:
Title, Author, Year, ISBN

User can search, delete, update, view books in Library
'''

from tkinter import *
from db_conn import  Database

db = Database("books.db")

def view_command():
    book_list.delete(0,END)
    for book in db.view():
        book_list.insert(END,book)

def seach_command():
    book_list.delete(0,END)
    for book in db.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        book_list.insert(END,book)

def add_command():
    book_list.delete(0,END)
    db.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    book_list.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def get_selected_row(event):
    global selected_book
    try:
        index = book_list.curselection()[0]
        selected_book = book_list.get(index)
        
        entry_title.delete(0,END)
        entry_title.insert(END,selected_book[1])

        author_title.delete(0,END)
        author_title.insert(END,selected_book[2])

        year_title.delete(0,END)
        year_title.insert(END,selected_book[3])

        isbn_title.delete(0,END)
        isbn_title.insert(END,selected_book[4])
    except:
        print("Error in selected book defintion: " + book_list.curselection()[0])
        pass


def delete_command():
    try:
        db.delete(selected_book[0])
        view_command()
    except:
        pass


def update_command():
    try:
        db.update(selected_book[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        view_command()
    except:
        pass
    
window = Tk()
window.wm_title("Officer Library")

# Labels
label_title = Label(window,text="Title") 
label_title.grid(row=0,column=0)

label_author = Label(window,text="Author")
label_author.grid(row=0,column=2)

label_year = Label(window,text="Year")
label_year.grid(row=1,column=0)

label_isbn = Label(window,text="ISBN")
label_isbn.grid(row=1,column=2)

# Entries
title_text = StringVar()
entry_title = Entry(window,textvariable=title_text)
entry_title.grid(row=0,column=1)

author_text = StringVar()
author_title = Entry(window,textvariable=author_text)
author_title.grid(row=0,column=3)

year_text = StringVar()
year_title = Entry(window,textvariable=year_text)
year_title.grid(row=1,column=1)

isbn_text = StringVar()
isbn_title = Entry(window,textvariable=isbn_text)
isbn_title.grid(row=1,column=3)

# Display list of records
book_list = Listbox(window,height=6,width=35)
book_list.grid(row=2,column=0,rowspan=6,columnspan=2)

scroll_book_list = Scrollbar(window)
scroll_book_list.grid(row=2,column=2,rowspan=6)

# Configure scroll bar with book list
book_list.configure(yscrollcommand=scroll_book_list.set)
scroll_book_list.configure(command=book_list.yview)

# bind list
book_list.bind('<<ListboxSelect>>',get_selected_row)

# Buttons
button_viewall = Button(window,text="View All",width=12,command=view_command)
button_viewall.grid(row=2,column=3)

button_search = Button(window,text="Search Entry",width=12,command=seach_command)
button_search.grid(row=3,column=3)

button_add = Button(window,text="Add Entry",width=12,command=add_command)
button_add.grid(row=4,column=3)

button_update = Button(window,text="Update",width=12,command=update_command)
button_update.grid(row=5,column=3)

button_delete = Button(window,text="Delete",width=12,command=delete_command)
button_delete.grid(row=6,column=3)

button_close = Button(window,text="Close",width=12,command=window.destroy)
button_close.grid(row=7,column=3)

window.mainloop()