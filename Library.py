from tkinter import *
import sqlite3
import getpass
from functools import partial
from datetime import date

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()
def passw():
    pa=getpass.getpass()
    passwo='seKde7sSG'
    print('Entered password is of ',len(pa),' characters, To continue press Enter otherwise Enter the passwords again')
    s=input()
    while s:
        print('Enter the correct password again: ')
        pa=getpass.getpass()
        print('Entered password is of ',len(pa),' characters, To continue press Enter otherwise Enter the passwords again')
        s=input()
    if pa==passwo:
        return 1;
    else:
        return 0;

def p_exit():
    exit()


def p_add1():
    add1=Tk()
    add1.title("Add records")
    add1.geometry("900x300")
    def p_ad():
        i=int(E_2.get())
        cur.execute('''INSERT OR IGNORE INTO Records('Roll_no') VALUES (?)''',(i,))
        conn.commit()
        L_ = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = E_2.get()+" Added")
        L_.place(x=10,y=150)
        
    L1 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Roll Number to add: ")
    L1.place(x=50,y=10)
    E_2 = Entry(add1,font=16,textvariable = b)
    E_2.place(x=410,y=10)
    B_1 = Button(add1,activebackground='Green',activeforeground='Red',width=5,bd=5,bg='Yellow',font=16, text = "Add",command = p_ad)
    B_1.place(x=350,y=100)
    add1.mainloop()


def p_addrng():
    add1=Tk()
    add1.title("Add records")
    add1.geometry("900x300")
    def p_ad():
        i=int(E_2.get())
        j=int(E_3.get())
        for k in range(i,j+1):
            cur.execute('''INSERT OR IGNORE INTO Records('Roll_no') VALUES (?)''',(k,))
        conn.commit()
        L_ = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = str(j-i+1)+" Recods Added")
        L_.place(x=10,y=250)
        
    L1 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Initial Roll number")
    L1.place(x=50,y=10)
    E_2 = Entry(add1,font=16,textvariable = b)
    E_2.place(x=410,y=10)
    L2 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Final Roll number")
    L2.place(x=50,y=100)
    E_3 = Entry(add1,font=16,textvariable = c)
    E_3.place(x=410,y=100)
    B_1 = Button(add1,activebackground='Green',activeforeground='Red',width=5,bd=5,bg='Yellow',font=16, text = "Add",command = p_ad)
    B_1.place(x=350,y=190)
    add1.mainloop()


def p_del1():
    add1=Tk()
    add1.title("Delete records")
    add1.geometry("900x300")
    def p_ad():
        i=int(E_2.get())
        cur.execute('''DELETE FROM Records where Roll_no = ?''',(i,))
        conn.commit()
        L_ = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = E_2.get()+" Deleted")
        L_.place(x=10,y=150)
        
    L1 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Roll Number to delete: ")
    L1.place(x=50,y=10)
    E_2 = Entry(add1,font=16,textvariable = b)
    E_2.place(x=410,y=10)
    B_1 = Button(add1,activebackground='Green',activeforeground='Red',width=5,bd=5,bg='Yellow',font=16, text = "Delete",command = p_ad)
    B_1.place(x=350,y=100)
    add1.mainloop()


def p_delrng():
    add1=Tk()
    add1.title("Delete records")
    add1.geometry("900x300")
    def p_ad():
        i=int(E_2.get())
        j=int(E_3.get())
        for k in range(i,j+1):
            cur.execute('''DELETE FROM Records where Roll_no = ?''',(k,))
        conn.commit()
        L_ = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = str(j-i+1)+" Recods Deleted")
        L_.place(x=10,y=250)
        
    L1 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Initial Roll number")
    L1.place(x=50,y=10)
    E_2 = Entry(add1,font=16,textvariable = b)
    E_2.place(x=410,y=10)
    L2 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Final Roll number")
    L2.place(x=50,y=100)
    E_3 = Entry(add1,font=16,textvariable = c)
    E_3.place(x=410,y=100)
    B_1 = Button(add1,activebackground='Green',activeforeground='Red',width=5,bd=5,bg='Yellow',font=16, text = "Delete",command = p_ad)
    B_1.place(x=350,y=190)
    add1.mainloop()



