import pandas as pd
import sqlite3
from tkinter import *
conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()
"""
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
a=list(df['Roll_no'])
b=list(df['Username'])
for i in range(len(a)):
    cur.execute('''INSERT OR IGNORE INTO RecordsEmail('Roll_no','Email') VALUES (?,?)''',(a[i],b[i],))
    print('Record generated for roll  no',a[i])
conn.commit()
input()


"""


def p_define_tble1():
    cur.execute('''
CREATE TABLE Records (Roll_no INTEGER PRIMARY KEY, book1 INTEGER DEFAULT 0, book2 INTEGER DEFAULT 0,
book3 INTEGER DEFAULT 0,book4 INTEGER DEFAULT 0,book5 INTEGER DEFAULT 0,DdI1 TEXT DEFAULT '00-00-0000',
DdI2 TEXT DEFAULT '00-00-0000',DdI3 TEXT DEFAULT '00-00-0000',DdI4 TEXT DEFAULT '00-00-0000',
DdI5 TEXT DEFAULT '00-00-0000')
''')
    conn.commit()
    b="Done new Table formed (table 1)"
    L2 = Label(root,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text =b)
    L2.place(x=150,y=290)

def p_define_tble2():
    cur.execute('''
CREATE TABLE RecordsEmail (Roll_no INTEGER PRIMARY KEY, Email TEXT)
''')
    conn.commit()
    b="Done new Table formed (table 2)"
    L2 = Label(root,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text =b)
    L2.place(x=150,y=290)




def p_transfer_data():
    data = pd.read_csv('data.csv')
    df = pd.DataFrame(data)
    a=list(df['Roll_no'])
    b=list(df['Username'])
    for i in range(len(a)):
        cur.execute('''INSERT OR IGNORE INTO RecordsEmail('Roll_no','Email') VALUES (?,?)''',(a[i],b[i],))
    conn.commit()
    b="Done data transfered to table 1 from data.csv. Records added= "+str(len(a))
    L2 = Label(root,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text =b)
    L2.place(x=150,y=290)


root = Tk()
root.title("Data_Management")
root.geometry("900x900")
a='''UNIVERSITY INSTITUTE OF ENGINEERING AND TECHNOLOGY
         KURUKSHETRA UNIVERSITY
             KURUKSHETRA'''
L = Label(root,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text =a)
L.place(x=150,y=10)

b1="Define a new table in Database for issuing info"
B_1 = Button(root,activebackground='Green',activeforeground='Red',width=53,bd=5,bg='Yellow',font=16, text =b1,command = p_define_tble1)
B_1.place(x=150,y=110)


b2="Define a new table in database for email info"
B_2 = Button(root,activebackground='Green',activeforeground='Red',width=53,bd=5,bg='Yellow',font=16, text =b2, command=p_define_tble2)
B_2.place(x=150,y=170)

b3 = "Transfering data into table from data.csv"
B_3 = Button(root,activebackground='Green',activeforeground='Red',width=53,bd=5,bg='Yellow',font=16, text =b3,command = p_transfer_data)
B_3.place(x=150,y=230)

root.mainloop()
