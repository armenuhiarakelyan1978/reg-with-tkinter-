#!/usr/bin/env python
#how to create simple Gui.
from Tkinter import *
#creating object 'root' of TK()
root = Tk()
root.geometry("500x500")
root.title('Registration form')
#this create 'Label' widget for Registration Form
label_0 = Label(root, text = "Registration form", width=20,font=("bold",20))
#place method in tkinter used to organize widget
label_0.place(x=90, y=60)

label_1= Label(root, text="FullName", width=20, font=("bold",10))
label_1.place(x=80,y=130)
#this will accept the input string text from user

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

#this create "Label"widget for Email
label_2 = Label(root,text="Email", width = 20, font=("bold",10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

var = IntVar()
Radiobutton(root, text="Male",padx = 6, variable=var,value=1).place(x=235, y=230)
Radiobutton(root,text="Female",padx = 6, variable=var,value=2).place(x=290,y=230)
label_4 = Label(root,text="Age:",width=20,font=("bold",10))
label_4.place(x=70,y=280)
entry_2 = Entry(root)
entry_2.place(x=240,y=280)
Button(root, text = "Submit", width=20, bg='brown',fg='white').place(x=180,y=380)

root.mainloop()
print("registration form seccussfully created")