def p_issue():
    add1=Tk()
    add1.title("Issue Books")
    add1.geometry("900x900")

    def p_book():
        i=int(E_2.get())
        row =conn.execute('''select * from Records where Roll_no = ?''',(i,))
        book1 = 0
        book2 = 0
        book3 = 0
        book4 = 0
        book5 = 0
        for rec in row:
            book1=rec[1]
            book2=rec[2]
            book3=rec[3]
            book4=rec[4]
            book5=rec[5]
            break
        mpty=0
        if book1==0:
            mpty+=1
        if book2==0:
            mpty+=1
        if book3==0:
            mpty+=1
        if book4==0:
            mpty+=1
        if book5==0:
            mpty+=1
        tt='You can issue '+str(mpty)+' number of books only as per the rule.'

        def p_lock():
            i=int(E_2.get())
            row =conn.execute('''select * from Records where Roll_no = ?''',(i,))
            book1 = 0
            book2 = 0
            book3 = 0
            book4 = 0
            book5 = 0
            for rec in row:
                book1=rec[1]
                book2=rec[2]
                book3=rec[3]
                book4=rec[4]
                book5=rec[5]
                break
            b1=E_3.get()
            b2=E_4.get()
            b3=E_5.get()
            b4=E_6.get()
            b5=E_7.get()
            aaa=0
            if b1=="":
                aaa+=1
            if b2=="":
                aaa+=1
            if b3=="":
                aaa+=1
            if b4=="":
                aaa+=1
            if b5=="":
                aaa+=1
            L8 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Books for issue= "+str(5-aaa))
            L8.place(x=50,y=510)
            aaa=5-aaa
            lst=[]
            if aaa==5:
                lst.append(b1)
                lst.append(b2)
                lst.append(b3)
                lst.append(b4)
                lst.append(b5)
            elif aaa==4:
                lst.append(b1)
                lst.append(b2)
                lst.append(b3)
                lst.append(b4)
            elif aaa==3:
                lst.append(b1)
                lst.append(b2)
                lst.append(b3)
            elif aaa==2:
                lst.append(b1)
                lst.append(b2)
            elif aaa==1:
                lst.append(b1)

            for j in range(len(lst)):
                aaa-=1
                if book1==0:
                    book1=lst[j]
                    di=date.today().strftime("%d-%m-%Y")
                    conn.execute('''UPDATE Records set book1=? where Roll_no=?''',(lst[j],i,))
                    conn.execute('''UPDATE Records set DdI1=? where Roll_no=?''',(di,i))
                    conn.commit()
                elif book2==0:
                    book2=lst[j]
                    di=date.today().strftime("%d-%m-%Y")
                    conn.execute('''UPDATE Records set book2=? where Roll_no=?''',(lst[j],i,))
                    conn.execute('''UPDATE Records set DdI2=? where Roll_no=?''',(di,i))
                    conn.commit()
                elif book3==0:
                    book3=lst[j]
                    di=date.today().strftime("%d-%m-%Y")
                    conn.execute('''UPDATE Records set book3=? where Roll_no=?''',(lst[j],i,))
                    conn.execute('''UPDATE Records set DdI3=? where Roll_no=?''',(di,i))
                    conn.commit()
                elif book4==0:
                    book4=lst[j]
                    di=date.today().strftime("%d-%m-%Y")
                    conn.execute('''UPDATE Records set book4=? where Roll_no=?''',(lst[j],i,))
                    conn.execute('''UPDATE Records set DdI4=? where Roll_no=?''',(di,i))
                    conn.commit()
                elif book5==0:
                    book5=lst[j]
                    di=date.today().strftime("%d-%m-%Y")
                    conn.execute('''UPDATE Records set book5=? where Roll_no=?''',(lst[j],i,))
                    conn.execute('''UPDATE Records set DdI5=? where Roll_no=?''',(di,i))
                    conn.commit()

            L9 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Books issued= "+str(len(lst)))
            L9.place(x=50,y=570)

        L2 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = tt)
        L2.place(x=50,y=180)
        L3 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Book1")
        L3.place(x=50,y=260)
        E_3 = Entry(add1,font=16)
        E_3.place(x=410,y=260)
        L4 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Book2")
        L4.place(x=50,y=310)
        E_4 = Entry(add1,font=16)
        E_4.place(x=410,y=310)
        L5 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Book3")
        L5.place(x=50,y=360)
        E_5 = Entry(add1,font=16)
        E_5.place(x=410,y=360)
        L6 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Book4")
        L6.place(x=50,y=410)
        E_6 = Entry(add1,font=16)
        E_6.place(x=410,y=410)
        L7 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Book5")
        L7.place(x=50,y=460)
        E_7 = Entry(add1,font=16)
        E_7.place(x=410,y=460)
        B_2 = Button(add1,activebackground='Green',activeforeground='Red',width=5,bd=5,bg='Yellow',font=16, text = "Book",command = p_lock)
        B_2.place(x=350,y=510)
    
    L1 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Roll number")
    L1.place(x=50,y=10)
    E_2 = Entry(add1,font=16,textvariable = b)
    E_2.place(x=410,y=10)
    B_1 = Button(add1,activebackground='Green',activeforeground='Red',width=10,bd=5,bg='Yellow',font=16, text = "Continue",command = p_book)
    B_1.place(x=350,y=100)



