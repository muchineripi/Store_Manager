from tkinter import *
from db import Database
from tkinter import messagebox

db = Database('store.db')
selected_item = ''

def populate_list():
    orders_list.delete(0, END)
    for row in db.fetch():
        orders_list.insert(END, row)

def add_item():
    if not item_text.get() or not customer_text.get() or not seller_text.get() or not price_text.get():
        messagebox.showerror('Required fields', 'Please include all fields')
    else:
        db.insert(item_text.get(), customer_text.get(), seller_text.get(), price_text.get())
        populate_list()
        clear_input()

def remove_item():
    db.remove(selected_item[0])
    clear_input()
    populate_list()

def update_item():
    db.update(selected_item[0], item_text.get(), customer_text.get(), seller_text.get(), price_text.get())
    populate_list()
    clear_input()

def clear_input():
    global selected_item
    item_entry.delete(0, END)
    customer_entry.delete(0, END)
    seller_entry.delete(0, END)
    price_entry.delete(0, END)
    selected_item = ''

def select_item(item):
    clear_input()

    global selected_item
    index = orders_list.curselection()[0]
    selected_item = orders_list.get(index)
    print(selected_item)

    item_entry.insert(END, selected_item[1])
    customer_entry.insert(END, selected_item[2])
    seller_entry.insert(END, selected_item[3])
    price_entry.insert(END, selected_item[4])

app = Tk()
app.title("Majoress Boutique Store Manager")
app.geometry('700x350')

item_text = StringVar()
item_label = Label(app, text='Item name', font=('bold', 14), pady=20, padx=20)
item_label.grid(row=0, column=0, sticky=W)
item_entry = Entry(app, textvariable=item_text)
item_entry.grid(row=0, column=1)

customer_text = StringVar()
customer_label = Label(app, text='Customer', font=('bold', 14), pady=20, padx=20)
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

seller_text = StringVar()
seller_label = Label(app, text='Seller', font=('bold', 14), pady=20, padx=20)
seller_label.grid(row=1, column=0, sticky=W)
seller_entry = Entry(app, textvariable=seller_text)
seller_entry.grid(row=1, column=1)

price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14), pady=20, padx=20)
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

add_btn = Button(app, text='Add order', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove order', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update order', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_input)
clear_btn.grid(row=2, column=3)

orders_list = Listbox(app, height=5, width=50, borderwidth=1)
orders_list.grid(row=3, column=0, columnspan=3, rowspan=6, padx=20, pady=20)

scrollbar = Scrollbar(app, orient=VERTICAL, command=orders_list.yview)
scrollbar.grid(row=3, column=2, rowspan=6, sticky=E, padx=20)

orders_list.config(yscrollcommand=scrollbar.set)
orders_list.bind("<<ListboxSelect>>", select_item)

populate_list()

app.mainloop()
