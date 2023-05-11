

from tkinter import *
import sqlite3
import tkinter  as tk 

from tkinter import ttk, LEFT, END
import tkinter.messagebox
import cv2
import os
from PIL import Image , ImageTk     
from PIL import Image


root = Tk()
root.geometry('500x500')
root.title("Registration Form")



image2 =Image.open('m.jpg')
image2 =image2.resize((500,500), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)




Id=StringVar()
Name=StringVar()
LastName=StringVar()
Address = StringVar()
status1=StringVar()
Mobile= StringVar()



def database():
   ID = Id.get()
   
   #conn = sqlite3.connect('face.db')
   

   my_conn = sqlite3.connect('face.db')
   r_set=my_conn.execute("select * from User where id =" + str(ID) +"");
   i=0 # row value inside the loop 
   for student in r_set: 
        for j in range(len(student)):
            e =tk.Entry(frame_display, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1




def display():
    
##### tkinter window ######
    
    print("Display.....")
    from subprocess import call
    call(["python", "display.py"])   
             
label_0 = Label(root, text="Registration Form",width=25,font=("bold", 22),fg="#FF8040",bg="black")
label_0.place(x=50,y=50)



label_1 = Label(root, text="ID",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Id,width=20,font=("bold", 10))
entry_1.place(x=280,y=130)



Button(root, text='Submit',width=20,bg='red',fg='white',command=database).place(x=80,y=400)

Button(root, text='Display',width=20,bg='red',fg='white',command=display).place(x=280,y=400)

root.mainloop()



