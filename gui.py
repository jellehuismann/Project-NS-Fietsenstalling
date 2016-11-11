import tkinter as tk
import image
from PIL import Image, ImageTk
import Database
import sqlite3
from Autenticatie import *
import random
db_conn = sqlite3.connect('database.db')
theCursor = db_conn.cursor()
ctrcode = 0
fietsnr = 0
pincode = 0
geplaatst = 0

class MainRender(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
    def show(self):
        self.lift()


class NieuweFiets(MainRender):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        global naamInvoer
        global achternaamInvoer
        global telefoonnummerInvoer
        global pincodeInvoer
        global FietsNr

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
        FietsNr = int((''.join(random.choice('1234567890') for _ in range(4))))
        tk.Button(self, text="Doorgaan", command=self.importDatabase).pack()
        tk.Button(self, text="Terug", command=HoofdScherm.schermMainMenu).pack()


    def importDatabase(self):
        print(ctrcode)
        db_conn.execute("INSERT INTO Fietsenstalling (Naam, Achternaam, Telefoon, FietsNr, PIN, otpKEY) VALUES "
                        "(?, ?, ?, ?, ?, ?);", (naamInvoer.get(), achternaamInvoer.get(), telefoonnummerInvoer.get(), FietsNr, pincodeInvoer.get(), ctrcode))

        db_conn.commit()
        HoofdScherm.schermFietsGeinstalleerd()


class FietsOphalen(MainRender):
    def __init__(self):
        super().__init__()
        self.initialize()
    def initialize(self):

        global entry_1
        global entry_2
        global entry_3
        label_1 = tk.Label(self, text="Wat is uw fietsnummer: ")
        label_2 = tk.Label(self, text="Wat uw pincode: ")
        label_3 = tk.Label(self, text="Wat is uw 6 cijferige authenticatie code: ")

        entry_1 = (tk.Entry(self))
        entry_2 = (tk.Entry(self, show="*"))
        entry_3 = (tk.Entry(self))

        label_1.grid(row=0, sticky=tk.E)
        label_2.grid(row=1, sticky=tk.E)
        label_3.grid(row=2, sticky=tk.E)
        entry_1.grid(row=0, column=1)
        entry_2.grid(row=1, column=1)
        entry_3.grid(row=2, column=1)

        doorgaan = tk.Button(self, text="doorgaan", command=self._login_btn_clicked)
        doorgaan.grid(columnspan=2)
        terug = tk.Button(self, text="terug", command=HoofdScherm.schermMainMenu)
        terug.grid(columnspan=2)

    def _login_btn_clicked(self):
        global entry_1
        global entry_2
        global pincode
        global fietsnr
        # print("Clicked")
        fietsnr = int(entry_1.get())
        pincode = int(entry_2.get())
        authcode = int(entry_3.get())


        theCursor.execute('SELECT * FROM Fietsenstalling WHERE FietsNr = ? AND PIN = ?', (fietsnr, pincode))
            # If nothing was found then c.fetchall() would be an empty list, which
            # evaluates to False
        s = set(theCursor.fetchall())
        theCursor.execute('SELECT otpKEY FROM Fietsenstalling WHERE FietsNr = ? AND PIN = ?', (fietsnr, pincode))
        otpKEY = theCursor.fetchone()
        controle = str(otpKEY[0])
        print(controle)
        if len(s) > 0:
            verif = controle_otp(controle, authcode)
            print(verif)
            if verif is True:
                HoofdScherm.schermFietsvrijgegeven()
        else:
            HoofdScherm.schermFietsNietVrijgegeven()
            print('Login failed')
        #print(username, password)


class FietsStallen(MainRender):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):

        global entry_3
        global entry_4

        label_1 = tk.Label(self, text="Wat is uw fietsnummer: ")
        label_2 = tk.Label(self, text="Wat uw pincode: ")

        entry_3 = (tk.Entry(self))
        entry_4 = (tk.Entry(self, show="*"))



        label_1.grid(row=0, sticky=tk.E)
        label_2.grid(row=1, sticky=tk.E)


        entry_3.grid(row=0, column=1)
        entry_4.grid(row=1, column=1)


        doorgaan = tk.Button(self, text="doorgaan", command=self._login_btn_clicked)
        doorgaan.grid(columnspan=2)
        terug = tk.Button(self, text="terug", command=HoofdScherm.schermMainMenu)
        terug.grid(columnspan=2)

    def _login_btn_clicked(self):
        global entry_3
        global entry_4
        global fietsnr
        global pincode


        fietsnr = int(entry_3.get())
        pincode = int(entry_4.get())


        theCursor.execute('SELECT * FROM Fietsenstalling WHERE FietsNr = ? AND PIN = ?' (fietsnr, pincode))

        s = set(theCursor.fetone())
        if len(s) > 0:
                HoofdScherm.schermFietsGestalt()
        elif geplaatst == 1:
            print('Uw fiets is al geplaatst')

        else:
            HoofdScherm.schermFietsNietGestalt()
            print('Login failed')