def p_delete():
    add1=Tk()
    add1.title("Return book")
    add1.geometry("900x900")
    def p_del():
        i=int(E_2.get())
        row =conn.execute('''select * from Records where Roll_no = ?''',(i,))
        book1 = 0
        book2 = 0
        book3 = 0
        book4 = 0
        book5 = 0
        for rec in row:
            book1=rec[1]
            book2=rec[2]
            book3=rec[3]
            book4=rec[4]
            book5=rec[5]
            break
        strr=""
        if book1!=0:
            strr=strr+str(book1)+','
        if book2!=0:
            strr=strr+str(book2)+','
        if book3!=0:
            strr=strr+str(book3)+','
        if book4!=0:
            strr=strr+str(book4)+','
        if book5!=0:
            strr=strr+str(book5)
        strr='You have these books issued '+strr

        def p_cal():
            i=int(E_2.get())
            row =conn.execute('''select * from Records where Roll_no = ?''',(i,))
            book1 = 0
            book2 = 0
            book3 = 0
            book4 = 0
            book5 = 0
            for rec in row:
                book1=rec[1]
                book2=rec[2]
                book3=rec[3]
                book4=rec[4]
                book5=rec[5]
                d1=rec[6]
                d2=rec[7]
                d3=rec[8]
                d4=rec[9]
                d5=rec[10]
                break
            b1=E_3.get()
            b2=E_4.get()
            b3=E_5.get()
            b4=E_6.get()
            b5=E_7.get()
            aaa=0
            if b1=="":
                aaa+=1
            if b2=="":
                aaa+=1
            if b3=="":
                aaa+=1
            if b4=="":
                aaa+=1
            if b5=="":
                aaa+=1
            aaa=5-aaa
            lst=[]
            if aaa==5:
                lst.append(int(b1))
                lst.append(int(b2))
                lst.append(int(b3))
                lst.append(int(b4))
                lst.append(int(b5))
            elif aaa==4:
                lst.append(int(b1))
                lst.append(int(b2))
                lst.append(int(b3))
                lst.append(int(b4))
            elif aaa==3:
                lst.append(int(b1))
                lst.append(int(b2))
                lst.append(int(b3))
            elif aaa==2:
                lst.append(int(b1))
                lst.append(int(b2))
            elif aaa==1:
                lst.append(int(b1))
            dys_free=0
            total=0
            for j in range(len(lst)):
                if book1==lst[j]:
                    r_dat=date.today()
                    a=int(d1[6:])
                    b=int(d1[3:5])
                    c=int(d1[:2])
                    i_dat=date(a,b,c)
                    delta=r_dat-i_dat
                    dys=delta.days
                    if dys>dys_free:
                        dys=dys-dys_free
                    else:
                        dys=0
                    total+=0.50*dys
                elif book2==lst[j]:
                    r_dat=date.today()
                    a=int(d2[6:])
                    b=int(d2[3:5])
                    c=int(d2[:2])
                    i_dat=date(a,b,c)
                    delta=r_dat-i_dat
                    dys=delta.days
                    if dys>dys_free:
                        dys=dys-dys_free
                    else:
                        dys=0
                    total+=0.50*dys
                elif book3==lst[j]:
                    r_dat=date.today()
                    a=int(d3[6:])
                    b=int(d3[3:5])
                    c=int(d3[:2])
                    i_dat=date(a,b,c)
                    delta=r_dat-i_dat
                    dys=delta.days
                    if dys>dys_free:
                        dys=dys-dys_free
                    else:
                        dys=0
                    total+=0.50*dys
                elif book4==lst[j]:
                    r_dat=date.today()
                    a=int(d4[6:])
                    b=int(d4[3:5])
                    c=int(d4[:2])
                    i_dat=date(a,b,c)
                    delta=r_dat-i_dat
                    dys=delta.days
                    if dys>dys_free:
                        dys=dys-dys_free
                    else:
                        dys=0
                    total+=0.50*dys
                elif book5==lst[j]:
                    r_dat=date.today()
                    a=int(d5[6:])
                    b=int(d5[3:5])
                    c=int(d5[:2])
                    i_dat=date(a,b,c)
                    delta=r_dat-i_dat
                    dys=delta.days
                    if dys>dys_free:
                        dys=dys-dys_free
                    else:
                        dys=0
                    total+=0.50*dys
            def p_conf():
                i=int(E_2.get())
                row =conn.execute('''select * from Records where Roll_no = ?''',(i,))
                book1 = 0
                book2 = 0
                book3 = 0
                book4 = 0
                book5 = 0
                for rec in row:
                    book1=rec[1]
                    book2=rec[2]
                    book3=rec[3]
                    book4=rec[4]
                    book5=rec[5]
                    d1=rec[6]
                    d2=rec[7]
                    d3=rec[8]
                    d4=rec[9]
                    d5=rec[10]
                    break
                b1=E_3.get()
                b2=E_4.get()
                b3=E_5.get()
                b4=E_6.get()
                b5=E_7.get()
                aaa=0
                if b1=="":
                    aaa+=1
                if b2=="":
                    aaa+=1
                if b3=="":
                    aaa+=1
                if b4=="":
                    aaa+=1
                if b5=="":
                    aaa+=1
                aaa=5-aaa
                lst=[]
                if aaa==5:
                    lst.append(int(b1))
                    lst.append(int(b2))
                    lst.append(int(b3))
                    lst.append(int(b4))
                    lst.append(int(b5))
                elif aaa==4:
                    lst.append(int(b1))
                    lst.append(int(b2))
                    lst.append(int(b3))
                    lst.append(int(b4))
                elif aaa==3:
                    lst.append(int(b1))
                    lst.append(int(b2))
                    lst.append(int(b3))
                elif aaa==2:
                    lst.append(int(b1))
                    lst.append(int(b2))
                elif aaa==1:
                    lst.append(int(b1))
                for j in range(len(lst)):
                    if book1==lst[j]:
                        conn.execute('''UPDATE Records set 'book1'=? where Roll_no=?''',(0,i,))
                        conn.execute('''UPDATE Records set 'DdI1'=? where Roll_no=?''',('00-00-0000',i,))
                        conn.commit()
                    elif book2==lst[j]:
                        conn.execute('''UPDATE Records set 'book2'=? where Roll_no=?''',(0,i,))
                        conn.execute('''UPDATE Records set 'DdI2'=? where Roll_no=?''',('00-00-0000',i,))
                        conn.commit()
                    elif book3==lst[j]:
                        conn.execute('''UPDATE Records set 'book3'=? where Roll_no=?''',(0,i,))
                        conn.execute('''UPDATE Records set 'DdI3'=? where Roll_no=?''',('00-00-0000',i,))
                        conn.commit()
                    elif book4==lst[j]:
                        conn.execute('''UPDATE Records set 'book4'=? where Roll_no=?''',(0,i,))
                        conn.execute('''UPDATE Records set 'DdI4'=? where Roll_no=?''',('00-00-0000',i,))
                        conn.commit()
                    elif book5==lst[j]:
                        conn.execute('''UPDATE Records set 'book5'=? where Roll_no=?''',(0,i,))
                        conn.execute('''UPDATE Records set 'DdI5'=? where Roll_no=?''',('00-00-0000',i,))
                        conn.commit()
                L9 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "done")
                L9.place(x=350,y=720)
            L8 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Total fine: "+str(total))
            L8.place(x=50,y=580)
            B_2 = Button(add1,activebackground='Green',activeforeground='Red',width=7,bd=5,bg='Yellow',font=16, text = "Confirm",command = p_conf)
            B_2.place(x=350,y=650)
            

        L2 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = strr)
        L2.place(x=50,y=180)
        L3 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Book1")
        L3.place(x=50,y=260)
        E_3 = Entry(add1,font=16)
        E_3.place(x=410,y=260)
        L4 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Book2")
        L4.place(x=50,y=310)
        E_4 = Entry(add1,font=16)
        E_4.place(x=410,y=310)
        L5 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Book3")
        L5.place(x=50,y=360)
        E_5 = Entry(add1,font=16)
        E_5.place(x=410,y=360)
        L6 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Book4")
        L6.place(x=50,y=410)
        E_6 = Entry(add1,font=16)
        E_6.place(x=410,y=410)
        L7 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Book5")
        L7.place(x=50,y=460)
        E_7 = Entry(add1,font=16)
        E_7.place(x=410,y=460)
        B_2 = Button(add1,activebackground='Green',activeforeground='Red',width=5,bd=7,bg='Yellow',font=16, text = "Return",command = p_cal)
        B_2.place(x=350,y=510)


    L1 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Roll number")
    L1.place(x=50,y=10)
    E_2 = Entry(add1,font=16,textvariable = b)
    E_2.place(x=410,y=10)
    B_1 = Button(add1,activebackground='Green',activeforeground='Red',width=10,bd=5,bg='Yellow',font=16, text = "Continue",command = p_del)
    B_1.place(x=350,y=100)


