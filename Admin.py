import tkinter as tk
import tkinter.messagebox
import Database
import random
import re
import sqlite3
import csv
from datetime import datetime
class Admin:
    def __init__(self):
        self.win = tk.Tk()
        self.win.configure(bg="cyan")
        self.win.title('KSUCup')
        self.win.geometry("800x800")
        self.win.geometry("+600+200")
        self.win.resizable(False,False)

        #main_frame
        win_frame = tk.Frame(self.win, bg="cyan" )

        #form frames
        lapel_frame = tk.LabelFrame(win_frame, text="Admin", bg="lightblue")
        event_name_frame = tk.Frame(lapel_frame, pady=20, padx=20, bg="lightblue")
        event_location_frame = tk.Frame(lapel_frame, pady=20, padx=20, bg="lightblue")
        event_capacity_frame = tk.Frame(lapel_frame, pady=20, padx=20, bg="lightblue")
        event_date_frame = tk.Frame(lapel_frame, pady=20, padx=20, bg="lightblue")
        botton_frame = tk.Frame(lapel_frame, pady=200, padx=200, bg="lightblue")

        #variables
        self.name_var = tk.StringVar()
        self.location_var = tk.StringVar()
        self.capacity_var = tk.StringVar()
        self.date_var = tk.StringVar()

        self.errName_var = tk.StringVar()
        self.errName_var.set('')
        self.errL_var = tk.StringVar()
        self.errL_var.set('')
        self.errC_var = tk.StringVar()
        self.errC_var.set('')
        self.errD_var = tk.StringVar()
        self.errD_var.set('')
        #entry
        event_name_promt = tk.Label(event_name_frame,bg="lightblue", text="Event Name:      ")
        event_name_box = tk.Entry(event_name_frame,textvariable=self.name_var)
        err_name_promt = tk.Label(event_name_frame, bg="lightblue", textvariable=self.errName_var,fg='red')

        event_location_promt = tk.Label(event_location_frame, bg="lightblue", text="Event Location: ")
        event_location_box = tk.Entry(event_location_frame,textvariable=self.location_var)
        err_location_promt = tk.Label(event_location_frame, bg="lightblue", textvariable=self.errL_var,fg='red')

        event_capacity_promt = tk.Label(event_capacity_frame, bg="lightblue", text="Event Capacity: ")
        event_capacity_box = tk.Entry(event_capacity_frame,textvariable=self.capacity_var)
        err_capacity_promt = tk.Label(event_capacity_frame, bg="lightblue", textvariable=self.errC_var,fg='red')

        event_date_promt = tk.Label(event_date_frame, bg="lightblue", text="Event Date:        ")
        event_date_box = tk.Entry(event_date_frame,textvariable=self.date_var)
        err_date_promt = tk.Label(event_date_frame, bg="lightblue", textvariable=self.errD_var,fg='red')

        #bottons
        create_button = tk.Button(botton_frame,text="Create",command=self.create)
        logout_button = tk.Button(botton_frame,text="Logout", command=self.logout)
        backup_btn = tk.Button(botton_frame,text="Backup",command=self.backup)





        lapel_frame.pack(ipadx=400,ipady=400)
        event_name_frame.pack()
        event_location_frame.pack()
        event_location_promt.pack(side="left")
        event_location_box.pack(side="left")
        event_capacity_frame.pack()
        event_capacity_promt.pack(side="left")
        event_capacity_box.pack(side="left")
        event_name_promt.pack(side="left")
        event_name_box.pack(side="left")
        event_date_frame.pack()
        event_date_promt.pack(side="left")
        event_date_box.pack(side="left")
        botton_frame.pack()
        create_button.pack(side="left",padx=10)
        logout_button.pack(side="left",padx=10)
        backup_btn.pack(padx=10,side="right")
        err_date_promt.pack(padx=10,side="right")
        err_capacity_promt.pack(padx=10,side="right")
        err_location_promt.pack(padx=10,side="right")
        err_name_promt.pack(padx=10,side="right")
        win_frame.pack()
        self.win.mainloop()

    def logout(self):
        self.win.destroy()
        import Signup

    def create(self):
        self.errName_var.set('')
        self.errL_var.set('')
        self.errC_var.set('')
        self.errD_var.set('')
        errcheck=0
        if not self.checkname():
            self.errName_var.set("Error: Enter event name ")
            errcheck=1
        if not self.checklocation():
            self.errL_var.set("Error: Enter event location ")
            errcheck = 1
        if  self.checkcapacity() == -2:
            self.errC_var.set("Error: Enter event capacity ")
            errcheck = 1
        elif self.checkcapacity() ==-1:
            self.errC_var.set("Error: Capacity must be a positive number! ")
            errcheck = 1
        if self.checkdate()==-2:
            self.errD_var.set("Error: Enter event date ")
            errcheck = 1
        elif self.checkdate()==-1:
            self.errD_var.set("Error:The Date should be in this\n format YYYY-MM-DD HH:MM:SS\n For Example: 2022-04-06 07:03:00")
            errcheck = 1
        if errcheck==0:
            id =random.randrange(10000,99999)
            Database.addEvent(id,self.name_var.get(),self.location_var.get(),self.capacity_var.get(),self.date_var.get())
            tk.messagebox.showinfo("Information Accept","Event created successfully ")
            self.name_var.set("")
            self.location_var.set("")
            self.capacity_var.set("")
            self.date_var.set("")


    def checkname(self):
        if len(self.name_var.get())==0:
            return False
        return True
    def checklocation(self):
        if len(self.location_var.get())==0:
            return False
        return True
    def checkcapacity(self):
        if len(self.capacity_var.get())==0:
            return -2
        elif not self.capacity_var.get().isdigit():
            return -1
        return 1
    def checkdate(self):
        if len(self.date_var.get())==0:
            return -2
        Date=self.date_var.get()
        VilidDate=re.search("^20[0-9][0-9]-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]) (0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$",Date)
        if not (VilidDate):
            return -1
        return 1
    def backup(self):
        conn = sqlite3.connect('KSUCup.db')
        f = open("KSUCupBackup.csv", 'a', newline="")
        data = csv.writer(f)

        Spliter1 =["____________________________________________________"]
        data.writerow(Spliter1)

        time = [f"Time: {datetime.now()}"]
        data.writerow(time)

        for T in "ACCOUNT", "EVENT", "BOOKINGS":
            Spliter1 = ["_______________________"]
            data.writerow(Spliter1)
            data.writerow([f"{T} table"])
            D = conn.execute(f"SELECT * FROM {T}")
            for x in D:
                data.writerow(x)
        f.close()
        tkinter.messagebox.showinfo(message="Backup is Done")

Admin()