#====================User====================#
"""
    Project Created By:
        Us
    Thank You;
"""

#===============Importing Stuff==============#
from tabulate import tabulate
import mysql.connector as mc
import time

#Creative Menu
#Slow Printing(DONE)
#try to add colours
#Show report card(DONE)
#Second table on stream subject(DONE)

def menu():
    menuobject=open("menu.txt","r")
    l=len(menuobject.read())
    menuobject.seek(0)
    for x in range(0,l):
        t=menuobject.read(1)
        print(t,end="")
        time.sleep(0.03)
    menuobject.close()


def add():
    con = mc.connect(host="localhost", user="root", passwd='@ANIGAME0359')
    cur = con.cursor()
    cur.execute("create database if not exists project;")
    cur.execute("use project")
    cur.execute("create table if not exists students(rno int, sname varchar(20), addr varchar(50), cont bigint, primary key(rno));")
    print("Enter the number of students.")
    n=int(input(""))
    for x in range(n):
        rno = int(input("Enter the roll number: "))
        sname = input("Enter the name of the student: ")
        addr = input("Enter the student's address: ")
        cont = int(input("Enter the student's contact number: "))
        st = "insert into students values({} , '{}' , '{}' , {})".format(rno,sname,addr,cont)
        cur.execute(st)
        con.commit()
    con.close()    

def delete():
    con = mc.connect(host="localhost", user="root", passwd='@ANIGAME0359')
    cur = con.cursor()
    cur.execute("use project")
    print("Enter the role number of student whose details you want to forever remove. Non refundable.")
    n = int(input(""))
    cur.execute("delete from students where rno = {}".format(n))
    print("Updated data:")
    cur.execute("select * from students")
    data=cur.fetchall()
    hdr=['RollNo','Name','Address','ContactNumber']
    print(tabulate(data,headers=hdr,tablefmt="outline"))
    cur.commit()
    print("Updated Data:")
    cur.execute("select * from students")
    data=cur.fetchall()
    hdr=['RollNo','Name','Address','ContactNumber']
    print(tabulate(data,headers=hdr,tablefmt="outline"))
    con.close()

def update():
    con = mc.connect(host="localhost", user="root", passwd='@ANIGAME0359')
    cur = con.cursor()
    cur.execute("use project")
    print("Enter the roll number of the student whose details you would like to edit.")
    n=int(input(""))
    print("What would you like to edit?")
    print("1. Name")
    print("2. Address")
    print("3. Contact Number")
    m=int(input(""))
    if m==1:
        print("Enter New Name")
        nm=input("")
        cur.execute("update students set sname = '{}' where rno ={}".format(nm,n))
    elif m==2:
        print("Enter New Address")
        nm=input("")
        cur.execute("update students set addr = '{}' where rno ={}".format(nm,n))   
    elif m==3:
        print("Enter New Contact Number")
        nm=int(input(""))
        cur.execute("update students set cont = {} where rno ={}".format(nm,n))
    else:
        print("Wrong Input")
    cur.commit()
    print("Updated Data:")
    cur.execute("select * from students")
    data=cur.fetchall()
    hdr=['RollNo','Name','Address','ContactNumber']
    print(tabulate(data,headers=hdr,tablefmt="outline"))
    con.close()

def show():
    con = mc.connect(host="localhost", user="root", passwd='@ANIGAME0359')
    cur = con.cursor()
    cur.execute("use project")
    cur.execute("select * from students")
    data=cur.fetchall()
    hdr=['RollNo','Name','Address','ContactNumber']
    print(tabulate(data,headers=hdr,tablefmt="outline"))
    con.close()

def prints(r):
    con = mc.connect(host="localhost", user="root", passwd='@ANIGAME0359')
    cur = con.cursor()
    cur.execute("use project")
    printobject=open("prints.txt","r")
    l=len(printobject.read())
    printobject.seek(0)
    for x in range(0,l):
        t=printobject.read(1)
        print(t,end="")
        time.sleep(0.03)
    printobject.close()
    st=int(input("Your Choice of Stream: "))
    pfileobject=open("ReportCard.txt","w")
    pfileobject.write("||================================================||\n")
    pfileobject.write("\n")
    Roll="Roll Number: [(\'"+str(r)+"\')]\n"
    pfileobject.write(Roll)
    cur.execute("select sname from students where rno = {}".format(r))
    o=cur.fetchall()
    o=str(o)
    o=o[0:len(o)-3]+o[-2]+o[-1]
    Name="Name of the Student: "+str(o)+"\n"
    pfileobject.write(Name)
    cur.execute("select addr from students where rno = {}".format(r))
    o=cur.fetchall()
    o=str(o)
    o=o[0:len(o)-3]+o[-2]+o[-1]
    Addr="Address of the Student: "+str(o)+"\n"
    pfileobject.write(Addr)
    cur.execute("select cont from students where rno = {}".format(r))
    o=cur.fetchall()
    o=str(o)
    o=o[0:len(o)-3]+o[-2]+o[-1]
    Cont="Contact Number of the Student: "+str(o)+"\n"
    pfileobject.write(Cont)
    cur.execute("select stname from stream where sno = {}".format(st))
    o=cur.fetchall()
    o=str(o)
    o=o[0:len(o)-3]+o[-2]+o[-1]
    Stream="Stream Chosen of the Student: "+str(o)+"\n"
    pfileobject.write(Stream)
    pfileobject.write("\n")
    pfileobject.write("||================================================||")
    pfileobject.close()
    print2object=open("prints2.txt","r")
    l=len(print2object.read())
    print2object.seek(0)
    for x in range(0,l):
        t=print2object.read(1)
        print(t,end="")
        time.sleep(0.03)
    print2object.close()
    

def clientlogin():
    clientobject=open("client.txt","r")
    l=len(clientobject.read())
    clientobject.seek(0)
    for x in range(0,l):
        t=clientobject.read(1)
        print(t,end="")
        time.sleep(0.03)
    clientobject.close()
    r=int(input("Enter The Roll Number: "))
    con = mc.connect(host="localhost", user="root", passwd='@ANIGAME0359')
    cur = con.cursor()
    cur.execute("use project")
    cur.execute("select * from students where rno = {}".format(r))
    data=cur.fetchall()
    hdr=['RollNo','Name','Address','ContactNumber']
    print("")
    output=(tabulate(data,headers=hdr,tablefmt="outline"))
    print(output)
    print("")
    print("Would you like to print slip?")
    ch=input("")
    if ch=="Yes" or ch=="yes":
        prints(r)


def main():
    mainobject=open("main.txt","r")
    l=len(mainobject.read())
    mainobject.seek(0)
    for x in range(0,l):
        t=mainobject.read(1)
        print(t,end="")
        time.sleep(0.03)
    mainobject.close()
    choice = int(input("Enter Your Choice: "))
    if choice==1:
        adminlogin()
    elif choice==2:
        clientlogin()
    else:
        print("Wrong Choice")
    
menu()
main()

#GG BRO



    
