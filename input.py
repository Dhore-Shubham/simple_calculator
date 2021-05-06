from tkinter import *

root=Tk()

e=Entry(root,width=50,bg="blue",fg="white",borderwidth=5)
e.pack()
e.insert(0,"enter your name:")


def myclick():
  hello="Hello.."+e.get()
  mylabel=Label(root,text=hello)
  mylabel.pack()

#button with different parameters


mybutton=Button(root,text="enter your name",command=myclick,fg="blue",bg="yellow")

mybutton.pack()

root.mainloop()