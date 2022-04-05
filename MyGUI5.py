#Canvas widget
#Syntax C = Canvas(root, height, width, bd, bg, ..)
'''
Optional parameters:

root = root window.
height = height of the canvas widget.
width = width of the canvas widget.
bg = background colour for canvas.
bd = border of the canvas window.
scrollregion (w, n, e, s)tuple defined as a region for scrolling left, top, bottom and right.
highlightcolor colour shown in the focus highlight.
cursor It can be defined as a cursor for the canvas which can be a circle, a do, an arrow etc.
confine decides if canvas can be accessed outside the scroll region.
relief type of the border which can be SUNKEN, RAISED, GROOVE and RIDGE.
'''

from tkinter import *
win = Tk()
c = Canvas(win, bg ='blue', height=250, width=350)
line = c.create_line(108, 120, 320, 40, fill='red')
arc = c.create_arc(180, 150, 80, 210, start=0, extent=220, fill='yellow')
oval = c.create_oval(80, 30, 140, 150, fill='green')

c.pack()
mainloop()

