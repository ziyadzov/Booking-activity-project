import sqlite3
import hashlib
def create():
    conn = sqlite3.connect("KSUCup.db")
    print("Opened database successfully")

    try:
        conn.execute('''
            CREATE TABLE ACCOUNT
                (
                    FirstName      CHAR(15)         NOT NULL,
                    LastName       CHAR(15)        NOT NULL,
                    ID              INT            NOT NULL,
                    Password        TEXT           NOT NULL,
                    Email           TEXT           NOT NULL,
                    PhoneNumber     INT            NOT NULL,
                    Admin           BOOL           NOT NULL,
                    PRIMARY KEY (ID),
                    UNIQUE(Email),
                    UNIQUE(PhoneNumber)
                );
        ''')

        print("Table created successfully")
        conn.execute('''
               CREATE TABLE EVENT
                   ( 
                       ID      INT         NOT NULL,
                       Name      CHAR(15)         NOT NULL,
                       Location       TEXT        NOT NULL,
                       Capacity       INT            NOT NULL,
                       CurrentCap       INT            NOT NULL,
                       Date        DATETIME           NOT NULL,
                       PRIMARY KEY (ID)
                   );
           ''')



        print("Table created successfully")
        conn.execute('''
                   CREATE TABLE BOOKINGS
                       ( 
                           SID      INT         NOT NULL,
                           EID      INT        NOT NULL,
                           CONSTRAINT PK PRIMARY KEY (SID,EID)
                           FOREIGN KEY (SID) REFERENCES ACCOUNT (ID)
                           FOREIGN KEY (EID) REFERENCES EVENT (ID)
                       );
               ''')

        print("Table created successfully")
    except sqlite3.OperationalError:
            print('Database has been created previously')
    try:
        AdminPassword='123456'
        HashPassword = hashlib.sha256(AdminPassword.encode()).hexdigest()
        conn.execute(f"INSERT INTO ACCOUNT (FirstName,LastName,ID,Password,Email,PhoneNumber,Admin)  VALUES ('Ziyad', 'Aseel',1234567890,'{HashPassword}', 'Admin@ksu.edu.sa','0555555555', TRUE );")
        conn.commit()
        conn.close()
        print("The admin account is created successfully ")
    except sqlite3.IntegrityError:
        print('The admin account has been created previously')

def CreateStudentAccount(fn,ln,id,pas,email,pn):
    conn = sqlite3.connect("KSUCup.db")
    try:
        conn.execute(f"INSERT INTO ACCOUNT (FirstName,LastName,ID,Password,Email,PhoneNumber,Admin)  VALUES ('{fn}' , '{ln}',{id},'{pas}','{email}','{pn}' ,FALSE);")
        conn.commit()
        conn.close()
        print("The account created Successfully")
        return True
    except sqlite3.IntegrityError:
        print("The  account created before")
        return False
def login(id):
    conn = sqlite3.connect("KSUCup.db")
    curser = conn.execute(f"select Password from ACCOUNT where {id} =ID ;")
    password =''
    for row in curser:
        password += row[0]

    return password

def isAdmin(id):
    conn = sqlite3.connect("KSUCup.db")
    curser = conn.execute(f"select Admin from ACCOUNT where {id} =ID ;")
    for row in curser:
        state = row[0]
    return state
def addEvent(id,name,location,capacity,date):
    conn = sqlite3.connect("KSUCup.db")
    try:
        conn.execute(f"INSERT INTO EVENT (ID,Name,Location,Capacity,CurrentCap,Date) VALUES ('{id}','{name}','{location}',{capacity},0,'{date}');")
        conn.commit()
        conn.close()
        print("The event created Successfully")
    except sqlite3.IntegrityError:
        print("The  event created before")
def addbooking(sid,eid):
    conn = sqlite3.connect("KSUCup.db")
    temp = conn.execute(f"SELECT Capacity, CurrentCap from EVENT where ID = '{eid}'")
    for i in temp:
        Cap = int(i[0])
        CuCap = int(i[1])

    if Cap <= CuCap:
        return -1
    try:
        conn.execute(f"INSERT INTO BOOKINGS (SID, EID) VALUES ('{sid}','{eid}');")
        conn.execute(f"UPDATE EVENT set CurrentCap = '{CuCap+1}' WHERE ID = '{eid}'")
        conn.commit()
        conn.close()
        print("The booking created Successfully")

        return 1
    except sqlite3.IntegrityError:
        print("The  booking created before")
        return -2
s= create()