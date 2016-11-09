#test
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        label_1 = Label(self, text="wat is uw fietsnummer: ")
        label_2 = Label(self, text="wat uw pincode: ")

        entry_1 = Entry(self)
        entry_2 = Entry(self, show="*")

        label_1.grid(row=0, sticky=E)
        label_2.grid(row=1, sticky=E)
        entry_1.grid(row=0, column=1)
        entry_2.grid(row=1, column=1)

        doorgaan = Button(self, text="doorgaan", command = self._login_btn_clicked)
        doorgaan.grid(columnspan=2)



        def _login_btn_clicked(self):
            # print("Clicked")
            fietsnr = self.entry_1.get()
            pincode = self.entry_2.get()

            # print(username, password)

            if fietsnr == "john" and pincode == "password":
                # functie controle_otp toekennen
            else:
                print("incorrect")
