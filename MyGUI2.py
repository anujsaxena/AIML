# import everything from tkinter module
from tkinter import *

#tkinter.ttk will override any widget

from tkinter.ttk import *
# create a tkinter window
win = Tk()

# Open window/frame having dimension 500X500
win.geometry('300x300')

# Create a Button
btn = Button(win, text='Test Button !', command=win.destroy)

# Set the position of button on the top of window.
btn.pack(side='top')

win.mainloop()