import Database
import sqlite3
import tkinter as tk


db_conn = sqlite3.connect('database.db')
theCursor = db_conn.cursor()

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        label_1 = tk.Label(self, text="wat is uw fietsnummer: ")
        label_2 = tk.Label(self, text="wat uw pincode: ")

        entry_1 = tk.Entry(self)
        entry_2 = tk.Entry(self, show="*")

        label_1.grid(row=0, sticky=E)
        label_2.grid(row=1, sticky=E)
        entry_1.grid(row=0, column=1)
        entry_2.grid(row=1, column=1)


                # print(username, password)

