#label demo
from tkinter import Tk, mainloop, LEFT, TOP
from tkinter.ttk import *

# Creating tkinter window with fixed geometry
win = Tk()
win.geometry('250x250')

# This will create a LabelFrame
lf = LabelFrame(win, text='Exploring gUI')
lf.pack(expand='yes', fill='both')

btn1 = Button(lf, text="Button one!")
btn1.place(x=30,y=10)

btn2 = Button(lf, text="Button two!")
btn2.place(x=130,y=10)

#check buttons
cb1 = Checkbutton(lf, text="First Choice")
cb1.place(x=30,y=50)

cb2 = Checkbutton(lf, text="Second Choice")
cb2.place(x=30,y=80)

mainloop()