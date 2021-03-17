# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:30:47 2021

@author: satyam singh
"""
import tkinter as tk
from tkinter import *
import sqlite3
master = Tk()
master.title('Registration Form')
master.geometry("400x300")
master.configure(background='light green')
registration=[]

#Connections
connection = sqlite3.connect("RegistrationForm.db")
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS RegistrationForm(Name, Course, Semester, Form Number, Contact Number, Email ID, Address)")

#Definitions
def Insert():
    connection = sqlite3.connect("RegistrationForm.db")
    st = "Insert into RegistrationForm values('"+str(name.get())+"', '"+str(course.get())+"', '"+str(sem.get())+"', '"+str(formNo.get())+"', '"+str(contactNo.get())+"' , '"+str(email.get())+"' , '"+str(address.get())+"')"
    print(st)
    connection.execute(st)
    connection.commit()
    connection.close()

def Delete():
    connection = sqlite3.connect("RegistrationForm.db")
    st = "Delete from RegistrationForm where name = '"+str(name.get())+"'"
    print(st)
    connection.execute(st)
    connection.commit()
    connection.close()
    
def Update():
    connection = sqlite3.connect("RegistrationForm.db")
    st1 = "Update RegistrationForm set Course = '"+str(course.get())+"' where name = '"+str(name.get())+"'"
    st2 = "Update RegistrationForm set Semester = '"+str(sem.get())+"' where name = '"+str(name.get())+"'"
    st3 = "Update RegistrationForm set Form = '"+str(formNo.get())+"' where name = '"+str(name.get())+"'"
    st4 = "Update RegistrationForm set Contact = '"+str(contactNo.get())+"' where name = '"+str(name.get())+"'"
    st5 = "Update RegistrationForm set Email = '"+str(email.get())+"' where name = '"+str(name.get())+"'"
    st6 = "Update RegistrationForm set Address = '"+str(address.get())+"' where name = '"+str(name.get())+"'"
    print(st1)
    connection.execute(st1)
    print(st2)
    connection.execute(st2)
    print(st3)
    connection.execute(st3)
    print(st4)
    connection.execute(st4)
    print(st5)
    connection.execute(st5)
    print(st6)
    connection.execute(st6)
    connection.commit()
    connection.close()
    
def Search():
    connection = sqlite3.connect("RegistrationForm.db")
    st = "Select * from RegistrationForm where name = '"+str(name.get())+"'"
    curs = connection.execute(st)
    for row in curs:
        name.set(row[0])
        course.set(row[1])
        sem.set(row[2])
        formNo.set(row[3])
        contactNo.set(row[4])
        email.set(row[5])
        address.set(row[6])
    connection.commit()
    connection.close()
    

    
#Frames   
formName = Label(master, text='Form',bg='light green')
formName.pack(pady=10)
frame1=Frame(master,bg='light green')
frame1.pack(side='top',padx=10)
frame2=Frame(master,bg='light green')
frame2.pack(side='top',padx=5,pady=20)

#Labels
name=Label(frame1,text='Name',bg='light green').grid(row = 0 , column = 0)
course=Label(frame1,text='Course',bg='light green').grid(row=1,column=0)
sem=Label(frame1,text='Semester',bg='light green').grid(row=2,column=0)
formNo=Label(frame1,text='Form No',bg='light green').grid(row=3,column=0)
contactNo=Label(frame1,text='Contact No',bg='light green').grid(row=4,column=0)
email=Label(frame1,text='Email ID',bg='light green').grid(row=5,column=0)
address=Label(frame1,text='Address',bg='light green').grid(row=6,column=0)

#Entries
name=tk.StringVar()
course=tk.StringVar()
sem=tk.StringVar()
formNo=tk.StringVar()
contactNo=tk.StringVar()
email=tk.StringVar()
address=tk.StringVar()

entryname=Entry(frame1, width='100',textvariable = name).grid(row=0,column=1)

entryCourse=Entry(frame1, width='100',textvariable = course).grid(row=1,column=1)

entrySem=Entry(frame1, width='100',textvariable = sem).grid(row=2,column=1)

entryformNo=Entry(frame1, width='100',textvariable = formNo).grid(row=3, column =1)

entrycontactNo=Entry(frame1, width='100',textvariable = contactNo).grid(row=4,column=1)

entryemail=Entry(frame1, width='100',textvariable = email).grid(row=5,column=1)

entryaddress=Entry(frame1, width='100',textvariable = address).grid(row=6,column=1)

insertButton=Button(frame2,text="Insert", bg='red',relief=RIDGE, command = Insert).grid(row=7,column=0,padx=10)

searchButton=Button(frame2,text="Search", bg='red',relief=RIDGE, command = Search).grid(row=7,column=1,padx=10)

deleteButton=Button(frame2,text="Delete", bg='red',relief=RIDGE, command = Delete).grid(row=7,column=2,padx=10)

updateButton=Button(frame2,text="Update", bg='red',relief=RIDGE, command = Update).grid(row=7,column=3,padx=10)

master.mainloop()