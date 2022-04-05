#label demo
from tkinter import Tk, mainloop, LEFT, TOP
from tkinter.ttk import *

# Creating tkinter window with fixed geometry
win = Tk()
win.geometry('250x250')

# This will create a LabelFrame
lf = LabelFrame(win, text='GUI Modules')
lf.pack(expand='yes', fill='both')

lf1 = Label(lf, text='1. Tkinter')
lf1.place(x=0, y=5)

lf2 = Label(lf, text='2. PyQT')
lf2.place(x=0, y=30)

lf3 = Label(lf,text='3. winQT')

lf3.place(x=0, y=55)
mainloop()