import tkinter as tk
import tkinter.messagebox
import hashlib
import Database
class Login:
    def __init__(self):
        #Main
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.geometry('800x800')
        self.window.geometry("+600+200")
        self.window.resizable(False, False)
        self.window.configure(bg="blue")

        #variavles
        self.errID_var = tk.StringVar()
        self.errID_var.set('')
        self.errPass_var = tk.StringVar()
        self.errPass_var.set('')

        #Frames


        self.LogINFrame =  tk.LabelFrame( text='Log in', bg="light blue")
        self.IDFrame = tk.Frame(self.LogINFrame, pady=20, padx=20, bg="light blue")
        self.PasswordFrame = tk.Frame(self.LogINFrame, pady=20, padx=20, bg="light blue")
        self.ButtonsFrame = tk.Frame(self.LogINFrame, pady=20, padx=20, bg="light blue")

        #Labels
        self.IDLabel = tk.Label(self.IDFrame, text="Student ID :", bg="light blue")
        self.PasswordLabel = tk.Label(self.PasswordFrame, text="Password : ", bg="light blue")

        # ERROR Labels
        self.erIDLabel = tk.Label(self.IDFrame, textvariable=self.errID_var, bg="light blue",fg='red')
        self.erPasswordLabel = tk.Label(self.PasswordFrame, textvariable=self.errPass_var, bg="light blue",fg='red')

        #Entery
        self.IDEntery = tk.Entry(self.IDFrame)
        self.PasswordEntery = tk.Entry(self.PasswordFrame)

        # Buttons
        self.buttonBack = tk.Button(self.ButtonsFrame, text='Signup', command=self.go_signup)
        self.buttonLogin = tk.Button(self.ButtonsFrame, text='Login', command=self.LOGON)
        # Packing

        self.LogINFrame.pack(expand="yes",fill="both")

        self.IDFrame.pack()
        self.PasswordFrame.pack()
        self.ButtonsFrame.pack()


        self.IDLabel.pack(side="left")
        self.PasswordLabel.pack(side="left")
        self.buttonBack.pack(side="right",padx=10)
        self.buttonLogin.pack(side="left",padx=10)
        self.erIDLabel.pack(side="right",padx=10)
        self.erPasswordLabel.pack(side="right",padx=10)

        self.IDEntery.pack(side="right",)
        self.PasswordEntery.pack(side="right")


        self.buttonBack.pack()
        self.window.mainloop()



    def go_signup(self):
        self.window.destroy()
        import Signup

    def LOGON(self):
        self.errID_var.set('')
        self.errPass_var.set('')
        errcheck =0
        if self.IsNotEmpty() == False:
            tkinter.messagebox.showerror("Error", "you should write all the information")
            errcheck = 1
        if self.TestID() == False:
            self.errID_var.set("Error: The ID  can not contain\n letters and must be 10 positive digits")
            errcheck = 1
        if self.TestPassword() == False:
            self.errPass_var.set("Error: The length of the \npassword  must be more than 5 ")
            errcheck = 1
        if errcheck ==0:
            password = Database.login(self.IDEntery.get())
            HashPassword = hashlib.sha256(self.PasswordEntery.get().encode()).hexdigest()
            if(password == HashPassword):
                if Database.isAdmin(self.IDEntery.get()):
                    self.window.destroy()
                    import Admin
                else:
                    Stid = str(self.IDEntery.get())
                    self.window.destroy()
                    import Student_window
                    s = Student_window.Student_window(Stid)
            else:
                tkinter.messagebox.showerror("Error", "Wrong password or ID ")



    def TestID(self):
        ID = str(self.IDEntery.get())
        if len(ID) != 10:
            return False
        for i in ID:
            if not i.isdigit():
                return False
        return True
    def TestPassword(self):
        Password = str(self.PasswordEntery.get())
        if len(Password) < 6:
            return False
        return True

    def IsNotEmpty(self):
        ID = self.IDEntery.get()
        Password = self.PasswordEntery.get()
        if  len(ID) != 0 and len(Password) != 0 :
            return True
        else:
            return False
Login()

