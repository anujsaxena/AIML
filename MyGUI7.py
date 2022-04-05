# Combobox Widget in tkinter
# Syntax : combobox = ttk.Combobox(master, option=value, ...)

import tkinter as tk
from tkinter import ttk

#create a window
win = tk.Tk()
win.title("Example of Combo Box")
win.geometry("500x300")

#label text of the title

ttk.Label(win, text="My Combo Box", background="green", foreground="white", font=("Times New Roman", 12)).grid(row=0, column=1)

#label
ttk.Label(win, text="Select Month",font=("Times New Roman", 10)).grid(row=5, column=0, padx=10, pady=25)

#create combobox
n = tk.StringVar()

monthch = ttk.Combobox(win, width=27, textvariable=n)

monthch['values']=( 'Select a month ..',
                 'January',
                 'Feb',
                 'March',
                 'April',
                 'May',
                 'June',
                 'July',
                 'August',
                 'September',
                 'October',
                 'Nov',
                 'December')

monthch.grid(column=1, row=5)

monthch.current(0)

win.mainloop()
