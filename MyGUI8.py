# Entry widget
#login screen

import tkinter as tk
win = tk.Tk()
win.geometry("600x500")

#declare string variables

name = tk.StringVar()
pwd = tk.StringVar()

#create a function

def submit():
    nm = name.get()
    password = pwd.get()

    print('The name is ', nm)
    print('Password entered is ', password)

    name.set("")
    pwd.set("")

#create label for name
n_label = tk.Label(win, text="Username ", fon=('calibre',12,'bold'))
n_entry = tk.Entry(win, textvariable=name,fon=('calibre',12,'normal') )

#create label for paswword
p_label = tk.Label(win, text="Password ", fon=('calibre',12,'bold'))
p_entry = tk.Entry(win, textvariable=pwd,fon=('calibre',12,'normal') )

#Create a submit button
sub_button = tk.Button(win, text="Submit", command=submit)

#put the things in the position
n_label.grid(row=0, column=0)
n_entry.grid(row=0, column=1)
p_label.grid(row=1, column=0)
p_entry.grid(row=1, column=1)
sub_button.grid(row=2, column=1)

#all done ... loop it
win.mainloop()