def p_mail():
    add1=Tk()
    add1.title("Mail to students")
    add1.geometry("700x300")
    import smtplib
    row =conn.execute('''select * from Records''')
    lst1=[]
    for rec in row:
        mpty=0
        book1=rec[1]
        d1=rec[6]
        book2=rec[2]
        d2=rec[7]
        book3=rec[3]
        d3=rec[8]
        book4=rec[4]
        d4=rec[9]
        book5=rec[5]
        d5=rec[10]
        if book1!=0:
            mpty+=1
        if book2!=0:
            mpty+=1
        if book3!=0:
            mpty+=1
        if book4!=0:
            mpty+=1
        if book5!=0:
            mpty+=1
        total=0
        free_days=0
        for i in range(mpty):
            if book1 !=0:
                r_dat=date.today()
                a=int(d1[6:])
                b=int(d1[3:5])
                c=int(d1[:2])
                i_dat=date(a,b,c)
                delta=r_dat-i_dat
                dys=delta.days
                if dys>free_days:
                    dys=dys-free_days
                else:
                    dys=0
                total+=0.50*dys
            elif book2 !=0:
                r_dat=date.today()
                a=int(d2[6:])
                b=int(d2[3:5])
                c=int(d2[:2])
                i_dat=date(a,b,c)
                delta=r_dat-i_dat
                dys=delta.days
                if dys>free_days:
                    dys=dys-free_days
                else:
                   dys=0
                total+=0.50*dys
            elif book3 !=0:
                r_dat=date.today()
                a=int(d3[6:])
                b=int(d3[3:5])
                c=int(d3[:2])
                i_dat=date(a,b,c)
                delta=r_dat-i_dat
                dys=delta.days
                if dys>free_days:
                    dys=dys-free_days
                else:
                    dys=0
                total+=0.50*dys
            elif book4 !=0:
                r_dat=date.today()
                a=int(d4[6:])
                b=int(d4[3:5])
                c=int(d4[:2])
                i_dat=date(a,b,c)
                delta=r_dat-i_dat
                dys=delta.days
                if dys>free_days:
                    dys=dys-free_days
                else:
                    dys=0
                total+=0.50*dys
            elif book5 == lst1[i]:
                r_dat=date.today()
                a=int(d5[6:])
                b=int(d5[3:5])
                c=int(d5[:2])
                i_dat=date(a,b,c)
                delta=r_dat-i_dat
                dys=delta.days
                if dys>free_days:
                    dys=dys-free_days
                else:
                    dys=0
                total+=0.50*dys
        if total!=0:
            lst1.append(rec[0])
    lst2=[]
    for rrol in lst1:
        row =conn.execute('''select * from RecordsEmail where Roll_no=?''',(rrol,))
        for rec in row:
            eme=rec[1]
            lst2.append(eme)
    lstt=lst2
    L1 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text =str(len(lstt))+" are number of students whose fine started.")
    L1.place(x=10,y=10)
    sender = "systemlibrary567@gmail.com"
    recipient = lstt
    password = getpass.getpass() # Your SMTP password for Gmail
    subject = "UIET KUK LIBRARY"
    text = '''
Dear student,
This is gentle remainder from uiet kuk library that we have started fine.
This is automatic mailing so don't reply. This is only for uiet kuk 
student. If you are not student so please ignore it.
'''
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.login(sender, password)
    message = "Subject: {}\n\n{}".format(subject, text)
    if  len(lstt)>0:
        smtp_server.sendmail(sender, recipient, message)
    smtp_server.close()
    L2 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text ="Done mailed.")
    L2.place(x=10,y=110)


