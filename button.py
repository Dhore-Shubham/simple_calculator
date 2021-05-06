from tkinter import *

root=Tk()

def myclick():
  mylabel=Label(root,text="i clicked my buttn..")
  mylabel.pack()

#button with different parameters


mybutton=Button(root,text="click Me..",padx=50,pady=50,command=myclick,fg="blue",bg="yellow")

mybutton.pack()

root.mainloop()