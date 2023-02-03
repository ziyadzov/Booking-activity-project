import hashlib
import tkinter as tk
import tkinter.messagebox
import Database
import re
class Signup:
    def __init__(self):
        #Main
        self.window =tk.Tk()
        self.window.title("Sign up")
        self.window.geometry('800x800')
        self.window.geometry("+600+200")
        self.window.configure(bg="light blue")
        self.window.resizable(False, False)

        self.errFName_var = tk.StringVar()
        self.errFName_var.set('')
        self.errLName_var = tk.StringVar()
        self.errLName_var.set('')
        self.errID_var = tk.StringVar()
        self.errID_var.set('')
        self.errPass_var = tk.StringVar()
        self.errPass_var.set('')
        self.errEmail_var = tk.StringVar()
        self.errEmail_var.set('')
        self.errPhone_var = tk.StringVar()
        self.errPhone_var.set('')

        # Frames
        self.SingUpFrame=tk.LabelFrame(self.window,text='Sing up', bg="light blue")
        self.FirstNameFrame=tk.Frame(self.SingUpFrame, pady=20, padx=20, bg="light blue")
        self.LastNameFrame = tk.Frame(self.SingUpFrame, pady=20, padx=20, bg="light blue")
        self.IDFrame = tk.Frame(self.SingUpFrame, pady=20, padx=20,  bg="light blue")
        self.PasswordFrame = tk.Frame(self.SingUpFrame, pady=20, padx=20, bg="light blue")
        self.EmailFrame = tk.Frame(self.SingUpFrame, pady=20, padx=20, bg="light blue")
        self.PhoneNumberFrame = tk.Frame(self.SingUpFrame, pady=20, padx=20, bg="light blue")
        self.ButtonsFrame= tk.Frame(self.SingUpFrame, pady=20, padx=20, bg="light blue")
        #Labels
        self.FirstNameLabel=tk.Label(self.FirstNameFrame,text="First name :       ",bg="light blue")
        self.LastNameLabel=tk.Label(self.LastNameFrame,text="Last name :       ",bg="light blue")
        self.IDLabel=tk.Label(self.IDFrame,text="Student ID :     ",bg="light blue")
        self.PasswordLabel = tk.Label(self.PasswordFrame, text="Password :         ", bg="light blue")
        self.EmailLabel = tk.Label(self.EmailFrame, text="Student Email :   ", bg="light blue")
        self.PhoneNumberLabel = tk.Label(self.PhoneNumberFrame, text="Phone number :", bg="light blue")

        # ERROR Labels
        self.erFirstNameLabel = tk.Label(self.FirstNameFrame, textvariable=self.errFName_var, bg="light blue",fg='red')
        self.erLastNameLabel = tk.Label(self.LastNameFrame, textvariable=self.errLName_var, bg="light blue",fg='red')
        self.erIDLabel = tk.Label(self.IDFrame,textvariable=self.errID_var, bg="light blue",fg='red')
        self.erPasswordLabel = tk.Label(self.PasswordFrame, textvariable=self.errPass_var, bg="light blue",fg='red')
        self.erEmailLabel = tk.Label(self.EmailFrame, textvariable=self.errEmail_var, bg="light blue",fg='red')
        self.erPhoneNumberLabel = tk.Label(self.PhoneNumberFrame, textvariable=self.errPhone_var, bg="light blue",fg='red')

        #Entery
        self.FirstNameEntery=tk.Entry(self.FirstNameFrame)
        self.LastNameEntery=tk.Entry(self.LastNameFrame)
        self.IDEntery=tk.Entry(self.IDFrame)
        self.PasswordEntery=tk.Entry(self.PasswordFrame)
        self.EmaiEntery=tk.Entry(self.EmailFrame)
        self.PhoneNumberEntery=tk.Entry(self.PhoneNumberFrame)
        #Buttons
        self.Submet=tk.Button(self.ButtonsFrame,text='Submit',command=self.SUBMIT)
        self.LogIn=tk.Button(self.ButtonsFrame,text='Login',command=self.go_Login)



        #Packing

        self.SingUpFrame.pack(fill="both",expand=True)

        self.FirstNameFrame.pack()
        self.LastNameFrame.pack()
        self.IDFrame.pack()
        self. PasswordFrame.pack()
        self.EmailFrame.pack()
        self.PhoneNumberFrame.pack()
        self.ButtonsFrame.pack()

        self.FirstNameLabel.pack(side="left")
        self.LastNameLabel.pack(side="left")
        self.IDLabel.pack(side="left")
        self.PasswordLabel.pack(side="left")
        self.EmailLabel.pack(side="left")
        self.PhoneNumberLabel.pack(side="left")

        self.erFirstNameLabel.pack(side="right",padx=10)
        self.erLastNameLabel.pack(side="right",padx=10)
        self.erIDLabel.pack(side="right",padx=10)
        self.erPasswordLabel.pack(side="right",padx=10)
        self.erEmailLabel.pack(side="right",padx=10)
        self.erPhoneNumberLabel.pack(side="right",padx=10)

        self.FirstNameEntery.pack(side="right")
        self.LastNameEntery.pack(side="right")
        self.IDEntery.pack(side="right")
        self.PasswordEntery.pack(side="right")
        self.EmaiEntery.pack(side="right")
        self.PhoneNumberEntery.pack(side="right")
        self.Submet.pack(side="left",padx=10)
        self.LogIn.pack(side="right",padx=10)

        tk.mainloop()
    def SUBMIT(self):
        self.errFName_var.set('')
        self.errLName_var.set('')
        self.errID_var.set('')
        self.errPass_var.set('')
        self.errEmail_var.set('')
        self.errPhone_var.set('')
        errcheck = 0
        if self.IsNotEmpty()==False:
            tkinter.messagebox.showerror("Error", "you should write all the information")
            errcheck = 1

        else:
            if self.TestFirstName()==False:
                self.errFName_var.set("Error: The first name \ncan only contain letters")
                errcheck = 1
            if self.TestLastName()==False:
                self.errLName_var.set("Error: The last name \ncan only contain letters")
                errcheck = 1
            if self.TestID()==False:
                self.errID_var.set("Error: The ID  can only \ncontain digits and must \nbe 10 positive digits")
                errcheck = 1
            if self.TestPassword()==False:
                self.errPass_var.set("Error: The length of \nthe password  must \nbe more than 5 ")
                errcheck = 1
            if self.TestEmail()==False:
                self.errEmail_var.set("Error: The length of \nthe Email  must be \nmore than 11 and must \nend with @ksu.edu.sa \nand the username of email \ncan only contain letters \nor digits or . or - or_ ")
                errcheck = 1
            if self.TestPhone()== False:
                self.errPhone_var.set("Error: The phone number \ncan only contain \ndigits and must be 10 \n positive digits and start with 05")
                errcheck = 1
            if errcheck ==0:
                HashPassword = hashlib.sha256(self.PasswordEntery.get().encode()).hexdigest()
                if Database.CreateStudentAccount(self.FirstNameEntery.get(),self.LastNameEntery.get(),self.IDEntery.get(),HashPassword,self.EmaiEntery.get(),self.PhoneNumberEntery.get())==True:
                    tkinter.messagebox.showinfo("Accept information", "The Account created successfully ")
                    self.window.destroy()
                    import Login
                else:
                    tkinter.messagebox.showerror("Error", "The  account created before")





    def go_Login(self):
        self.window.destroy()
        import Login


    def TestFirstName(self):
        Firstname = str(self.FirstNameEntery.get())
        RE1 = re.search("^[A-Za-z]{1,}$", Firstname)
        if(RE1):
            return True
        else:
            return False
    def TestLastName(self):
        Lastname = str(self.LastNameEntery.get())
        RE2 = re.search("^[A-Za-z]{1,}$", Lastname)
        if (RE2):
            return True
        else:
            return False
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

    def TestEmail(self):
        Email=str(self.EmaiEntery.get())
        RE3=re.search("^([a-zA-Z0-9\._-]+)(@ksu\.edu\.sa)$",Email)
        if (RE3):
            return True
        else:
            return False

    def TestPhone(self):
        phone = str(self.PhoneNumberEntery.get())

        if len(phone) != 10:
            return False
        if phone[:2] != "05":
            return False

        for p in phone:
            if not p.isdigit():
                return False

        return True
    def IsNotEmpty(self):
        FirstName=self.FirstNameEntery.get()
        LastName=self.LastNameEntery.get()
        ID=self.IDEntery.get()
        Password=self.PasswordEntery.get()
        Email=self.EmaiEntery.get()
        PhoneNumber=self.PhoneNumberEntery.get()
        if len(FirstName)!=0 and len(LastName)!=0 and len(ID)!=0 and len(Password)!=0 and len(Email)!=0 and len(PhoneNumber)!= 0:
            return True
        else:
            return False





Signup()