def p_details():
    def p_show():
        rol=int(E_2.get())
        row =conn.execute('''select * from Records where Roll_no = ?''',(rol,))
        row1=conn.execute('''select * from RecordsEmail where Roll_no = ?''',(rol,))
        for rec in row1:
            L2 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Email of student: "+rec[1])
            L2.place(x=50,y=160)
            break
        lst1=[]
        total=0
        mpty=0
        for rec in row:
            book1=rec[1]
            d1=rec[6]
            book2=rec[2]
            d2=rec[7]
            book3=rec[3]
            d3=rec[8]
            book4=rec[4]
            d4=rec[9]
            book5=rec[5]
            d5=rec[10]
            break
        if book1!=0:
            mpty+=1
            lst1.append(book1)
            L3 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Book Number= "+str(book1)+"        Issue Date: "+ d1)
            L3.place(x=50,y=220)
        if book2!=0:
            mpty+=1
            lst1.append(book2)
            L4 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Book Number= "+ str(book2)+"        Issue Date: "+ d2)
            L4.place(x=50,y=280)
        if book3!=0:
            mpty+=1
            lst1.append(book3)
            L5 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Book Number= "+str(book3)+"        Issue Date: "+ d3)
            L5.place(x=50,y=340)
        if book4!=0:
            mpty+=1
            lst1.append(book4)
            L6 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Book Number= "+str(book4)+"        Issue Date: "+ d4)
            L6.place(x=50,y=400)
        if book5!=0:
            mpty+=1
            lst1.append(book5)
            L7 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text ="Book Number= "+ str(book5)+"        Issue Date: "+ d5)
            L7.place(x=50,y=460)
        days_free=0
        for i in range(len(lst1)):
            if book1 == lst1[i]:
                r_dat=date.today()
                a=int(d1[6:])
                b=int(d1[3:5])
                c=int(d1[:2])
                i_dat=date(a,b,c)
                delta=r_dat-i_dat
                dys=delta.days
                if dys>days_free:
                    dys=dys-days_free
                else:
                    dys=0
                total+=0.50*dys
            elif book2 == lst1[i]:
                r_dat=date.today()
                a=int(d2[6:])
                b=int(d2[3:5])
                c=int(d2[:2])
                i_dat=date(a,b,c)
                delta=r_dat-i_dat
                dys=delta.days
                if dys>days_free:
                    dys=dys-days_free
                else:
                    dys=0
                total+=0.50*dys
            elif book3 == lst1[i]:
                r_dat=date.today()
                a=int(d3[6:])
                b=int(d3[3:5])
                c=int(d3[:2])
                i_dat=date(a,b,c)
                delta=r_dat-i_dat
                dys=delta.days
                if dys>days_free:
                    dys=dys-days_free
                else:
                    dys=0
                total+=0.50*dys
            elif book4 == lst1[i]:
                r_dat=date.today()
                a=int(d4[6:])
                b=int(d4[3:5])
                c=int(d4[:2])
                i_dat=date(a,b,c)
                delta=r_dat-i_dat
                dys=delta.days
                if dys>days_free:
                    dys=dys-days_free
                else:
                    dys=0
                total+=0.50*dys
            elif book5 == lst1[i]:
                r_dat=date.today()
                a=int(d5[6:])
                b=int(d5[3:5])
                c=int(d5[:2])
                i_dat=date(a,b,c)
                delta=r_dat-i_dat
                dys=delta.days
                if dys>days_free:
                    dys=dys-days_free
                else:
                    dys=0
                total+=0.50*dys
        L8 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Total fine= "+str(total))
        L8.place(x=50,y=520)
    add1=Tk()
    add1.title("Show Details")
    add1.geometry("900x900")
    L1 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Roll Number")
    L1.place(x=50,y=10)
    E_2 = Entry(add1,font=16,textvariable = b)
    E_2.place(x=410,y=10)
    B_1 = Button(add1,activebackground='Green',activeforeground='Red',width=5,bd=5,bg='Yellow',font=16, text = "Show",command = p_show)
    B_1.place(x=350,y=100)
    add1.mainloop()