class fietsGestalt(MainRender):
    def __init__(self):
        super().__init__()
        self.initialize()
    def initialize(self):
        tk.Label(self, text="Uw fiets is gestalt").pack()
        tk.Button(self, text='Terug naar hoofdmenu', command=HoofdScherm.schermMainMenu)

class fietsNietGestalt(MainRender):
    def __init__(self):
        super().__init__()
        self.initialize()
    def initialize(self):
        tk.Button(self, text="Uw gegevens zijn onjuist, probeer opnieuw", command=HoofdScherm.schermFietsOphalen).pack()


class FietsGeregistreerd(MainRender):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        global ctrcode
        ctrcode = nieuwe_gebruiker()
        print(ctrcode)
        tk.Label(self, text='Uw fiets is succesvol geregistreerd. \nUw fietscode is '+ str(FietsNr) +' \nMiddels de volgende QR code kunt u Google Autenticator activeren.').pack()
        terug = tk.Button(self, text="verder", command=HoofdScherm.schermMainMenu)
        terug.pack()
        #Database.import_otp()
        img = Image.open("qrcode.png")
        render = ImageTk.PhotoImage(img)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=100, y=100)
        HoofdScherm.schermFietsGeinstalleerd


#frame for in window
class MainMenu(MainRender):
    def __init__(self):
        super().__init__()
        self.initialize()
    def initialize(self):
        butt1= tk.Button(self,text='Nieuwe Fiets', command=HoofdScherm.schermNieuweFiets).pack()
        butt2= tk.Button(self,text='Fiets Stallen', command=HoofdScherm.schermFietsStallen).pack()
        butt3= tk.Button(self, text="Fiets Ophalen", command=HoofdScherm.schermFietsOphalen).pack()

        img = Image.open("NStrans.png")
        render = ImageTk.PhotoImage(img)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=150, y=100)

class fietsVrijgegeven(MainRender):
    def __init__(self):
        super().__init__()
        self.initialize()
    def initialize(self):
        tk.Label(self, text="Uw fiets is vrijgegeven").pack()
        tk.Button(self, text='Terug naar hoofdmenu', command=HoofdScherm.schermMainMenu)

class fietsNietVrijgegeven(MainRender):
    def __init__(self):
        super().__init__()
        self.initialize()
    def initialize(self):
        tk.Button(self, text="Uw gegevens zijn onjuist, probeer opnieuw", command=HoofdScherm.schermFietsOphalen).pack()


#window
class HoofdScherm(tk.Frame):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        global Pag1
        global Pag2
        global Pag3
        global Pag4
        global Pag5
        global Pag6
        global Pag7
        global Pag8
        global Pag9

        Pag1 = NieuweFiets()
        Pag2 = FietsStallen()
        Pag3 = MainMenu()
        Pag4 = FietsOphalen()
        Pag5 = FietsGeregistreerd()
        Pag6 = fietsVrijgegeven()
        Pag7 = fietsNietVrijgegeven()
        Pag8 = fietsGestalt()
        Pag9 = fietsNietGestalt()

        self.buttonframe = tk.Frame(self)
        self.container = tk.Frame(self)
        self.buttonframe.pack(side='top', fill='x', expand=False)
        self.container.pack(side='top', fill='both', expand=True)

        Pag1.place(in_ = self.container, x=0, y=0, relwidth=1, relheight=1)
        Pag2.place(in_ = self.container, x=0, y=0, relwidth=1, relheight=1)
        Pag3.place(in_ = self.container, x=0, y=0, relwidth=1, relheight=1)
        Pag4.place(in_ = self.container, x=0, y=0, relwidth=1, relheight=1)
        Pag5.place(in_ = self.container, x=0, y=0, relwidth=1, relheight=1)
        Pag6.place(in_ = self.container, x=0, y=0, relwidth=1, relheight=1)
        Pag7.place(in_ = self.container, x=0, y=0, relwidth=1, relheight=1)
        Pag8.place(in_ = self.container, x=0, y=0, relwidth=1, relheight=1)
        Pag9.place(in_ = self.container, x=0, y=0, relwidth=1, relheight=1)

        Pag3.show()

    def schermNieuweFiets():
        Pag1.lift()
    def schermFietsOphalen():
        Pag4.lift()

    def schermMainMenu():
        Pag3.lift()

    def schermFietsStallen():
        Pag2.lift()

    def schermFietsGeinstalleerd():
        Pag5.lift()

    def schermFietsvrijgegeven():
        Pag6.lift()

    def schermFietsNietVrijgegeven():
        Pag7.lift()

    def schermFietsGestalt():
        Pag8.lift()

    def schermFietsNietGestalt():
        Pag9.lift()


if __name__ == "__main__":
    root=tk.Tk()
    main=HoofdScherm()

    main.pack(side='top', fill='both', expand=True)
    root.geometry('640x640')
    root.mainloop()

