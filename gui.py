import _tkinter as tk
import 
import sqlite3

db_conn = sqlite3.connect('database.db')
theCursor = db_conn.cursor()

class MainRender(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
    def show(self):
        self.lift()

class NieuweFiets(MainRender):
    def __init__(self):
        super.__init__()
        self.initialize()

    def initialize(self):
        global naamInvoer
        global achternaamInvoer
        global telefoonnummerInvoer
        global pincodeInvoer

        naam = tk.Label(self, text="Naam: ").pack()
        naamInvoer = tk.Entry(self)
        naamInvoer.pack()

        #print(naamInvoer.get())
        achternaam= tk.Label(self, text= "Achternaam: ").pack()
        achternaamInvoer = tk.Entry(self)
        achternaamInvoer.pack()

        telefoonnummer = tk.Label(self, text="Telefoonnummer: ").pack()
        telefoonnummerInvoer = tk.Entry(self)
        telefoonnummerInvoer.pack()

        pincode = tk.Label(self, text="Kies een viercijferige pincode: ").pack()
        pincodeInvoer = tk.Entry(self)
        pincodeInvoer.pack()

        doorgaan = tk.Button(self, text="doorgaan", command=self.importDatabase).pack()
    def importDatabase(self):
        db_conn.execute("INSERT INTO Fietsenstalling VALUES (Naam, Achternaam, Telefoonnummer, PIN);", (naamInvoer.get(), achternaamInvoer.get(), telefoonnummerInvoer.get(), pincodeInvoer.get()))
        db_conn.commit()
        #print(naamInvoer.get(), achternaamInvoer.get(), telefoonnummerInvoer.get(), pincodeInvoer.get())


    def switch1(self):
        print(naamInvoer.get())
        Pag1.lift()

class FietsOphalen(MainRender):
    def __init__(self):
        super.__init__()
        self.initialize()
    def initialize(self):

        label_1 = tk.Label(self, text="wat is uw fietsnummer: ")
        label_2 = tk.Label(self, text="wat uw pincode: ")

        entry_1 = tk.Entry(self)
        entry_2 = tk.Entry(self, show="*")

        label_1.grid(row=0, sticky=tk.E)
        label_2.grid(row=1, sticky=tk.E)
        entry_1.grid(row=0, column=1)
        entry_2.grid(row=1, column=1)


    def _login_btn_clicked(self):
        # print("Clicked")
        fietsnr = tk.Entry(self)
        pincode = tk.Entry(self)

        # print(username, password)

        if fietsnr == "john" and pincode == "password":
            ("scan QR code")
        else:
            tm.showerror("incorrect")



class FietsStallen(MainRender):
    def __init__(self):
        super.__init__()
        self.initialize()
    def initialize(self):
        tk.Label(self, text='randomtext').pack()

#frame for in window
class MainMenu(MainRender):
    def __init__(self):
        super.__init__()
        self.initialize()
    def initialize(self):
        butt1= tk.Button(self,text='Nieuwe Fiets', command=HoofdScherm.schermNieuweFiets).pack()
        butt2= tk.Button(self,text='Fiets Stallen', command=HoofdScherm.schermFietsStallen).pack()
        butt3= tk.Button(self, text="Fiets Ophalen", command=HoofdScherm.schermFietsOphalen).pack()

#window
class HoofdScherm(tk.Frame):
    def __init__(self):
        super.__init__()
        self.initialize()

    def initialize(self):
        global Pag1
        global Pag2
        global Pag3
        global Pag4

        Pag1 = NieuweFiets()
        Pag2 = FietsStallen()
        Pag3 = MainMenu()
        Pag4 = FietsOphalen()

        self.buttonframe = tk.Frame(self)
        self.container = tk.Frame(self)
        self.buttonframe.pack(side='top', fill='x', expand=False)
        self.container.pack(side='top', fill='both', expand=True)

        Pag1.place(in_ = self.container, x=0, y=0, relwidth=1, relheight=1)
        Pag2.place(in_ = self.container, x=0, y=0, relwidth=1, relheight=1)
        Pag3.place(in_ = self.container, x=0, y=0, relwidth=1, relheight=1)
        Pag4.place(in_ = self.container, x=0, y=0, relwidth=1, relheight=1)


        Pag3.show()

    def schermNieuweFiets(self):
        Pag1.lift()

    def schermFietsOphalen(self):
        Pag4.lift()

    def schermMainMenu(self):
        Pag3.lift()

    def schermFietsStallen(self):
        Pag2.lift()




if __name__ == "__main__":
    root=tk.Tk()
    main=HoofdScherm()
    main.pack(side='top', fill='both', expand=True)
    root.geometry('640x640')
    root.mainloop()