def p_mail_change():
    add1=Tk()
    add1.title("Edit Details")
    add1.geometry("900x900")
    def p_changeg():
        i=int(E_2.get())
        row1=conn.execute('''select * from RecordsEmail where Roll_no = ?''',(i,))
        ssa=''
        for rec in row1:
            ssa='Email for rollno '+str(i)+' is '+rec[1]
        def p_change_conf():
            rol=int(E_2.get())
            newEmail=E_3.get()
            conn.execute('''UPDATE RecordsEmail set 'Email'=? where Roll_no=?''',(newEmail,rol,))
            conn.commit()
            L4 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = 'Done')
            L4.place(x=150,y=360)
        L2 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = ssa)
        L2.place(x=50,y=160)
        L3 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = 'New Email: ')
        L3.place(x=50,y=220)
        E_3 = Entry(add1,font=16)
        E_3.place(x=410,y=220)
        B_1 = Button(add1,activebackground='Green',activeforeground='Red',width=8,bd=5,bg='Yellow',font=16, text = "Change",command = p_change_conf)
        B_1.place(x=350,y=300)
    L1 = Label(add1,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text = "Roll Number")
    L1.place(x=50,y=10)
    E_2 = Entry(add1,font=16,textvariable = b)
    E_2.place(x=410,y=10)
    B_1 = Button(add1,activebackground='Green',activeforeground='Red',width=5,bd=5,bg='Yellow',font=16, text = "Edit",command = p_changeg)
    B_1.place(x=350,y=100)
    add1.mainloop()
