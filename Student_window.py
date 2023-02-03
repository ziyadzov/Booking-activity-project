import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Database
from datetime import datetime
import logging

class Student_window:
    logging.basicConfig(filename='KSUCupLog.log', filemode='a', format='%(levelname)s - %(asctime)s - %(message)s',level=logging.INFO)
    def __init__(self,StID):
        self.StID = StID
        self.win = tk.Tk()
        self.win.configure(bg="cyan")
        self.win.title('KSUCup')
        self.win.geometry("800x800")
        self.win.geometry("+600+200")
        self.win.resizable(False, False)
        tabs = ttk.Notebook(self.win)
        bookticket = LabelFrame(tabs,bg="light blue")
        self.viewticket = LabelFrame(tabs,bg="light blue")
        tabs.add(bookticket, text="Book a ticket")
        tabs.add(self.viewticket, text="View my tickets")
        f = tk.Frame(bookticket,bg="light blue")
        f2 = tk.Frame(bookticket, bg="light blue")
        book_button = tk.Button(f,text="Book",command=self.book)
        logout_button = tk.Button(f, text="Logout",command=self.logout)
        self.errmsg = tk.StringVar()
        self.errmsg.set('')
        errLabel = tk.Label(f2,textvariable=self.errmsg,fg='red',bg='lightblue',font='25')
        tabs.pack(expand=True,fill="both")
        f2.pack(side='bottom')
        f.pack(side= 'bottom')

        errLabel.pack(side='left')
        book_button.pack(padx=10,pady=20,side="left")
        logout_button.pack(padx=10, pady=20)

        import Database
        conn = sqlite3.connect('KSUCup.db')
        self.tv = ttk.Treeview(bookticket,columns=(1,2,3,4), show='headings')

        self.tv.heading(1, text='Event ID:')
        self.tv.heading(2,text='Name:')
        self.tv.heading(3, text='Location:')
        self.tv.heading(4, text='Date:')
        cursor = conn.execute(f'select id,Name,Location, Date from EVENT where Date>"{datetime.now()}"')
        count = 0
        for row in cursor:
            self.tv.insert(parent='', index=  count, text='',values= (row[0],row[1],row[2],row[3]))
            count+=1
        f1 = tk.Frame(self.viewticket, bg="light blue")
        show_button = tk.Button(f1, text="Show",command=self.show)
        logout_button = tk.Button(f1, text="Logout", command=self.logout)
        tabs.pack(expand=True, fill="both")
        f1.pack(side='bottom')
        show_button.pack(padx=10, pady=20, side="left")
        logout_button.pack(padx=10, pady=20)
        self.tv1 = ttk.Treeview(self.viewticket, columns=(1, 2, 3, 4), show='headings')

        self.tv.pack(side='right')
        self.win.mainloop()


    def book(self):
        self.errmsg.set('')
        try:
            selectedItem = self.tv.focus()
            self.Temp1 = self.tv.item(selectedItem)
            EID = self.Temp1['values'][0]
            NAME=self.Temp1['values'][1]
            LOCATION=self.Temp1['values'][2]
            temp2 = Database.addbooking(self.StID, EID)
            if temp2 ==1 :
                self.errmsg.set('Event booked successfully!')
                logging.info(f"The student {self.StID} has booked the event: {NAME} located in {LOCATION} ")
            elif temp2 == -2:
                self.errmsg.set('Error: you already booked this event!')
            elif temp2 == -1:
                self.errmsg.set('Error: The event is full!')

        except :
            self.errmsg.set('Error: you must select an event')

    def show(self):
        conn = sqlite3.connect('KSUCup.db')
        self.tv1.destroy()
        self.tv1 = ttk.Treeview(self.viewticket, columns=(1, 2, 3, 4), show='headings')
        self.tv1.heading(1, text='Event:')
        self.tv1.heading(2, text='Name:')
        self.tv1.heading(3, text='Location:')
        self.tv1.heading(4, text='Date:')

        cursor = conn.execute(
            f"select Name,Location, Date ,id from EVENT, BOOKINGS where SID = '{self.StID}' AND EID = id and Date>'{datetime.now()}' ")
        count = 0
        for row in cursor:
            self.tv1.insert(parent='', index=count, text='', values=(str(count + 1), row[0], row[1], row[2], row[3]))
            count += 1
        conn.close()
        self.tv1.pack()
    def logout(self):
        self.win.destroy()
        import Signup
