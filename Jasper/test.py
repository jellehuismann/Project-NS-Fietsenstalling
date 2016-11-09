from tkinter import *
import sqlite3


root = Tk()


label_1 = Label(root, text='Wat is uw fietsnummer: ')
label_2 = Label(root, text='wat is uw pincode: ')
invoer_fietsnr = Entry(root)
invoer_pin= Entry(root)

label_1.grid(row=0, sticky='E')
label_2.grid(row=1, sticky='E')
invoer_fietsnr.grid(row=0, column=1)
invoer_pin.grid(row=1, column=1)

doorgaan = Button(root, text='doorgaan')
doorgaan.grid(columnspan= 2)


root.mainloop()

fietsnr = 1
pincode = 1

def inlog:
    if fietsnr == invoer_fietsnr.get() and pincode.get == invoer_pin.get()