if not(passw()):
    exit()
root = Tk()
root.title("Library_Management")
root.geometry("900x900")

a='''UNIVERSITY INSTITUTE OF ENGINEERING AND TECHNOLOGY
         KURUKSHETRA UNIVERSITY
             KURUKSHETRA'''

c= StringVar()
b = StringVar()
rol = StringVar()
L = Label(root,activebackground='Green',activeforeground='Red',bg="light green",bd=5,font=16, text =a)
L.place(x=150,y=10)
b1="Enroll 1 or more student(s) having different roll numbers"
B_1 = Button(root,activebackground='Green',activeforeground='Red',width=53,bd=5,bg='Yellow',font=16, text =b1,command = p_add1)
B_1.place(x=150,y=100)

b2="Enroll students in a range"
B_2 = Button(root,activebackground='Green',activeforeground='Red',width=53,bd=5,bg='Yellow',font=16, text =b2, command=p_addrng)
B_2.place(x=150,y=160)

b3 = "Delete 1 or more students(s) having different roll numbers"
B_3 = Button(root,activebackground='Green',activeforeground='Red',width=53,bd=5,bg='Yellow',font=16, text =b3,command = p_del1)
B_3.place(x=150,y=220)

b4="Delete students in a range"
B_4 = Button(root,activebackground='Green',activeforeground='Red',width=53,bd=5,bg='Yellow',font=16, text =b4, command=p_delrng)
B_4.place(x=150,y=280)

b5="Issue book(s) for a roll number"
B_5 = Button(root,activebackground='Green',activeforeground='Red',width=53,bd=5,bg='Yellow',font=16, text =b5, command=p_issue)
B_5.place(x=150,y=340)

b6="Return book(s) by any student using roll number"
B_6 = Button(root,activebackground='Green',activeforeground='Red',width=53,bd=5,bg='Yellow',font=16, text =b6, command=p_delete)
B_6.place(x=150,y=400)

b7="To get mail those students whose fine already started"
B_7 = Button(root,activebackground='Green',activeforeground='Red',width=53,bd=5,bg='Yellow',font=16, text =b7, command= p_mail)
B_7.place(x=150,y=460)

b8="To get all details related to any student"
B_8 = Button(root,activebackground='Green',activeforeground='Red',width=53,bd=5,bg='Yellow',font=16, text =b8,command= p_details)
B_8.place(x=150,y=520)

b9="Edit the details i.e. change Email of any student"
B_9 = Button(root,activebackground='Green',activeforeground='Red',width=53,bd=5,bg='Yellow',font=16, text =b9, command=p_mail_change)
B_9.place(x=150,y=580)

B_10 = Button(root,activebackground='Green',activeforeground='Red',width=10,bd=5,bg='Yellow',font=16, text ="Exit",command = p_exit)
B_10.place(x=400,y=640)
root.mainloop()