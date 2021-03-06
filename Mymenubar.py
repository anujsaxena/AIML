# Menu widget in Tkinter
# Syntax: m= Menu(master, **options)
from tkinter import *

win = Tk()
ribbon = Menu(win)
win.title("My main menu")
win.config(menu=ribbon)
fileMenu = Menu(ribbon)
ribbon.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(labe='New Prpoject')
fileMenu.add_command(labe='New')
fileMenu.add_command(labe='New Scratch File')
fileMenu.add_separator()
fileMenu.add_command(labe='Save')
fileMenu.add_command(labe='Save as')
fileMenu.add_separator()
fileMenu.add_command(labe='Ext', command=win.quit)
EditMenu = Menu(ribbon)
ribbon.add_cascade(label="Edit", menu=EditMenu)
EditMenu.add_command(label='Undo Typing')
EditMenu.add_command(label='Redo Typing')
EditMenu.add_separator()
EditMenu.add_command(label='Cut')
EditMenu.add_command(label='Copy')

ViewMenu = Menu(ribbon)
ribbon.add_cascade(label="View", menu=ViewMenu)
ViewMenu.add_command(label='Tool Windows')
ViewMenu.add_command(label='Appearance')
ViewMenu.add_separator()
ViewMenu.add_command(label='Quick definition')
ViewMenu.add_command(label='Context_Info')

mainloop()

