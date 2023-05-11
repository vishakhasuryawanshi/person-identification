# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:41:26 2021

@author: srcdo
"""

from tkinter import *
import sqlite3
import tkinter.messagebox
import tkinter  as tk 
from tkinter import * 
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()
root.geometry('500x500')
root.title("Registration Form")


Name=StringVar()
LastName=StringVar()
Address = StringVar()
c=StringVar()
Mobile= StringVar()
Pword=StringVar()

#------------------------------------------------


root.configure(background="seashell2")
#root.geometry("1300x700")
import sqlite3
my_conn = sqlite3.connect('face.db')

#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.geometry("%dx%d+0+0" % (w, h))


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('bg1.jpg')
image2 =image2.resize((500,500), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image
background_label.place(x=0, y=0)
#------------------------------------------------------


#-------------------------------------------------

def database():
    
   
   name = Name.get()
   lastname = LastName.get()
   address = Address.get()
   status = c.get()
   mobileno = Mobile.get()
   password=Pword.get()
   conn = sqlite3.connect('face.db')
   with conn:
      cursor=conn.cursor()
  # cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
   cursor.execute('INSERT INTO User (Name,Lastname,Address,Status,Mobileno,Password) VALUES(?,?,?,?,?,?)',(name,lastname,address,status,mobileno,password))
   conn.commit()
   tkinter.messagebox.showinfo('PopUp','REGISTRATION SUCCESSFULLY!!!!!!!!!')
   
  


   
def display():
    
##### tkinter window ######
    
    print("SS")
    from subprocess import call
    call(["python", "display.py"])   
             
label_0 = Label(root, text="Register Here",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="First Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Name,bg="lightgray")
entry_1.place(x=300,y=130)

label_2 = Label(root, text="Last Name",width=20,font=("bold", 10))
label_2.place(x=80,y=180)

entry_2 = Entry(root,textvar=LastName,bg="lightgray")
entry_2.place(x=300,y=180)

label_3 = Label(root, text="Address",width=20,font=("bold", 10))
label_3.place(x=80,y=230)

entry_3 = Entry(root,textvar=Address,bg="lightgray")
entry_3.place(x=300,y=230)

label_4 = Label(root, text="Status",width=20,font=("bold", 10))
label_4.place(x=80,y=280)

list1 = ['Criminal Person','Missing Person','Normal Person'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=20)
c.set('Select Status of Person') 
droplist.place(x=300,y=280)

label_5 = Label(root, text="Mobile No",width=20,font=("bold", 10))
label_5.place(x=80,y=330)

entry_5 = Entry(root,textvar=Mobile,bg="lightgray")
entry_5.place(x=300,y=330)

label_5 = Label(root, text="Password",width=20,font=("bold", 10))
label_5.place(x=80,y=380)

entry_5 = Entry(root,show='*',textvar=Pword,bg="lightgray")
entry_5.place(x=300,y=380)

Button(root, text='Register Now',width=20,bg='brown',fg='white',command=database).place(x=180,y=420)


root.mainloop()


