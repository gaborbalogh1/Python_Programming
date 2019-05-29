import tkinter as tk
from tkinter import ttk, messagebox as msg
import tkinter.scrolledtext as sct
from tkinter import StringVar
import sqlite3
# from GlobalVar import name, address, tel
# from SQLConnect import sql_connect, sql_insert

root = tk.Tk()
root.minsize(width='400', height='600')
root.title('DataBase Form')

name = StringVar()
tel = StringVar()
address = tk.WORD

name_text = "Type your name here..."
tel_text = "+44(0) 1234567890"
address = "2 Microsoft Way, Redmond WA United States"

name.set(name_text)
tel.set(tel_text)


def sql_connect():
    db = "sql3.db"

    create_customers_table = """ CREATE TABLE IF NOT EXISTS Customers (
                                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name text NOT NULL,
                                        address text,
                                        tel text
                                    ); """

    create_membership_table = """CREATE TABLE IF NOT EXISTS Membership (
                                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        Customers_id INTEGER NOT NULL,
                                        name text NOT NULL,
                                        address integer,
                                        tel text NOT NULL,
                                        is_member text NOT NULL,
                                        join_date text,
                                        leave_date text,
                                        FOREIGN KEY (Customers_id) REFERENCES Customers (ID)
                                    );"""

    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(create_customers_table)
    c.execute(create_membership_table)
    conn.commit()
    conn.close()
    print("added 2 table")


def sql_insert(name_text, address, tel_text):
    # SQL lite error on insert shown you need to use parameters or params for short to send SQL statement.
    params = (name_text, address, tel_text)

    sql_connect()
    # need to set to auto increment id
    con = sqlite3.connect('sql3.db')
# insert into the database now working fine. Need to add more entry by file source like .csv
    with con:
        cur = con.cursor()
        # id = cur.execute("SELECT seq from sqlite_sequence where name=Customers")
        # print(id)
        cur.execute("INSERT INTO Customers VALUES(NULL, ?, ?, ?)", params)
        print("updated the table")
    con.commit()
    con.close()

# TODO need to apply an event handler for clearing the 3 text values on
# TODO mouse enter and to take the new values from the 3 box. then refactor to OOP this time :)
# TODO also need to implement a new query for the membership table if the membership is selected on the form.


def save(*args):
    sql_connect()
    sql_insert(name_text, address, tel_text)


def cancel():
    exit()

# take the fields and update the database with it.


def send():
    sql_connect()
    # sql_insert(name_text, address, tel_text)
    message = "Sent data to database."
    msg.askokcancel("Update Database ", message)


label = ttk.Label(root, text='Name', width='15').grid(column='0', row='0', columnspan='4', rowspan='1', padx=5,
                                                             pady=5, sticky='ns')

label2 = ttk.Label(root, text='Address', width='15').grid(column='0', row='1', columnspan='4', rowspan='1',
                                                          padx=5, pady=5, sticky='ns')

label3 = ttk.Label(root, text='Tel', width='15').grid(column='0', row='2', columnspan='4', rowspan='1',
                                                      padx=5, pady=5, sticky='ns')

label4 = ttk.Label(root, text='Membership', width='15').grid(column='0', row='3', columnspan='4', rowspan='1',
                                                             padx=5, pady=5, sticky='ns')

cancel_button = ttk.Button(root, text='cancel', width='15', command=cancel).grid(column='1', row='5', columnspan='2',
                                                                                 rowspan='1', padx=5, pady=5,
                                                                                 sticky='ns')

send_button = ttk.Button(root, text='send', width='15', command=send).grid(column='1', row='6', columnspan='4',
                                                                           rowspan='1', padx=5, pady=5, sticky='ns')

save_button = ttk.Button(root, text='save', width='15', command=save).grid(column='1', row='7', columnspan='4',
                                                                           rowspan='1', padx=5, pady=5, sticky='ns')

name_entry = tk.Entry(root, textvariable=name, relief=tk.SUNKEN, bg='orange').\
    grid(column='5', row='0', columnspan='4', rowspan='1', padx=5, pady=5, sticky='ns')

address_C = sct.ScrolledText(root, width=27, height=5, bg='orange',
                             wrap=tk.WORD)

address_C.grid(column='5', row='1', columnspan='4', rowspan='1', padx=5, pady=5, sticky='ns')

address_C.insert(tk.INSERT, address)

address_C.insert(tk.END, "\n\nHello")


tel_entry = tk.Entry(root, text="+44(0) 1234567890", textvariable=tel, relief=tk.SUNKEN, bg='orange').\
    grid(column='5', row='2', columnspan='4', rowspan='1', padx=5, pady=5, sticky='ns')

tk_var = tk.StringVar(root)
choices = ['Yes', 'No']
tk_var.set('Yes')

membership_entry = ttk.OptionMenu(root, tk_var, choices[0], *choices).grid(column='5', row='3', columnspan='4',
                                                                           rowspan='1', padx=5, pady=5, sticky='ns')


def change_drop_down(*args):
    choice = tk_var.get()
    print("You Selected: "+choice)
    # sql_connect()
    # print("connected to db")


tk_var.trace('w', change_drop_down)

root.mainloop()

# if __name__ == '__main__':

